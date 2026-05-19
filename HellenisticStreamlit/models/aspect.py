"""The five Ptolemaic aspects (Brennan Ch. 9).

Determined first by sign relationship (whole-sign configuration), then refined
by degree closeness — within ~3° is "partile" and emits a stronger ray.
"""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from .planet import Planet


class Harmony(str, Enum):
    SOFT = "soft"
    HARD = "hard"
    NEUTRAL = "neutral"


class AspectKind(str, Enum):
    CONJUNCTION = "conjunction"
    SEXTILE = "sextile"
    SQUARE = "square"
    TRINE = "trine"
    OPPOSITION = "opposition"

    @property
    def glyph(self) -> str:
        return {
            AspectKind.CONJUNCTION: "☌",
            AspectKind.SEXTILE:     "⚹",
            AspectKind.SQUARE:      "□",
            AspectKind.TRINE:       "△",
            AspectKind.OPPOSITION:  "☍",
        }[self]

    @property
    def sign_separation(self) -> int:
        return {
            AspectKind.CONJUNCTION: 0,
            AspectKind.SEXTILE:     2,
            AspectKind.SQUARE:      3,
            AspectKind.TRINE:       4,
            AspectKind.OPPOSITION:  6,
        }[self]

    @property
    def exact_degrees(self) -> float:
        return self.sign_separation * 30.0

    @property
    def harmony(self) -> Harmony:
        if self in (AspectKind.TRINE, AspectKind.SEXTILE):
            return Harmony.SOFT
        if self in (AspectKind.SQUARE, AspectKind.OPPOSITION):
            return Harmony.HARD
        return Harmony.NEUTRAL


@dataclass(frozen=True)
class Aspect:
    first: Planet
    second: Planet
    kind: AspectKind
    orb: float           # absolute degree separation between the two planets (0..180)
    is_partile: bool     # True when orb ≤ 3° from exact

    @property
    def id(self) -> str:
        return f"{self.first.value}-{self.kind.value}-{self.second.value}"
