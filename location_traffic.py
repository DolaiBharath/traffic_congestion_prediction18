
import streamlit as st
import requests
import folium

from streamlit_folium import st_folium


# ==========================================
# GET TOMTOM API KEY
# ==========================================

def get_api_key():
    try:
        return st.secrets["TOMTOM_API_KEY"]

    except Exception:
        st.error("TomTom API key not found.")
        return None


# ==========================================
# SEARCH LOCATION USING PLACES SEARCH API
# ==========================================

def search_location(place):

    api_key = get_api_key()

    if not api_key:
        return None

    url = "https://api.tomtom.com/maps/orbis/places/discover"

    headers = {
        "TomTom-Api-Key": api_key,
        "TomTom-Api-Version": "3",
        "Attributes": "results(title,position,address)",
        "Content-Type": "application/json"
    }

    payload = {
        "query": place,
        "maxResults": 5,
        "geopoliticalView": "IN",
        "filters": {
            "countryCodesIso2": ["IN"]
        }
    }

    try:

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=15
        )

        response.raise_for_status()

        results = response.json().get("results", [])

        if results:

            coordinates = results[0]["position"]["coordinates"]

            longitude = coordinates[0]
            latitude = coordinates[1]

            return latitude, longitude

        return None

    except requests.exceptions.RequestException as error:

        st.error(f"Location search error: {error}")

        if error.response is not None:
            st.write("TomTom response:", error.response.text)

        return None


# ==========================================
# FETCH LIVE TRAFFIC
# ==========================================

def get_selected_traffic(latitude, longitude):

    api_key = get_api_key()

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

        return response.json().get("flowSegmentData")

    except requests.exceptions.RequestException as error:

        st.error(f"Traffic API error: {error}")

        return None


# ==========================================
# DISPLAY SELECTED LOCATION TRAFFIC
# ==========================================

def display_traffic(latitude, longitude):

    traffic = get_selected_traffic(
        latitude,
        longitude
    )

    if not traffic:

        st.warning(
            "Traffic information unavailable for this location."
        )

        return

    current_speed = traffic.get("currentSpeed")
    free_flow_speed = traffic.get("freeFlowSpeed")

    st.subheader("Selected Location Traffic")

    st.write(f"Latitude: {latitude:.6f}")
    st.write(f"Longitude: {longitude:.6f}")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Current Speed",
            f"{current_speed} km/h"
            if current_speed is not None
            else "Unavailable"
        )

    with col2:

        st.metric(
            "Free Flow Speed",
            f"{free_flow_speed} km/h"
            if free_flow_speed is not None
            else "Unavailable"
        )

    # Traffic classification

    if current_speed is not None and free_flow_speed is not None:

        if free_flow_speed <= 0:

            st.warning(
                "Unable to determine traffic condition."
            )

        else:

            ratio = current_speed / free_flow_speed

            if ratio >= 0.75:

                st.success("Low Traffic")

            elif ratio >= 0.40:

                st.warning("Moderate Traffic")

            else:

                st.error("Heavy Traffic")

    # Additional traffic information

    travel_time = traffic.get("currentTravelTime")
    confidence = traffic.get("confidence")

    if travel_time is not None:

        st.metric(
            "Travel Time",
            f"{travel_time} seconds"
        )

    if confidence is not None:

        st.write(
            f"TomTom Confidence: {confidence * 100:.1f}%"
        )

    road_closure = traffic.get("roadClosure")

    if road_closure is not None:

        st.write(
            f"Road Closure: {road_closure}"
        )


# ==========================================
# MAIN LOCATION TRAFFIC FEATURE
# ==========================================

def show_location_traffic():

    st.header("Traffic Check by Location")

    st.write(
        "Search for a place or click anywhere on the map "
        "to check its live traffic."
    )

    # --------------------------------------
    # LOCATION SEARCH
    # --------------------------------------

    search_text = st.text_input(
        "Search a road or location",
        placeholder="Example: Kaza, Guntur, Andhra Pradesh"
    )

    if st.button("Search Location"):

        if search_text.strip():

            result = search_location(
                search_text.strip()
            )

            if result:

                st.session_state.selected_traffic_location = result

                st.success(
                    "Location found successfully!"
                )

                st.rerun()

            else:

                st.warning(
                    "Location not found. Please try another search."
                )

        else:

            st.warning(
                "Please enter a location."
            )

    # --------------------------------------
    # DEFAULT MAP LOCATION
    # --------------------------------------

    default_location = (17.3850, 78.4867)

    selected = st.session_state.get(
        "selected_traffic_location",
        default_location
    )

    # --------------------------------------
    # CREATE INTERACTIVE MAP
    # --------------------------------------

    traffic_map = folium.Map(
        location=selected,
        zoom_start=13
    )

    folium.Marker(
        selected,
        tooltip="Selected location",
        popup="Check traffic here"
    ).add_to(traffic_map)

    # --------------------------------------
    # DISPLAY MAP
    # --------------------------------------

    map_result = st_folium(
        traffic_map,
        height=500,
        width=None,
        key="traffic_location_map",
        returned_objects=["last_clicked"]
    )

    # --------------------------------------
    # CAPTURE CLICKED LOCATION
    # --------------------------------------

    if map_result and map_result.get("last_clicked"):

        clicked = map_result["last_clicked"]

        clicked_location = (
            clicked["lat"],
            clicked["lng"]
        )

        st.session_state.selected_traffic_location = clicked_location

        st.rerun()

    # --------------------------------------
    # DISPLAY SELECTED COORDINATES
    # --------------------------------------

    selected = st.session_state.get(
        "selected_traffic_location",
        default_location
    )

    st.subheader("Selected Location")

    st.write(
        f"Latitude: {selected[0]:.6f}"
    )

    st.write(
        f"Longitude: {selected[1]:.6f}"
    )

    # --------------------------------------
    # CHECK TRAFFIC
    # --------------------------------------

    if st.button("Check Traffic at Selected Location"):

        display_traffic(
            selected[0],
            selected[1]
        )
