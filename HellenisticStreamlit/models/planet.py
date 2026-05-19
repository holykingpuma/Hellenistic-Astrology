"""Planet model — the seven traditional planets of Hellenistic astrology.

Ported from Swift `Models/Planet.swift`. Same shape, same conventions:
benefic/malefic/neutral/luminary nature, retrograde flag on positions.
"""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


class Planet(str, Enum):
    SUN = "sun"
    MOON = "moon"
    MERCURY = "mercury"
    VENUS = "venus"
    MARS = "mars"
    JUPITER = "jupiter"
    SATURN = "saturn"

    @property
    def display_name(self) -> str:
        return self.value.capitalize()

    @property
    def glyph(self) -> str:
        return {
            Planet.SUN: "☉",
            Planet.MOON: "☽",
            Planet.MERCURY: "☿",
            Planet.VENUS: "♀",
            Planet.MARS: "♂",
            Planet.JUPITER: "♃",
            Planet.SATURN: "♄",
        }[self]

    @property
    def is_luminary(self) -> bool:
        return self in (Planet.SUN, Planet.MOON)


class Nature(str, Enum):
    BENEFIC = "benefic"   # Venus, Jupiter
    MALEFIC = "malefic"   # Mars, Saturn
    NEUTRAL = "neutral"   # Mercury
    LUMINARY = "luminary" # Sun, Moon


def planet_nature(p: Planet) -> Nature:
    return {
        Planet.SUN: Nature.LUMINARY,
        Planet.MOON: Nature.LUMINARY,
        Planet.MERCURY: Nature.NEUTRAL,
        Planet.VENUS: Nature.BENEFIC,
        Planet.JUPITER: Nature.BENEFIC,
        Planet.MARS: Nature.MALEFIC,
        Planet.SATURN: Nature.MALEFIC,
    }[p]


def _normalize(deg: float) -> float:
    mod = deg % 360.0
    return mod + 360.0 if mod < 0 else mod


@dataclass(frozen=True)
class PlanetaryPosition:
    """A planet's position in the natal chart at a moment in time.

    longitude is tropical ecliptic longitude in degrees (0..<360).
    """
    planet: Planet
    longitude: float
    is_retrograde: bool

    def __post_init__(self):
        # Frozen dataclass — bypass __setattr__ for normalization.
        object.__setattr__(self, "longitude", _normalize(self.longitude))

    @property
    def sign(self):
        from .zodiac import ZodiacSign
        return ZodiacSign(int(self.longitude / 30.0) % 12)

    @property
    def sign_degree(self) -> float:
        return self.longitude % 30.0

    @property
    def formatted_position(self) -> str:
        deg = int(self.sign_degree)
        minutes = int((self.sign_degree - deg) * 60.0)
        return f"{deg}° {self.sign.glyph} {minutes:02d}'"


# Canonical iteration order used throughout the analyzer (matches Swift Planet.allCases).
ALL_PLANETS: tuple[Planet, ...] = (
    Planet.SUN, Planet.MOON, Planet.MERCURY, Planet.VENUS,
    Planet.MARS, Planet.JUPITER, Planet.SATURN,
)
