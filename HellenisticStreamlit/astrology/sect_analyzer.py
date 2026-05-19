"""Sect status of every chart factor (Brennan Ch. 7)."""
from __future__ import annotations
from dataclasses import dataclass

from models.house import HousePlace
from models.natal_chart import NatalChart
from models.planet import Planet
from models.sect import Sect
from models.zodiac import ZodiacSign


@dataclass(frozen=True)
class SectReport:
    sect: Sect
    sect_light: Planet
    benefic: Planet
    contrary_benefic: Planet
    malefic: Planet
    contrary_malefic: Planet
    sect_light_house: HousePlace
    sect_light_sign: ZodiacSign

    @property
    def sect_light_is_in_aversion(self) -> bool:
        return self.sect_light_house.is_in_aversion_to_ascendant


def analyze(chart: NatalChart) -> SectReport:
    s = chart.sect
    light = s.sect_light
    light_pos = chart.position(light)
    assert light_pos is not None
    return SectReport(
        sect=s,
        sect_light=light,
        benefic=s.benefic,
        contrary_benefic=s.contrary_benefic,
        malefic=s.malefic,
        contrary_malefic=s.contrary_malefic,
        sect_light_house=chart.house_place_for_sign(light_pos.sign),
        sect_light_sign=light_pos.sign,
    )
