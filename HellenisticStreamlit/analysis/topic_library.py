"""Source-grounded delineation library for major life topics.

Parallel in shape to LotLibrary. Ported from Swift `Analysis/TopicLibrary.swift`.
References: Brennan, Hellenistic Astrology, Chs. 11-12 and 14; George, AATP Vol II;
Avelar & Ribeiro, On the Heavenly Spheres, Ch. 5.
"""
from __future__ import annotations
from enum import Enum
from typing import Optional

from models.house import HousePlace


class LifeTopic(str, Enum):
    CAREER = "career"
    LOVE = "love"
    FINANCE = "finance"
    STYLE = "style"
    COURSE_OF_LIFE = "course_of_life"
    HEALTH = "health"

    @property
    def headline(self) -> str:
        return {
            LifeTopic.CAREER:         "Career & Vocation",
            LifeTopic.LOVE:           "Love & Partnership",
            LifeTopic.FINANCE:        "Finance & Resources",
            LifeTopic.STYLE:          "Style & Bearing",
            LifeTopic.COURSE_OF_LIFE: "Course of Life",
            LifeTopic.HEALTH:         "Health & Service",
        }[self]


def topic(t: LifeTopic) -> str:
    return {
        LifeTopic.CAREER:
            "**Career & Vocation** — the 10th place, the Culmination (HA Ch. 11). The place of action in the world: what the native becomes known for, the work that culminates above the horizon at noon. In plain terms — what one does, how one is publicly recognized, the shape of the life's outward work.",
        LifeTopic.LOVE:
            "**Love & Partnership** — the 7th place, the Setting (HA Ch. 11). The place of the other: the one who comes to meet the native — partner, spouse, beloved, and also the open adversary, since both arrive face-to-face. In plain terms — the kind of relating that suits the native, the partner they are drawn to, how love arrives.",
        LifeTopic.FINANCE:
            "**Finance & Resources** — the 2nd place, the Gate of Hades (HA Ch. 11). Livelihood, possessions, the things drawn on to sustain the self. In plain terms — money in and money out, what one owns, what supports materially. Read with the Lot of Fortune (HA Ch. 17), which marks where the chart quietly provides without effort.",
        LifeTopic.STYLE:
            "**Style & Bearing** — the 1st place, the Hour-Marker, the rising sign itself (HA Ch. 11). The place of the body, the soul's vehicle, the temperament others read at first sight. Style in this register is not what one puts on; it is what comes through.",
        LifeTopic.COURSE_OF_LIFE:
            "**Course of Life** — read from the sect light, the ruler of the Ascendant, and the Lot of Fortune (HA Chs. 7, 17). These three together are the chart's gravitational center: the luminary that leads the soul, the planet that carries the native through the life, and the seat of the given. The whole arc, not any single chapter.",
        LifeTopic.HEALTH:
            "**Health & Service** — the 6th place, Bad Fortune (HA Ch. 11). The place of illness, injury, accident, and of the work that wears the body — manual labor, subordination, what is done under others. Mars rejoices in the 6th (HA Ch. 10), which does not make the place pleasant — it means Mars knows how to operate from this position. Vitality is read primarily from the ruler of the Ascendant (AATP II).",
    }[t]


def life_example(t: LifeTopic, topical_house: HousePlace, ruler_house: HousePlace,
                 signif_house: Optional[HousePlace]) -> str:
    topical_topic = topical_house.topic.lower()
    ruler_topic = ruler_house.topic.lower()

    if t is LifeTopic.CAREER:
        if signif_house is None:
            return _concrete_career(topical_house, ruler_house)
        sun_topic = signif_house.topic.lower()
        if topical_house == ruler_house == signif_house:
            return (f"What this might look like in your life: the tenth place, its ruler, AND the Sun all converge in the same "
                    f"area of your life ({topical_topic}). That's an unusually concentrated career signature — the work, its "
                    f"channel, and the soul's drive all sit in one room. Expect the life's vocational center of gravity to be located here.")
        if topical_house == ruler_house:
            return (f"What this might look like in your life: the work itself and the channel through which it reaches you "
                    f"BOTH sit in {topical_topic} — these aren't two distinct arenas, they're one. The Sun in {sun_topic} adds "
                    f"a second register: that's where you feel your characteristic light wants to shine, regardless of the job "
                    f"title that carries the paycheck.")
        if ruler_house == signif_house:
            return (f"What this might look like in your life: the work is shaped by {topical_topic}, but it reaches you AND "
                    f"finds your inner fire through {ruler_topic}. When the ruler of your career and your Sun share a house, "
                    f"the channel is doubled — that life area is where vocation activates.")
        return (f"What this might look like in your life: the work itself takes the shape of {topical_topic}; it reaches you "
                f"through the affairs of {ruler_topic}; and the Sun — your characteristic light, what you're meant to shine as "
                f"— wants to come through in {sun_topic}. The career story is at the intersection of these three life areas.")

    if t is LifeTopic.LOVE:
        if signif_house is None:
            return _concrete_love(topical_house, ruler_house)
        venus_topic = signif_house.topic.lower()
        if topical_house == ruler_house == signif_house:
            return (f"What this might look like in your life: the seventh, its ruler, and Venus all converge in the same area "
                    f"of your life ({topical_topic}). Partnership is concentrated and visible in this one room — the people, "
                    f"the love itself, and the way it arrives all sit together.")
        if topical_house == ruler_house:
            return (f"What this might look like in your life: the partner you're drawn to AND the channel through which they "
                    f"reach you both sit in {topical_topic}. Venus, the heart of love, operates from {venus_topic} — adding a "
                    f"second life-area where attraction and grace come into play.")
        return (f"What this might look like in your life: you are drawn to a partner whose character is "
                f"{topical_house.topic.lower()}-shaped; they tend to reach you through the affairs of {ruler_topic}; and Venus, "
                f"the heart of attraction, weaves love through {venus_topic}. Your love life is the geometry of these three "
                f"areas overlapping.")

    if t is LifeTopic.FINANCE:
        if signif_house is None:
            return _concrete_finance(topical_house, ruler_house)
        jupiter_topic = signif_house.topic.lower()
        if topical_house == ruler_house:
            return (f"What this might look like in your life: livelihood AND the channel that feeds it both sit in {topical_topic} — "
                    f"these are the same room. Jupiter, the natural abundance-giver, expands wealth through {jupiter_topic} — "
                    f"that's where the chart says \"yes\" most generously when it comes to resources.")
        return (f"What this might look like in your life: money in your life takes the shape of {topical_topic}; it reaches you "
                f"through the affairs of {ruler_topic}; and Jupiter — the natural significator of abundance — opens doors through "
                f"{jupiter_topic}. The resourcing pattern is at the intersection.")

    if t is LifeTopic.STYLE:
        return (f"What this might look like in your life: your bearing is read in your body and the texture of {topical_topic}, "
                f"but the planet that carries you operates from {ruler_topic}. That means people receive you in two registers — "
                f"what shows on the surface (the rising sign) and what gets stamped on through the life-areas your chart-lord "
                f"inhabits. Your style is a conversation between them.")

    if t is LifeTopic.COURSE_OF_LIFE:
        if signif_house is None:
            return _concrete_course_of_life(topical_house, ruler_house)
        light_topic = signif_house.topic.lower()
        if ruler_house == signif_house:
            return (f"What this might look like in your life: your sect light AND the planet that carries you both sit in the "
                    f"same area ({light_topic}). That's a concentrating signature — the life's gravitational center is unusually "
                    f"clear. The years return, again and again, to this room.")
        return (f"What this might look like in your life: the soul's leading edge — your sect light — keeps drawing you back to "
                f"{light_topic}. The planet that carries you through the life operates through {ruler_topic}. Most major chapters "
                f"will play out as some combination of these two — the place you keep returning to, and the channel that runs the journey.")

    # HEALTH
    if signif_house is None:
        return _concrete_health(topical_house, ruler_house)
    affliction_topic = signif_house.topic.lower()
    if signif_house == topical_house:
        return (f"What this might look like in your life: the body's wear shows up in {topical_topic}, and the planet most able "
                f"to bring difficulty (the malefic contrary to your sect) is parked in the same room. Both strain and source-of-"
                f"strain live here — pay close attention to this area of life; it's where the body's signal is loudest.")
    if signif_house == ruler_house:
        return (f"What this might look like in your life: illness or strain shows up in {topical_topic}, and the malefic contrary "
                f"to your sect sits exactly where the channel of health runs — {ruler_topic}. That's a coincidence worth noting: "
                f"the planet that pressures the body, and the planet that carries your sixth-house affairs, share a stage.")
    return (f"What this might look like in your life: the body's strain points are in {topical_topic}; the channel through "
            f"which they manifest is {ruler_topic}; and the planet most likely to apply pressure (the malefic contrary to your "
            f"sect) operates from {affliction_topic}. Health is the conversation between these three areas — watch all of them "
            f"for the body's signal.")


def _concrete_career(topical_house: HousePlace, ruler_house: HousePlace) -> str:
    if topical_house == ruler_house:
        return (f"What this might look like in your life: the work and the channel that carries it both sit in "
                f"{topical_house.topic.lower()} — this single area is where the career story is most likely to play out.")
    return (f"What this might look like in your life: the work itself takes the shape of {topical_house.topic.lower()}; "
            f"it reaches you through the affairs of {ruler_house.topic.lower()}.")


def _concrete_love(topical_house: HousePlace, ruler_house: HousePlace) -> str:
    if topical_house == ruler_house:
        return (f"What this might look like in your life: the partner you're drawn to and the channel through which love "
                f"reaches you both sit in {topical_house.topic.lower()}.")
    return (f"What this might look like in your life: the partner takes their character from {topical_house.topic.lower()}; "
            f"love reaches you through the affairs of {ruler_house.topic.lower()}.")


def _concrete_finance(topical_house: HousePlace, ruler_house: HousePlace) -> str:
    if topical_house == ruler_house:
        return (f"What this might look like in your life: resources and the channel that delivers them both sit in "
                f"{topical_house.topic.lower()}.")
    return (f"What this might look like in your life: money in your life takes the shape of {topical_house.topic.lower()}; "
            f"it reaches you through the affairs of {ruler_house.topic.lower()}.")


def _concrete_course_of_life(topical_house: HousePlace, ruler_house: HousePlace) -> str:
    return f"What this might look like in your life: the journey runs through {ruler_house.topic.lower()}."


def _concrete_health(topical_house: HousePlace, ruler_house: HousePlace) -> str:
    if topical_house == ruler_house:
        return (f"What this might look like in your life: the body's strain points and the channel through which they show up "
                f"both sit in {topical_house.topic.lower()} — that single area carries the chart's whole sixth-house weight.")
    return (f"What this might look like in your life: the body's strain points are in {topical_house.topic.lower()}; they tend "
            f"to manifest through the affairs of {ruler_house.topic.lower()}.")
