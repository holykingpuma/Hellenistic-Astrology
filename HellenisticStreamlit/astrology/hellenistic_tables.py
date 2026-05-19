"""All canonical Hellenistic reference tables in one place.

Verified against:
- Brennan, Hellenistic Astrology, Ch. 8 (Dignities) — primary source
- George, Ancient Astrology Vol II — essential dignities chapter
- Avelar & Ribeiro, On the Heavenly Spheres, Ch. 4

Changing values here will ripple through every analyzer. Do not touch
unless cross-referencing the cited primary sources.
"""
from __future__ import annotations
from dataclasses import dataclass

from models.house import HousePlace
from models.planet import Planet
from models.zodiac import Element, ZodiacSign


# Domicile rulers (Brennan p. 233, Fig 8.2)
DOMICILE_RULER: dict[ZodiacSign, Planet] = {
    ZodiacSign.ARIES:       Planet.MARS,
    ZodiacSign.TAURUS:      Planet.VENUS,
    ZodiacSign.GEMINI:      Planet.MERCURY,
    ZodiacSign.CANCER:      Planet.MOON,
    ZodiacSign.LEO:         Planet.SUN,
    ZodiacSign.VIRGO:       Planet.MERCURY,
    ZodiacSign.LIBRA:       Planet.VENUS,
    ZodiacSign.SCORPIO:     Planet.MARS,
    ZodiacSign.SAGITTARIUS: Planet.JUPITER,
    ZodiacSign.CAPRICORN:   Planet.SATURN,
    ZodiacSign.AQUARIUS:    Planet.SATURN,
    ZodiacSign.PISCES:      Planet.JUPITER,
}


# Exaltations & falls (Brennan p. 240-249, Fig 8.5)
@dataclass(frozen=True)
class Exaltation:
    sign: ZodiacSign
    exact_degree: int       # degree within the sign of perfection
    fall_sign: ZodiacSign


EXALTATION: dict[Planet, Exaltation] = {
    Planet.SUN:     Exaltation(ZodiacSign.ARIES,     19, ZodiacSign.LIBRA),
    Planet.MOON:    Exaltation(ZodiacSign.TAURUS,     3, ZodiacSign.SCORPIO),
    Planet.MERCURY: Exaltation(ZodiacSign.VIRGO,     15, ZodiacSign.PISCES),
    Planet.VENUS:   Exaltation(ZodiacSign.PISCES,    27, ZodiacSign.VIRGO),
    Planet.MARS:    Exaltation(ZodiacSign.CAPRICORN, 28, ZodiacSign.CANCER),
    Planet.JUPITER: Exaltation(ZodiacSign.CANCER,    15, ZodiacSign.CAPRICORN),
    Planet.SATURN:  Exaltation(ZodiacSign.LIBRA,     21, ZodiacSign.ARIES),
}


# Triplicity rulers — Dorothean scheme (Brennan p. 267 Table 8.1)
@dataclass(frozen=True)
class TriplicityRulership:
    day: Planet
    night: Planet
    cooperating: Planet      # "participating" — third ruler


TRIPLICITY: dict[str, TriplicityRulership] = {
    Element.FIRE:  TriplicityRulership(Planet.SUN,    Planet.JUPITER, Planet.SATURN),
    Element.EARTH: TriplicityRulership(Planet.VENUS,  Planet.MOON,    Planet.MARS),
    Element.AIR:   TriplicityRulership(Planet.SATURN, Planet.MERCURY, Planet.JUPITER),
    Element.WATER: TriplicityRulership(Planet.VENUS,  Planet.MARS,    Planet.MOON),
}


# Egyptian bounds (Brennan p. 277, Table 8.3)
# For each sign, 5 bound rulers and the exclusive upper degree.
# Sun and Moon receive no bounds.
@dataclass(frozen=True)
class Bound:
    ruler: Planet
    upper_degree: int        # exclusive upper bound, 1..30


EGYPTIAN_BOUNDS: dict[ZodiacSign, list[Bound]] = {
    ZodiacSign.ARIES:       [Bound(Planet.JUPITER,  6), Bound(Planet.VENUS,   12), Bound(Planet.MERCURY, 20), Bound(Planet.MARS,    25), Bound(Planet.SATURN,  30)],
    ZodiacSign.TAURUS:      [Bound(Planet.VENUS,    8), Bound(Planet.MERCURY, 14), Bound(Planet.JUPITER, 22), Bound(Planet.SATURN,  27), Bound(Planet.MARS,    30)],
    ZodiacSign.GEMINI:      [Bound(Planet.MERCURY,  6), Bound(Planet.JUPITER, 12), Bound(Planet.VENUS,   17), Bound(Planet.MARS,    24), Bound(Planet.SATURN,  30)],
    ZodiacSign.CANCER:      [Bound(Planet.MARS,     7), Bound(Planet.VENUS,   13), Bound(Planet.MERCURY, 19), Bound(Planet.JUPITER, 26), Bound(Planet.SATURN,  30)],
    ZodiacSign.LEO:         [Bound(Planet.JUPITER,  6), Bound(Planet.VENUS,   11), Bound(Planet.SATURN,  18), Bound(Planet.MERCURY, 24), Bound(Planet.MARS,    30)],
    ZodiacSign.VIRGO:       [Bound(Planet.MERCURY,  7), Bound(Planet.VENUS,   17), Bound(Planet.JUPITER, 21), Bound(Planet.MARS,    28), Bound(Planet.SATURN,  30)],
    ZodiacSign.LIBRA:       [Bound(Planet.SATURN,   6), Bound(Planet.MERCURY, 14), Bound(Planet.JUPITER, 21), Bound(Planet.VENUS,   28), Bound(Planet.MARS,    30)],
    ZodiacSign.SCORPIO:     [Bound(Planet.MARS,     7), Bound(Planet.VENUS,   11), Bound(Planet.MERCURY, 19), Bound(Planet.JUPITER, 24), Bound(Planet.SATURN,  30)],
    ZodiacSign.SAGITTARIUS: [Bound(Planet.JUPITER, 12), Bound(Planet.VENUS,   17), Bound(Planet.MERCURY, 21), Bound(Planet.SATURN,  26), Bound(Planet.MARS,    30)],
    ZodiacSign.CAPRICORN:   [Bound(Planet.MERCURY,  7), Bound(Planet.JUPITER, 14), Bound(Planet.VENUS,   22), Bound(Planet.SATURN,  26), Bound(Planet.MARS,    30)],
    ZodiacSign.AQUARIUS:    [Bound(Planet.MERCURY,  7), Bound(Planet.VENUS,   13), Bound(Planet.JUPITER, 20), Bound(Planet.MARS,    25), Bound(Planet.SATURN,  30)],
    ZodiacSign.PISCES:      [Bound(Planet.VENUS,   12), Bound(Planet.JUPITER, 16), Bound(Planet.MERCURY, 19), Bound(Planet.MARS,    28), Bound(Planet.SATURN,  30)],
}


def bound_ruler(sign: ZodiacSign, degree: float) -> Planet:
    """Look up the bound ruler for an exact zodiacal position."""
    bounds = EGYPTIAN_BOUNDS[sign]
    for b in bounds:
        if degree < float(b.upper_degree):
            return b.ruler
    return bounds[-1].ruler


# Planetary joys (Brennan Ch. 10, p. 336-339, Fig 10.5)
PLANETARY_JOY: dict[Planet, HousePlace] = {
    Planet.MERCURY: HousePlace.FIRST,
    Planet.MOON:    HousePlace.THIRD,
    Planet.VENUS:   HousePlace.FIFTH,
    Planet.MARS:    HousePlace.SIXTH,
    Planet.SUN:     HousePlace.NINTH,
    Planet.JUPITER: HousePlace.ELEVENTH,
    Planet.SATURN:  HousePlace.TWELFTH,
}
