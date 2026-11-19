
import streamlit as st
import requests
import pandas as pd

from streamlit_geolocation import streamlit_geolocation


# -----------------------------------
# 1. Get TomTom API Key
# -----------------------------------

def get_tomtom_key():
    try:
        return st.secrets["TOMTOM_API_KEY"]

    except Exception:
        st.error(
            "TomTom API key not found. "
            "Please configure .streamlit/secrets.toml"
        )
        return None


# -----------------------------------
# 2. Get Live Traffic from TomTom
# -----------------------------------

def get_live_traffic(latitude, longitude):

    api_key = get_tomtom_key()

    if not api_key:
        return None

    url = (
        "https://api.tomtom.com/traffic/services/4/"
        "flowSegmentData/absolute/10/json"
    )

    params = {
        "key": api_key,
        "point": f"{latitude},{longitude}",
        "unit": "kmph"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        return data.get("flowSegmentData")

    except requests.exceptions.RequestException as error:
        st.error(f"TomTom API error: {error}")
        return None

    except ValueError:
        st.error("Invalid response received from TomTom.")
        return None


# -----------------------------------
# 3. Display GPS and Traffic Details
# -----------------------------------

def show_gps_traffic():

    st.header("Live GPS Traffic Monitoring")

    st.write(
        "Click the location button below and allow browser "
        "location permission to detect your current location."
    )

    # Get browser location
    location = streamlit_geolocation()

    if not location:
        st.info(
            "Click the location button to get your GPS location."
        )
        return

    # Extract coordinates
    latitude = location.get("latitude")
    longitude = location.get("longitude")
    accuracy = location.get("accuracy")

    # Check location availability
    if latitude is None or longitude is None:

        st.info("Waiting for GPS location permission.")
        return

    # Convert coordinates to numbers
    try:
        latitude = float(latitude)
        longitude = float(longitude)

    except (TypeError, ValueError):
        st.error("Invalid GPS coordinates received.")
        return

    # Validate latitude
    if not -90 <= latitude <= 90:

        st.error("Invalid latitude received.")
        return

    # Validate longitude
    if not -180 <= longitude <= 180:

        st.error("Invalid longitude received.")
        return

    # -----------------------------------
    # 4. Display GPS Information
    # -----------------------------------

    st.success("GPS location detected successfully!")

    st.subheader("Your Current Location")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Latitude",
            f"{latitude:.7f}"
        )

    with col2:
        st.metric(
            "Longitude",
            f"{longitude:.7f}"
        )

    if accuracy is not None:

        try:
            accuracy = float(accuracy)

            st.metric(
                "GPS Accuracy",
                f"{accuracy:.1f} metres"
            )

            if accuracy <= 20:
                st.success("Good location accuracy.")

            elif accuracy <= 100:
                st.info("Reasonable location accuracy.")

            else:
                st.warning(
                    "Location is approximate. "
                    "Your laptop may not have precise GPS hardware."
                )

        except (TypeError, ValueError):
            st.warning("GPS accuracy value is invalid.")

    else:
        st.warning("GPS accuracy is not available.")

    # -----------------------------------
    # 5. Display Location on Map
    # -----------------------------------

    st.subheader("Location Map")

    map_data = pd.DataFrame({
        "latitude": [latitude],
        "longitude": [longitude]
    })

    st.map(map_data, zoom=15)

    # -----------------------------------
    # 6. Fetch TomTom Live Traffic
    # -----------------------------------

    st.subheader("Live Traffic Information")

    st.caption(
        f"Request coordinates: "
        f"{latitude:.7f}, {longitude:.7f}"
    )

    with st.spinner("Fetching live traffic from TomTom..."):

        traffic = get_live_traffic(
            latitude,
            longitude
        )

    if not traffic:

        st.warning(
            "Traffic information is currently unavailable."
        )
        return

    # -----------------------------------
    # 7. Extract Traffic Information
    # -----------------------------------

    current_speed = traffic.get("currentSpeed")

    free_flow_speed = traffic.get("freeFlowSpeed")

    confidence = traffic.get("confidence")

    travel_time = traffic.get("currentTravelTime")

    road_closure = traffic.get("roadClosure", False)

    # Validate traffic data
    if current_speed is None or free_flow_speed is None:

        st.warning("Traffic speed data is incomplete.")
        return

    # -----------------------------------
    # 8. Display Traffic Speed
    # -----------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Current Traffic Speed",
            f"{current_speed} km/h"
        )

    with col2:

        st.metric(
            "Free Flow Speed",
            f"{free_flow_speed} km/h"
        )

    # -----------------------------------
    # 9. Predict Traffic Condition
    # -----------------------------------

    st.subheader("Traffic Condition")

    if road_closure:

        st.error("Road closure reported by TomTom.")

    elif free_flow_speed <= 0:

        st.warning(
            "Unable to determine traffic condition."
        )

    else:

        speed_ratio = current_speed / free_flow_speed

        if speed_ratio >= 0.75:

            st.success("Low Traffic")

        elif speed_ratio >= 0.40:

            st.warning("Moderate Traffic")

        else:

            st.error("Heavy Traffic")

    # -----------------------------------
    # 10. Travel Time
    # -----------------------------------

    if travel_time is not None:

        st.metric(
            "Current Segment Travel Time",
            f"{travel_time} seconds"
        )

    # -----------------------------------
    # 11. TomTom Confidence
    # -----------------------------------

    if confidence is not None:

        st.write(
            f"TomTom data confidence: "
            f"{confidence * 100:.1f}%"
        )

    # -----------------------------------
    # 12. Information
    # -----------------------------------

    st.caption(
        "Traffic information is based on the nearest road segment "
        "provided by TomTom. Browser location accuracy depends "
        "on your device and location services."
    )
