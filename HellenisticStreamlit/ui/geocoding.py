"""Geocoding + timezone resolution.

Nominatim (OpenStreetMap) for free place→lat/lng. timezonefinder for
lat/lng→IANA timezone. No API keys required.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

import streamlit as st


@dataclass(frozen=True)
class GeocodeResult:
    place_name: str
    latitude: float
    longitude: float
    tz_id: str


@st.cache_data(ttl=24 * 3600, show_spinner=False)
def geocode(place: str) -> Optional[GeocodeResult]:
    """Look up `place` via Nominatim and resolve its IANA timezone."""
    from geopy.geocoders import Nominatim
    from timezonefinder import TimezoneFinder

    geolocator = Nominatim(user_agent="hellenistic-astrology-streamlit/1.0")
    location = geolocator.geocode(place, addressdetails=False, timeout=10)
    if location is None:
        return None

    tf = TimezoneFinder()
    tz_id = tf.timezone_at(lat=location.latitude, lng=location.longitude)
    if tz_id is None:
        return None

    return GeocodeResult(
        place_name=location.address,
        latitude=location.latitude,
        longitude=location.longitude,
        tz_id=tz_id,
    )
