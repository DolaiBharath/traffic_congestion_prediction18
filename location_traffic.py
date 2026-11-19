
import streamlit as st
import requests
import folium

from streamlit_folium import st_folium


# Get TomTom API key
def get_api_key():
    try:
        return st.secrets["TOMTOM_API_KEY"]
    except Exception:
        st.error("TomTom API key not found.")
        return None


# Search for a location using TomTom Search API
def search_location(place):

    api_key = get_api_key()

    if not api_key:
        return None

    url = "https://api.tomtom.com/search/2/geocode/" + requests.utils.quote(place) + ".json"

    params = {
        "key": api_key,
        "limit": 1
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        results = response.json().get("results", [])

        if results:
            position = results[0]["position"]

            return (
                position["lat"],
                position["lon"]
            )

        return None

    except requests.exceptions.RequestException as error:
        st.error(f"Location search error: {error}")
        return None


# Fetch live traffic
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


# Display selected traffic
def display_traffic(latitude, longitude):

    traffic = get_selected_traffic(
        latitude,
        longitude
    )

    if not traffic:
        st.warning("Traffic information unavailable for this location.")
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
            if current_speed is not None else "Unavailable"
        )

    with col2:
        st.metric(
            "Free Flow Speed",
            f"{free_flow_speed} km/h"
            if free_flow_speed is not None else "Unavailable"
        )

    if current_speed is not None and free_flow_speed is not None:

        if free_flow_speed <= 0:
            st.warning("Unable to determine traffic condition.")

        else:
            ratio = current_speed / free_flow_speed

            if ratio >= 0.75:
                st.success("Low Traffic")

            elif ratio >= 0.40:
                st.warning("Moderate Traffic")

            else:
                st.error("Heavy Traffic")

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


# Main feature
def show_location_traffic():

    st.header("Traffic Check by Location")

    st.write(
        "Search for a place or click anywhere on the map "
        "to check its live traffic."
    )

    # Location search
    search_text = st.text_input(
        "Search a road or location",
        placeholder="Example: Hitech City, Hyderabad"
    )

    if st.button("Search Location"):

        if search_text.strip():

            result = search_location(search_text.strip())

            if result:
                st.session_state.selected_traffic_location = result
                st.success("Location found successfully!")

            else:
                st.warning("Location not found.")

        else:
            st.warning("Please enter a location.")

    # Default map center
    default_location = (17.3850, 78.4867)

    selected = st.session_state.get(
        "selected_traffic_location",
        default_location
    )

    # Create map
    traffic_map = folium.Map(
        location=selected,
        zoom_start=13
    )

    folium.Marker(
        selected,
        tooltip="Selected location",
        popup="Check traffic here"
    ).add_to(traffic_map)

    # Display interactive map
    map_result = st_folium(
        traffic_map,
        height=500,
        width=None,
        key="traffic_location_map"
    )

    # Capture clicked location
    if map_result and map_result.get("last_clicked"):

        clicked = map_result["last_clicked"]

        clicked_location = (
            clicked["lat"],
            clicked["lng"]
        )

        st.session_state.selected_traffic_location = clicked_location

    # Show selected coordinates
    selected = st.session_state.get(
        "selected_traffic_location",
        default_location
    )

    st.write(
        f"Selected Latitude: {selected[0]:.6f}"
    )

    st.write(
        f"Selected Longitude: {selected[1]:.6f}"
    )

    if st.button("Check Traffic at Selected Location"):

        display_traffic(
            selected[0],
            selected[1]
        )
