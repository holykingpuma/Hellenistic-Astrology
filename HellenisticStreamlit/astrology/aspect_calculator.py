"""Whole-sign Ptolemaic aspects (Brennan p. 300-303, Fig 9.3).

Two planets are configured if their signs stand in one of the five Ptolemaic
sign-relations. Degree separation refines the configuration — within 3° is
"partile" and emits a stronger ray. Signs in aversion (2nd, 6th, 8th, 12th
from one another) do not configure at all.
"""
from __future__ import annotations

from models.aspect import Aspect, AspectKind
from models.natal_chart import NatalChart
from models.planet import PlanetaryPosition
from models.zodiac import ZodiacSign


PARTILE_ORB = 3.0


def _sign_distance(a: ZodiacSign, b: ZodiacSign) -> int:
    """Smallest sign-distance between two signs, 0..6."""
    raw = abs(int(a) - int(b)) % 12
    return min(raw, 12 - raw)


def aspect_between(first: PlanetaryPosition, second: PlanetaryPosition) -> Aspect | None:
    delta = _sign_distance(first.sign, second.sign)
    kind = next((k for k in AspectKind if k.sign_separation == delta), None)
    if kind is None:
        return None

    diff = abs(first.longitude - second.longitude)
    if diff > 180:
        diff = 360 - diff
    orb = abs(diff - kind.exact_degrees)
    return Aspect(
        first=first.planet,
        second=second.planet,
        kind=kind,
        orb=orb,
        is_partile=orb <= PARTILE_ORB,
    )


def aspects_in(chart: NatalChart) -> list[Aspect]:
    out: list[Aspect] = []
    planets = chart.positions
    for i in range(len(planets)):
        for j in range(i + 1, len(planets)):
            a = aspect_between(planets[i], planets[j])
            if a is not None:
                out.append(a)
    return out
