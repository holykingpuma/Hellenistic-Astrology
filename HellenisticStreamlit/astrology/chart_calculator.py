"""Cast a NatalChart from BirthData.

Ports `Astrology/ChartCalculator.swift`. Steps:
1. Planetary positions (longitude, retrograde flag) via pyswisseph.
2. Angles (Asc, MC).
3. Sect from Sun's whole-sign house offset from the Ascendant.
4. The seven Hermetic Lots (Brennan Ch. 17).
"""
from __future__ import annotations

from models.birth_data import BirthData
from models.lot import ALL_LOTS, HermeticLot, HermeticLotPosition
from models.natal_chart import NatalChart
from models.planet import ALL_PLANETS, Planet, PlanetaryPosition
from models.sect import Sect

from . import ephemeris


def _normalize(deg: float) -> float:
    mod = deg % 360.0
    return mod + 360.0 if mod < 0 else mod


def cast(birth_data: BirthData) -> NatalChart:
    jd = birth_data.julian_day_ut

    # 1. Planetary positions.
    positions: list[PlanetaryPosition] = []
    samples: dict[Planet, ephemeris.PlanetSample] = {}
    for p in ALL_PLANETS:
        s = ephemeris.planet_sample(p, jd)
        samples[p] = s
        positions.append(PlanetaryPosition(planet=p, longitude=s.longitude, is_retrograde=s.is_retrograde))

    # 2. Angles.
    asc, mc = ephemeris.angles(jd, birth_data.latitude, birth_data.longitude)

    # 3. Sect — Sun's whole-sign house offset. Houses 7..12 (offsets 6..11) are
    #    the upper hemisphere — diurnal birth. Houses 1..6 (offsets 0..5) are
    #    the lower hemisphere — nocturnal birth.
    asc_sign = int(asc / 30.0) % 12
    sun_sign = int(samples[Planet.SUN].longitude / 30.0) % 12
    sun_offset = (sun_sign - asc_sign) % 12
    sect = Sect.DIURNAL if sun_offset >= 6 else Sect.NOCTURNAL

    # 4. Hermetic Lots.
    lots = _compute_lots(asc=asc, samples=samples, sect=sect)

    return NatalChart(
        birth_data=birth_data,
        ascendant_longitude=asc,
        midheaven_longitude=mc,
        positions=tuple(positions),
        sect=sect,
        lots=tuple(lots),
    )


def _compute_lots(asc: float,
                  samples: dict[Planet, ephemeris.PlanetSample],
                  sect: Sect) -> list[HermeticLotPosition]:
    """Compute all seven Hermetic Lots in dependency order.

    Fortune & Spirit are mirror images of each other across the Ascendant.
    The other five reference Fortune or Spirit, so we compute those two first.
    """
    sun = samples[Planet.SUN].longitude
    moon = samples[Planet.MOON].longitude
    mercury = samples[Planet.MERCURY].longitude
    venus = samples[Planet.VENUS].longitude
    mars = samples[Planet.MARS].longitude
    jupiter = samples[Planet.JUPITER].longitude
    saturn = samples[Planet.SATURN].longitude

    if sect is Sect.DIURNAL:
        fortune = _normalize(asc + moon - sun)
        spirit  = _normalize(asc + sun - moon)
    else:
        fortune = _normalize(asc + sun - moon)
        spirit  = _normalize(asc + moon - sun)

    def lot_formula(day_pos: float, day_neg: float) -> float:
        if sect is Sect.DIURNAL:
            return _normalize(asc + day_pos - day_neg)
        return _normalize(asc + day_neg - day_pos)

    eros      = lot_formula(venus,   spirit)
    necessity = lot_formula(fortune, mercury)
    courage   = lot_formula(fortune, mars)
    victory   = lot_formula(jupiter, spirit)
    nemesis   = lot_formula(fortune, saturn)

    return [
        HermeticLotPosition(kind=HermeticLot.FORTUNE,   longitude=fortune),
        HermeticLotPosition(kind=HermeticLot.SPIRIT,    longitude=spirit),
        HermeticLotPosition(kind=HermeticLot.EROS,      longitude=eros),
        HermeticLotPosition(kind=HermeticLot.NECESSITY, longitude=necessity),
        HermeticLotPosition(kind=HermeticLot.COURAGE,   longitude=courage),
        HermeticLotPosition(kind=HermeticLot.VICTORY,   longitude=victory),
        HermeticLotPosition(kind=HermeticLot.NEMESIS,   longitude=nemesis),
    ]
