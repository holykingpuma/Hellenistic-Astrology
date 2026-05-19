"""Source-grounded delineation library for the 7 Hermetic Lots.

Ported from Swift `Analysis/LotLibrary.swift`. References: Brennan, Hellenistic
Astrology, Ch. 17; George, AATP Vol. I — Lots chapter.
"""
from __future__ import annotations

from models.house import HousePlace
from models.lot import HermeticLot, HermeticLotPosition
from models.planet import Planet


def topic(lot: HermeticLot) -> str:
    return {
        HermeticLot.FORTUNE:
            "**The Lot of Fortune (Tyche, the Moon's lot)** — bodily life and material circumstance: the things that happen TO the native, the unearned good and ill, physical wellbeing, the contingent flow of luck. The given life, what arrives without effort (HA Ch. 17).",
        HermeticLot.SPIRIT:
            "**The Lot of Spirit (Daimon, the Sun's lot)** — the chosen life: what the native ACTS on, career, intellectual and willed direction. The willed life, what is achieved through one's own effort (HA Ch. 17). Fortune and Spirit are the two foundational lots — together they map the given and the chosen halves of a life.",
        HermeticLot.EROS:
            "**The Lot of Eros (Venus's lot)** — desire, romantic love, friendship, and the appetites that draw the native toward what they love (HA Ch. 17; AATP I).",
        HermeticLot.NECESSITY:
            "**The Lot of Necessity (Ananke, Mercury's lot)** — the constraints and circumstances that cannot be moved: what is fated, what limits, sometimes what enemies the native faces (HA Ch. 17; AATP I).",
        HermeticLot.COURAGE:
            "**The Lot of Courage (Tolma, Mars's lot)** — boldness, audacity, the readiness to fight, and the actions taken under pressure or in conflict (HA Ch. 17; AATP I).",
        HermeticLot.VICTORY:
            "**The Lot of Victory (Nike, Jupiter's lot)** — success, triumph, faith, and the topics in which the native is most likely to prevail or be rewarded (HA Ch. 17; AATP I).",
        HermeticLot.NEMESIS:
            "**The Lot of Nemesis (Saturn's lot)** — hidden adversaries, retribution, downfall, and the parts of life where things can quietly turn against the native (HA Ch. 17; AATP I).",
    }[lot]


def _ordinal_suffix(n: int) -> str:
    if n == 1: return "st"
    if n == 2: return "nd"
    if n == 3: return "rd"
    return "th"


def table_row(lot: HermeticLot,
              lot_position: HermeticLotPosition,
              lot_house: HousePlace,
              lot_lord: Planet,
              lord_house: HousePlace,
              lord_to_lot_aspect: str) -> str:
    """**Lot | Position | House | Lord | Lord's House | Lord→Lot Aspect.** Markdown."""
    deg = int(lot_position.sign_degree)
    minutes = int((lot_position.sign_degree - deg) * 60.0)
    position = f"{lot_position.sign.display_name} {deg}°{minutes:02d}'"
    return (
        f"**{lot.display_name}** — {position} · "
        f"{lot_house.value}{_ordinal_suffix(lot_house.value)} house · "
        f"lord: {lot_lord.display_name} ({lord_house.value}{_ordinal_suffix(lord_house.value)}) · "
        f"lord→lot: {lord_to_lot_aspect}"
    )


def life_example(lot: HermeticLot, lot_house: HousePlace, ruler_house: HousePlace) -> str:
    """Concrete 'what this might look like in your life' sentence."""
    lot_topic = lot_house.topic.lower()
    ruler_topic = ruler_house.topic.lower()

    if lot_house == ruler_house:
        return (
            f"What this might look like in your life: the lot AND the planet that carries it both sit in the same area of your life ({lot_topic}). "
            f"That doubles the significance — your {lot.display_name.lower()} plays out here directly, without an intermediate channel."
        )

    examples = {
        HermeticLot.FORTUNE:
            f"What this might look like in your life: opportunities, helpful resources, and quiet good arrive through {lot_topic}. "
            f"The channel that activates them is {ruler_topic}. "
            f"The pattern — when you engage with these areas of your life, fortune tends to find you.",
        HermeticLot.SPIRIT:
            f"What this might look like in your life: the work of your soul — what you actively choose to DO with your life — plays out in {lot_topic}. "
            f"The channel through which you act is {ruler_topic}. "
            f"In practice, your most meaningful achievements come through this combination.",
        HermeticLot.EROS:
            f"What this might look like in your life: what you love and what draws you is rooted in {lot_topic}. "
            f"The channel through which love arrives is {ruler_topic}. "
            f"In practice, the people and things you love most are tied to these life areas, and they reach you through what happens there.",
        HermeticLot.NECESSITY:
            f"What this might look like in your life: the unmovable parts of your life — the constraints and circumstances you cannot easily change — show up in {lot_topic}. "
            f"The channel they come through is {ruler_topic}. "
            f"These tend to be the places where you feel most bound.",
        HermeticLot.COURAGE:
            f"What this might look like in your life: the territory where you are most willing to fight, take risks, or push through resistance is {lot_topic}. "
            f"The channel for your boldness is {ruler_topic}. "
            f"In practice, your most courageous moments tend to play out at the intersection of these life areas.",
        HermeticLot.VICTORY:
            f"What this might look like in your life: success and triumph arrive through {lot_topic}. "
            f"The channel that brings them is {ruler_topic}. "
            f"In practice, your wins come from engaging with these areas — they're where the chart is most likely to reward you.",
        HermeticLot.NEMESIS:
            f"What this might look like in your life: hidden adversaries, retribution, or quiet undoing tend to arise in {lot_topic}. "
            f"The channel they come through is {ruler_topic}. "
            f"In practice, these are the life areas where you most need to stay alert to what runs against you.",
    }
    return examples[lot]
