"""NatalChart — the output of ChartCalculator and the input to every analyzer."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from .aspect import Aspect
from .birth_data import BirthData
from .house import House, HousePlace
from .lot import HermeticLot, HermeticLotPosition
from .planet import Planet, PlanetaryPosition
from .sect import Sect
from .zodiac import ZodiacSign


@dataclass(frozen=True)
class NatalChart:
    birth_data: BirthData
    ascendant_longitude: float
    midheaven_longitude: float
    positions: tuple[PlanetaryPosition, ...]
    sect: Sect
    lots: tuple[HermeticLotPosition, ...]

    @property
    def ascendant_sign(self) -> ZodiacSign:
        return ZodiacSign(int(self.ascendant_longitude / 30.0) % 12)

    @property
    def midheaven_sign(self) -> ZodiacSign:
        return ZodiacSign(int(self.midheaven_longitude / 30.0) % 12)

    def lot(self, kind: HermeticLot) -> HermeticLotPosition:
        for l in self.lots:
            if l.kind is kind:
                return l
        raise KeyError(kind)

    def house_place_for_sign(self, sign: ZodiacSign) -> HousePlace:
        offset = (int(sign) - int(self.ascendant_sign)) % 12
        return HousePlace(offset + 1)

    def house_place_for_planet(self, planet: Planet) -> Optional[HousePlace]:
        pos = self.position(planet)
        if pos is None:
            return None
        return self.house_place_for_sign(pos.sign)

    @property
    def houses(self) -> tuple[House, ...]:
        return tuple(
            House(place=HousePlace(i + 1),
                  sign=self.ascendant_sign.advanced(i))
            for i in range(12)
        )

    def position(self, planet: Planet) -> Optional[PlanetaryPosition]:
        for p in self.positions:
            if p.planet is planet:
                return p
        return None

    def planets_in_sign(self, sign: ZodiacSign) -> list[PlanetaryPosition]:
        return [p for p in self.positions if p.sign == sign]

    def planets_in_place(self, place: HousePlace) -> list[PlanetaryPosition]:
        return [p for p in self.positions if self.house_place_for_sign(p.sign) == place]
