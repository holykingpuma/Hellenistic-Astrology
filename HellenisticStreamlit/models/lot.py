"""The seven Hermetic Lots (Brennan Ch. 17).

Each Lot is a derived sensitive point computed from arithmetic between the
Ascendant and other chart factors. Formulas live in `astrology/chart_calculator.py`;
this file just defines the enum and position dataclass.
"""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from .planet import Planet


class HermeticLot(str, Enum):
    FORTUNE = "fortune"
    SPIRIT = "spirit"
    EROS = "eros"
    NECESSITY = "necessity"
    COURAGE = "courage"
    VICTORY = "victory"
    NEMESIS = "nemesis"

    @property
    def display_name(self) -> str:
        return {
            HermeticLot.FORTUNE:   "Lot of Fortune",
            HermeticLot.SPIRIT:    "Lot of Spirit",
            HermeticLot.EROS:      "Lot of Eros",
            HermeticLot.NECESSITY: "Lot of Necessity",
            HermeticLot.COURAGE:   "Lot of Courage",
            HermeticLot.VICTORY:   "Lot of Victory",
            HermeticLot.NEMESIS:   "Lot of Nemesis",
        }[self]

    @property
    def signifying_planet(self) -> Planet:
        """The traditional planet whose Hermetic Lot this is."""
        return {
            HermeticLot.FORTUNE:   Planet.MOON,
            HermeticLot.SPIRIT:    Planet.SUN,
            HermeticLot.EROS:      Planet.VENUS,
            HermeticLot.NECESSITY: Planet.MERCURY,
            HermeticLot.COURAGE:   Planet.MARS,
            HermeticLot.VICTORY:   Planet.JUPITER,
            HermeticLot.NEMESIS:   Planet.SATURN,
        }[self]


ALL_LOTS: tuple[HermeticLot, ...] = (
    HermeticLot.FORTUNE, HermeticLot.SPIRIT, HermeticLot.EROS,
    HermeticLot.NECESSITY, HermeticLot.COURAGE, HermeticLot.VICTORY,
    HermeticLot.NEMESIS,
)


def _normalize(deg: float) -> float:
    mod = deg % 360.0
    return mod + 360.0 if mod < 0 else mod


@dataclass(frozen=True)
class HermeticLotPosition:
    kind: HermeticLot
    longitude: float

    def __post_init__(self):
        object.__setattr__(self, "longitude", _normalize(self.longitude))

    @property
    def sign(self):
        from .zodiac import ZodiacSign
        return ZodiacSign(int(self.longitude / 30.0) % 12)

    @property
    def sign_degree(self) -> float:
        return self.longitude % 30.0
