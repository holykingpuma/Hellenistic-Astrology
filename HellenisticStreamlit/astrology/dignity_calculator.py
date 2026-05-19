"""Five-fold essential dignity scoring per Brennan Ch. 8."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from models.natal_chart import NatalChart
from models.planet import Planet, PlanetaryPosition
from models.sect import Sect
from models.zodiac import ZodiacSign

from . import hellenistic_tables as ht


@dataclass(frozen=True)
class DignityReport:
    planet: Planet
    sign: ZodiacSign
    sign_degree: float

    is_in_domicile: bool
    is_in_detriment: bool      # opposite of domicile
    is_in_exaltation: bool
    is_in_fall: bool
    is_triplicity_ruler: bool
    triplicity_role: Optional[str]   # "day" / "night" / "cooperating"
    bound_ruler: Planet
    is_in_own_bound: bool
    rejoices_in_house: bool

    @property
    def score(self) -> int:
        s = 0
        if self.is_in_domicile:      s += 5
        if self.is_in_exaltation:    s += 4
        if self.is_triplicity_ruler: s += 3
        if self.is_in_own_bound:     s += 2
        if self.rejoices_in_house:   s += 1
        if self.is_in_detriment:     s -= 5
        if self.is_in_fall:          s -= 4
        return s


def evaluate(position: PlanetaryPosition, sect: Sect, chart: NatalChart) -> DignityReport:
    sign = position.sign
    degree = position.sign_degree
    planet = position.planet

    domicile_ruler = ht.DOMICILE_RULER[sign]
    is_domicile = domicile_ruler is planet
    # Detriment: the sign opposite a planet's domicile.
    is_detriment = ht.DOMICILE_RULER[sign.advanced(6)] is planet

    is_exaltation = False
    is_fall = False
    if planet in ht.EXALTATION:
        ex = ht.EXALTATION[planet]
        is_exaltation = (ex.sign == sign)
        is_fall = (ex.fall_sign == sign)

    role: Optional[str] = None
    is_trip = False
    trip = ht.TRIPLICITY.get(sign.element)
    if trip is not None:
        if sect is Sect.DIURNAL:
            if   trip.day is planet:         is_trip, role = True, "day"
            elif trip.night is planet:       is_trip, role = True, "night"
            elif trip.cooperating is planet: is_trip, role = True, "cooperating"
        else:
            if   trip.night is planet:       is_trip, role = True, "night"
            elif trip.day is planet:         is_trip, role = True, "day"
            elif trip.cooperating is planet: is_trip, role = True, "cooperating"

    bound_ruler = ht.bound_ruler(sign, degree)
    is_own_bound = bound_ruler is planet

    house = chart.house_place_for_sign(sign)
    rejoices = ht.PLANETARY_JOY.get(planet) == house

    return DignityReport(
        planet=planet,
        sign=sign,
        sign_degree=degree,
        is_in_domicile=is_domicile,
        is_in_detriment=is_detriment,
        is_in_exaltation=is_exaltation,
        is_in_fall=is_fall,
        is_triplicity_ruler=is_trip,
        triplicity_role=role,
        bound_ruler=bound_ruler,
        is_in_own_bound=is_own_bound,
        rejoices_in_house=rejoices,
    )


def evaluate_all(chart: NatalChart) -> list[DignityReport]:
    return [evaluate(p, chart.sect, chart) for p in chart.positions]
