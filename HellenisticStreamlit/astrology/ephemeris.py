"""Swiss Ephemeris wrapper — tropical, geocentric, whole-sign-houses friendly.

Uses pyswisseph (PyPI: `pyswisseph`). The free Moshier built-in works without
any ephemeris files; for higher precision you can drop Swiss Ephemeris data
files alongside the project and call `swe.set_ephe_path(...)`.
"""
from __future__ import annotations
from dataclasses import dataclass

import swisseph as swe

from models.planet import Planet


# pyswisseph planet IDs.
_PLANET_ID: dict[Planet, int] = {
    Planet.SUN:     swe.SUN,
    Planet.MOON:    swe.MOON,
    Planet.MERCURY: swe.MERCURY,
    Planet.VENUS:   swe.VENUS,
    Planet.MARS:    swe.MARS,
    Planet.JUPITER: swe.JUPITER,
    Planet.SATURN:  swe.SATURN,
}


# Default: Swiss flag + speed (so we can detect retrograde via negative longitude speed).
_FLAGS = swe.FLG_SWIEPH | swe.FLG_SPEED


@dataclass(frozen=True)
class PlanetSample:
    longitude: float       # tropical ecliptic, degrees 0..<360
    speed_longitude: float # degrees per day; negative = retrograde
    is_retrograde: bool


def planet_sample(planet: Planet, julian_day_ut: float) -> PlanetSample:
    """Return position and motion for `planet` at the given Julian Day (UT)."""
    result, _retflag = swe.calc_ut(julian_day_ut, _PLANET_ID[planet], _FLAGS)
    longitude = result[0]
    speed = result[3]
    return PlanetSample(
        longitude=longitude,
        speed_longitude=speed,
        is_retrograde=speed < 0,
    )


def angles(julian_day_ut: float, latitude: float, longitude: float) -> tuple[float, float]:
    """Return (ascendant_longitude, midheaven_longitude) at the given moment + location.

    `swe.houses` returns (cusps, ascmc) where ascmc[0]=Asc, ascmc[1]=MC.
    We use 'W' (whole-sign) here for clarity, though for Asc/MC the house
    system doesn't matter — those two angles are geometric quantities
    independent of house division.
    """
    _cusps, ascmc = swe.houses(julian_day_ut, latitude, longitude, b'W')
    return ascmc[0], ascmc[1]
