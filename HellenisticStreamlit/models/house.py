"""Whole-sign houses — each of the 12 houses occupies exactly one sign,
beginning with the rising sign as the 1st house. Topics per Brennan Ch. 11-12.
"""
from __future__ import annotations
from dataclasses import dataclass
from enum import IntEnum


class Angularity(str):
    ANGULAR = "angular"
    SUCCEDENT = "succedent"
    CADENT = "cadent"


class HousePlace(IntEnum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    SIXTH = 6
    SEVENTH = 7
    EIGHTH = 8
    NINTH = 9
    TENTH = 10
    ELEVENTH = 11
    TWELFTH = 12

    @property
    def hellenistic_name(self) -> str:
        return {
            1: "Hour-Marker", 2: "Gate of Hades", 3: "Goddess",
            4: "Subterraneous", 5: "Good Fortune", 6: "Bad Fortune",
            7: "Setting", 8: "Idle", 9: "God",
            10: "Culmination", 11: "Good Spirit", 12: "Bad Spirit",
        }[int(self)]

    @property
    def topic(self) -> str:
        return {
            1:  "Self, body, temperament, life direction",
            2:  "Livelihood, resources, possessions",
            3:  "Siblings, short travel, communication",
            4:  "Home, parents, ancestry, foundations",
            5:  "Children, pleasure, creativity, eros",
            6:  "Illness, injury, subordinates, labor",
            7:  "Marriage, partnerships, open enemies",
            8:  "Death, inheritance, others' resources",
            9:  "Travel, philosophy, religion, study",
            10: "Career, public reputation, vocation",
            11: "Friends, alliances, hopes, fortune",
            12: "Hidden troubles, isolation, hostile forces",
        }[int(self)]

    @property
    def angularity(self) -> str:
        if int(self) in (1, 4, 7, 10):
            return Angularity.ANGULAR
        if int(self) in (2, 5, 8, 11):
            return Angularity.SUCCEDENT
        return Angularity.CADENT

    @property
    def is_in_aversion_to_ascendant(self) -> bool:
        # 2nd, 6th, 8th, 12th — places not configured to the 1st (Brennan p. 296).
        return int(self) in (2, 6, 8, 12)


@dataclass(frozen=True)
class House:
    place: HousePlace
    sign: "ZodiacSign"  # type: ignore[name-defined]  # noqa: F821
