"""Zodiac signs — 12 tropical signs, 0=Aries..11=Pisces.

Ported from Swift `Models/ZodiacSign.swift`. Integer-backed enum so arithmetic
on sign indices behaves naturally (whole-sign house offsets, aspect detection).
"""
from __future__ import annotations
from enum import IntEnum


class Element(str):
    FIRE = "fire"
    EARTH = "earth"
    AIR = "air"
    WATER = "water"


class Modality(str):
    CARDINAL = "cardinal"
    FIXED = "fixed"
    MUTABLE = "mutable"


class Polarity(str):
    DIURNAL = "diurnal"
    NOCTURNAL = "nocturnal"


class ZodiacSign(IntEnum):
    ARIES = 0
    TAURUS = 1
    GEMINI = 2
    CANCER = 3
    LEO = 4
    VIRGO = 5
    LIBRA = 6
    SCORPIO = 7
    SAGITTARIUS = 8
    CAPRICORN = 9
    AQUARIUS = 10
    PISCES = 11

    @property
    def display_name(self) -> str:
        return {
            ZodiacSign.ARIES: "Aries", ZodiacSign.TAURUS: "Taurus",
            ZodiacSign.GEMINI: "Gemini", ZodiacSign.CANCER: "Cancer",
            ZodiacSign.LEO: "Leo", ZodiacSign.VIRGO: "Virgo",
            ZodiacSign.LIBRA: "Libra", ZodiacSign.SCORPIO: "Scorpio",
            ZodiacSign.SAGITTARIUS: "Sagittarius", ZodiacSign.CAPRICORN: "Capricorn",
            ZodiacSign.AQUARIUS: "Aquarius", ZodiacSign.PISCES: "Pisces",
        }[self]

    @property
    def glyph(self) -> str:
        glyphs = "♈♉♊♋♌♍♎♏♐♑♒♓"
        return glyphs[int(self)]

    @property
    def element(self) -> str:
        groups = {
            Element.FIRE:  (ZodiacSign.ARIES, ZodiacSign.LEO, ZodiacSign.SAGITTARIUS),
            Element.EARTH: (ZodiacSign.TAURUS, ZodiacSign.VIRGO, ZodiacSign.CAPRICORN),
            Element.AIR:   (ZodiacSign.GEMINI, ZodiacSign.LIBRA, ZodiacSign.AQUARIUS),
            Element.WATER: (ZodiacSign.CANCER, ZodiacSign.SCORPIO, ZodiacSign.PISCES),
        }
        for el, signs in groups.items():
            if self in signs:
                return el
        raise RuntimeError("unreachable")

    @property
    def modality(self) -> str:
        groups = {
            Modality.CARDINAL: (ZodiacSign.ARIES, ZodiacSign.CANCER, ZodiacSign.LIBRA, ZodiacSign.CAPRICORN),
            Modality.FIXED:    (ZodiacSign.TAURUS, ZodiacSign.LEO, ZodiacSign.SCORPIO, ZodiacSign.AQUARIUS),
            Modality.MUTABLE:  (ZodiacSign.GEMINI, ZodiacSign.VIRGO, ZodiacSign.SAGITTARIUS, ZodiacSign.PISCES),
        }
        for m, signs in groups.items():
            if self in signs:
                return m
        raise RuntimeError("unreachable")

    @property
    def polarity(self) -> str:
        # Fire/Air = diurnal, Earth/Water = nocturnal (Brennan Ch. 4).
        return Polarity.DIURNAL if self.element in (Element.FIRE, Element.AIR) else Polarity.NOCTURNAL

    def advanced(self, count: int) -> "ZodiacSign":
        return ZodiacSign((int(self) + count) % 12)

    def sign_distance(self, other: "ZodiacSign") -> int:
        """Inclusive zodiacal distance — same sign = 1, next sign = 2, ..."""
        diff = (int(other) - int(self)) % 12
        return diff + 1
