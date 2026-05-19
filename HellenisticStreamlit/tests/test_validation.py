"""Validation test — output parity with the iOS app's test native.

Quebec 1993: June 24 1993, 14:36 EDT, Quebec City (46.81°N, 71.21°W).
Expected (per pyswisseph verification documented in project memory):
- Libra Asc 22.84°
- Cancer Sun 3.24° (10th)
- Virgo Moon 4.34° (12th)
- Cancer Mercury 26.46° (10th)
- Taurus Venus 18.11° (8th — domicile)
- Virgo Mars 0.84° (12th)
- Libra Jupiter 5.58° (1st)
- Pisces Saturn 0.16° R (6th)
- Day chart; Mars-Saturn partile opposition 0.68°
"""
from __future__ import annotations
import sys
from datetime import datetime
from pathlib import Path

# Make project root importable when running this file directly.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from astrology import aspect_calculator, chart_calculator
from models.birth_data import BirthData
from models.planet import Planet
from models.sect import Sect
from models.zodiac import ZodiacSign


TOLERANCE_DEG = 0.05  # Swiss Ephemeris is sub-arcsecond; we allow a tiny margin.


def _build_chart():
    bd = BirthData(
        name="Test Native",
        local_birth_moment=datetime(1993, 6, 24, 14, 36, 0),
        tz_id="America/Toronto",
        latitude=46.81,
        longitude=-71.21,
        place_name="Quebec City",
    )
    return chart_calculator.cast(bd)


def test_ascendant():
    chart = _build_chart()
    assert chart.ascendant_sign is ZodiacSign.LIBRA
    asc_deg = chart.ascendant_longitude % 30
    assert abs(asc_deg - 22.84) < TOLERANCE_DEG, asc_deg


def test_sect_is_diurnal():
    chart = _build_chart()
    assert chart.sect is Sect.DIURNAL


def test_planet_signs_and_houses():
    chart = _build_chart()
    expected = {
        Planet.SUN:     (ZodiacSign.CANCER,  10, 3.24),
        Planet.MOON:    (ZodiacSign.VIRGO,   12, 4.34),
        Planet.MERCURY: (ZodiacSign.CANCER,  10, 26.46),
        Planet.VENUS:   (ZodiacSign.TAURUS,   8, 18.11),
        Planet.MARS:    (ZodiacSign.VIRGO,   12, 0.84),
        Planet.JUPITER: (ZodiacSign.LIBRA,    1, 5.58),
        Planet.SATURN:  (ZodiacSign.PISCES,   6, 0.16),
    }
    for planet, (sign, house, degree) in expected.items():
        pos = chart.position(planet)
        assert pos is not None
        assert pos.sign is sign, f"{planet.value}: expected {sign.display_name}, got {pos.sign.display_name}"
        assert chart.house_place_for_sign(pos.sign).value == house, planet
        assert abs(pos.sign_degree - degree) < TOLERANCE_DEG, (planet.value, pos.sign_degree, degree)


def test_saturn_retrograde():
    chart = _build_chart()
    sat = chart.position(Planet.SATURN)
    assert sat is not None and sat.is_retrograde


def test_mars_saturn_partile_opposition():
    chart = _build_chart()
    aspects = aspect_calculator.aspects_in(chart)
    match = next(
        (a for a in aspects
         if {a.first, a.second} == {Planet.MARS, Planet.SATURN}),
        None,
    )
    assert match is not None
    assert match.kind.value == "opposition"
    assert match.is_partile
    assert abs(match.orb - 0.68) < 0.05, match.orb


if __name__ == "__main__":
    # Run as a simple script (no pytest dep required for the user).
    for fn_name in [
        "test_ascendant", "test_sect_is_diurnal", "test_planet_signs_and_houses",
        "test_saturn_retrograde", "test_mars_saturn_partile_opposition",
    ]:
        fn = globals()[fn_name]
        try:
            fn()
            print(f"✓ {fn_name}")
        except AssertionError as e:
            print(f"✗ {fn_name}: {e}")
            sys.exit(1)
    print("\nAll validation tests passed.")
