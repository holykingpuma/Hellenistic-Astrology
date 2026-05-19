"""Per-topic advice using TopicLibrary's life_example treatment.

Mirrors the iOS Topical Advice screen. For each of the six topics (career,
love, finance, style, course of life, health) we build a paragraph with:
1. The topic intro (Hellenistic framing + plain-language gloss)
2. Chart-specific factors (topical house + its ruler's placement + natural
   significator's placement)
3. A "what this might look like in your life" sentence

References: Brennan Ch. 11-12 (houses), Ch. 14 (synthesis); George AATP II.
"""
from __future__ import annotations
from dataclasses import dataclass

from astrology.hellenistic_tables import DOMICILE_RULER
from astrology.sect_analyzer import analyze as analyze_sect
from models.house import HousePlace
from models.natal_chart import NatalChart
from models.planet import Planet

from . import delineation_library as dl
from .topic_library import LifeTopic, life_example, topic as topic_intro


# Topical house for each life topic (whole-sign place).
TOPICAL_HOUSE: dict[LifeTopic, HousePlace] = {
    LifeTopic.CAREER:         HousePlace.TENTH,
    LifeTopic.LOVE:           HousePlace.SEVENTH,
    LifeTopic.FINANCE:        HousePlace.SECOND,
    LifeTopic.STYLE:          HousePlace.FIRST,
    LifeTopic.COURSE_OF_LIFE: HousePlace.FIRST,   # the rising sign + chart ruler + sect light
    LifeTopic.HEALTH:         HousePlace.SIXTH,
}


# Natural significator (universal significator) for each topic.
SIGNIFICATOR: dict[LifeTopic, Planet | None] = {
    LifeTopic.CAREER:         Planet.SUN,
    LifeTopic.LOVE:           Planet.VENUS,
    LifeTopic.FINANCE:        Planet.JUPITER,
    LifeTopic.STYLE:          None,   # ruler of Asc IS the significator
    LifeTopic.COURSE_OF_LIFE: None,   # sect light passed separately
    LifeTopic.HEALTH:         None,   # we pass the malefic contrary to sect's house
}


@dataclass(frozen=True)
class TopicalAdvice:
    topic: LifeTopic
    topical_house: HousePlace
    ruler: Planet
    ruler_house: HousePlace
    paragraph: str


def analyze(chart: NatalChart, t: LifeTopic) -> TopicalAdvice:
    topical_house = TOPICAL_HOUSE[t]
    topical_sign = chart.ascendant_sign.advanced(int(topical_house) - 1)
    ruler = DOMICILE_RULER[topical_sign]
    ruler_pos = chart.position(ruler)
    assert ruler_pos is not None
    ruler_house = chart.house_place_for_sign(ruler_pos.sign)

    # Decide the "significator house" parameter for life_example.
    if t is LifeTopic.COURSE_OF_LIFE:
        sect_report = analyze_sect(chart)
        signif_house = sect_report.sect_light_house
    elif t is LifeTopic.HEALTH:
        sect_report = analyze_sect(chart)
        mal_pos = chart.position(sect_report.malefic)
        signif_house = chart.house_place_for_sign(mal_pos.sign) if mal_pos else None
    else:
        signif_planet = SIGNIFICATOR.get(t)
        if signif_planet is None:
            signif_house = None
        else:
            sp = chart.position(signif_planet)
            signif_house = chart.house_place_for_sign(sp.sign) if sp else None

    intro = topic_intro(t)

    # Chart-specific factors paragraph.
    chart_factors = (
        f"In your chart, this topic centers on your {dl.ordinal(topical_house.value)} house "
        f"({topical_house.hellenistic_name}), which falls in **{topical_sign.display_name}**. "
        f"The planet that rules {topical_sign.display_name} is **{ruler.display_name}**, "
        f"and {ruler.display_name} sits in your {dl.ordinal(ruler_house.value)} house "
        f"({ruler_house.topic.lower()}). In Hellenistic technique, that ruling planet 'carries' the topic — "
        f"its placement and condition shape how the topic actually reaches you (HA Ch. 14)."
    )

    example = life_example(t, topical_house, ruler_house, signif_house)
    paragraph = "\n\n".join([intro, chart_factors, example])
    return TopicalAdvice(
        topic=t,
        topical_house=topical_house,
        ruler=ruler,
        ruler_house=ruler_house,
        paragraph=paragraph,
    )


def analyze_all(chart: NatalChart) -> list[TopicalAdvice]:
    return [analyze(chart, t) for t in LifeTopic]
