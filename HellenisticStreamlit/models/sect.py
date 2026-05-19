"""Sect — the master variable of Hellenistic delineation (Brennan Ch. 7).

Day chart vs. night chart, and the planetary teams that follow from it.
"""
from __future__ import annotations
from enum import Enum
from .planet import Planet


class Sect(str, Enum):
    DIURNAL = "diurnal"
    NOCTURNAL = "nocturnal"

    @property
    def sect_light(self) -> Planet:
        return Planet.SUN if self is Sect.DIURNAL else Planet.MOON

    @property
    def contrary_luminary(self) -> Planet:
        return Planet.MOON if self is Sect.DIURNAL else Planet.SUN

    @property
    def benefic(self) -> Planet:
        """Benefic of sect — the more helpful benefic (Brennan p. 199)."""
        return Planet.JUPITER if self is Sect.DIURNAL else Planet.VENUS

    @property
    def contrary_benefic(self) -> Planet:
        return Planet.VENUS if self is Sect.DIURNAL else Planet.JUPITER

    @property
    def malefic(self) -> Planet:
        """Malefic contrary to sect — the more destructive malefic (Brennan p. 200)."""
        return Planet.MARS if self is Sect.DIURNAL else Planet.SATURN

    @property
    def contrary_malefic(self) -> Planet:
        return Planet.SATURN if self is Sect.DIURNAL else Planet.MARS

    def is_planet_of_sect(self, planet: Planet) -> bool:
        """Diurnal team: Sun, Jupiter, Saturn. Nocturnal team: Moon, Venus, Mars.
        Mercury is variable (oriental/occidental — handled separately).
        """
        if self is Sect.DIURNAL:
            return planet in (Planet.SUN, Planet.JUPITER, Planet.SATURN)
        return planet in (Planet.MOON, Planet.VENUS, Planet.MARS)
