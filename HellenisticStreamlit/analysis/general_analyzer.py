"""Composes the rich general analysis the user sees.

For each of the 7 planets we produce a multi-sentence paragraph layering:
  1. Sign placement       (PlanetInSignLibrary)
  2. House placement      (PlanetInHouseLibrary)
  3. House-structural     (DelineationLibrary.house_structural_note)
  4. Essential dignity    (DelineationLibrary.dignity_narrative)
  5. Sect status          (sect_status_line)

Plus an aspect-by-aspect narrative, lot table + readings, and condensed
strength/difficulty highlights.

References: Brennan Ch. 14 ("Putting It All Together"); George AATP II.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from astrology import aspect_calculator, dignity_calculator, sect_analyzer
from astrology.dignity_calculator import DignityReport
from astrology.hellenistic_tables import DOMICILE_RULER, PLANETARY_JOY
from astrology.sect_analyzer import SectReport
from models.aspect import Aspect, AspectKind, Harmony
from models.house import HousePlace
from models.lot import ALL_LOTS, HermeticLot
from models.natal_chart import NatalChart
from models.planet import ALL_PLANETS, Planet
from models.sect import Sect
from models.zodiac import ZodiacSign

from . import aspect_pair_library, delineation_library as dl
from . import lot_library, planet_in_house_library, planet_in_sign_library


@dataclass(frozen=True)
class PlanetReading:
    planet: Planet
    sign: ZodiacSign
    house: HousePlace
    paragraph: str
    dignity_score: int


@dataclass(frozen=True)
class AspectReading:
    aspect: Aspect
    paragraph: str


@dataclass(frozen=True)
class LotReading:
    lot: HermeticLot
    sign: ZodiacSign
    house: HousePlace
    paragraph: str


@dataclass(frozen=True)
class GeneralAnalysis:
    glossary: str
    summary: str
    structural_narrative: str
    planet_readings: list[PlanetReading]
    aspect_readings: list[AspectReading]
    lot_table: list[str]
    lot_readings: list[LotReading]
    positive_highlights: list[str]
    negative_highlights: list[str]
    sect_report: SectReport
    dignity_reports: list[DignityReport]


READING_GUIDE = """A quick guide to the language used below — this is a Hellenistic-tradition chart, which uses some terms unfamiliar to most modern readers:

• Places / houses — the 12 sectors of the chart, each signifying a different area of life. "1st place" and "1st house" mean the same thing. Numbered counterclockwise from your rising sign.

• Ascendant (Asc) — the degree rising on the eastern horizon at your moment of birth. The sign holding it becomes your 1st place / 1st house. The ruler of this sign is sometimes called "the lord of the chart" because it carries you through the life.

• Sect — whether you were born during the day (Sun above the horizon) or night (Sun below). Hellenistic astrology weighs this heavily: it decides which benefic (Venus or Jupiter) helps you most, and which malefic (Mars or Saturn) challenges you most.

• Aversion — a sign that doesn't form a Ptolemaic aspect (sextile, square, trine, or opposition) to your rising sign. Planets in those signs (your 2nd, 6th, 8th, and 12th houses) can't "see" the Ascendant, so their themes work at a remove from your direct will — through hidden, oblique, or external channels.

• Dignity — how strongly a planet operates from a particular sign. Five kinds: domicile (the sign it rules), exaltation (a sign of honor), triplicity (the element it co-rules), bound (a degree-range it owns), joy (a house it favors). The opposites — detriment (opposite its domicile) and fall (opposite its exaltation) — weaken it.

• Sect light — the Sun in a day chart, the Moon in a night chart. The luminary that "leads" the chart, sets the predominant direction of the life.

• The 7 Hermetic Lots — sensitive points named for each of the seven planets, marking specific life themes: Fortune (bodily life, what's given to you), Spirit (the work of your soul, what you achieve), Eros (desire and love), Necessity (constraint), Courage (boldness), Victory (triumph), Nemesis (hidden adversaries).
"""


def analyze(chart: NatalChart) -> GeneralAnalysis:
    sect_report = sect_analyzer.analyze(chart)
    dignities = dignity_calculator.evaluate_all(chart)
    aspects = aspect_calculator.aspects_in(chart)

    summary = _build_summary(chart, sect_report)
    structural = _build_structural_narrative(chart, sect_report, dignities, aspects)

    planet_readings = [_build_planet_reading(p, chart, sect_report, dignities) for p in ALL_PLANETS]
    aspect_readings = [
        AspectReading(
            aspect=a,
            paragraph=(aspect_pair_library.delineation(a.first, a.second, a.kind) +
                       " " + aspect_pair_library.orb_qualifier(a))
        )
        for a in aspects
    ]

    lot_table = _build_lot_table(chart)
    lot_readings = [_build_lot_reading(kind, chart) for kind in ALL_LOTS]
    positive = _build_positive(chart, sect_report, dignities)
    negative = _build_negative(chart, sect_report, dignities, aspects)

    return GeneralAnalysis(
        glossary=READING_GUIDE,
        summary=summary,
        structural_narrative=structural,
        planet_readings=planet_readings,
        aspect_readings=aspect_readings,
        lot_table=lot_table,
        lot_readings=lot_readings,
        positive_highlights=positive,
        negative_highlights=negative,
        sect_report=sect_report,
        dignity_reports=dignities,
    )


def _build_summary(chart: NatalChart, sect_report: SectReport) -> str:
    asc = chart.ascendant_sign
    asc_ruler = DOMICILE_RULER[asc]
    asc_ruler_pos = chart.position(asc_ruler)
    asc_ruler_sign_name = asc_ruler_pos.sign.display_name if asc_ruler_pos else "—"
    asc_ruler_house_num = chart.house_place_for_sign(asc_ruler_pos.sign).value if asc_ruler_pos else 0
    asc_ruler_degree = dl.format_degree(asc_ruler_pos) if asc_ruler_pos else "—"

    chart_foundation = "**I. Chart Foundation**\n\n" + dl.sect_narrative(sect_report.sect)

    asc_paragraph = (
        "**II. The Ascendant & Its Ruler**\n\n"
        f"The rising sign is **{asc.display_name}** ({dl.sign_keywords(asc)}). "
        f"The planet that rules {asc.display_name} is **{asc_ruler.display_name}**, "
        f"and it sits at {asc_ruler_degree}, in the {dl.ordinal(asc_ruler_house_num)} house. "
        f"This 'lord of the rising sign' is the helmsman of the chart — the planet that carries the native through the life "
        f"(HA Ch. 11; AAS Chs. 4–6). The conditions of {asc_ruler.display_name}, and the affairs of the "
        f"{dl.ordinal(asc_ruler_house_num)} house, shape much of how the life unfolds."
    )

    sect_light_topic = sect_report.sect_light_house.topic.lower()
    light_pos = chart.position(sect_report.sect_light)
    sect_light_degree = dl.format_degree(light_pos) if light_pos else sect_report.sect_light_sign.display_name
    day_or_night = "day" if sect_report.sect is Sect.DIURNAL else "night"

    if sect_report.sect_light_is_in_aversion:
        light_line = (
            f"The sect light — the **{sect_report.sect_light.display_name}** for this {day_or_night} chart — "
            f"sits at {sect_light_degree}, in the {dl.ordinal(sect_report.sect_light_house.value)} house ({sect_light_topic}). "
            "The house is in aversion to the rising sign (HA Ch. 11): the luminary that ought to lead the life cannot directly "
            "configure to the 1st. The practical implication is that integrating the sect light's themes will require conscious "
            "effort rather than arriving naturally."
        )
    else:
        light_line = (
            f"The sect light — the **{sect_report.sect_light.display_name}** for this {day_or_night} chart — "
            f"sits at {sect_light_degree}, in the {dl.ordinal(sect_report.sect_light_house.value)} house ({sect_light_topic}). "
            "It is well-situated to lead the chart (HA Ch. 7; AATP II). A foundational support — "
            "the affairs of this house are where the soul keeps returning."
        )

    return "\n\n".join([chart_foundation, asc_paragraph, light_line])


def _build_structural_narrative(chart: NatalChart, sect_report: SectReport,
                                dignities: list[DignityReport], aspects: list[Aspect]) -> str:
    asc = chart.ascendant_sign
    asc_ruler = DOMICILE_RULER[asc]
    asc_ruler_pos = chart.position(asc_ruler)
    assert asc_ruler_pos is not None
    asc_ruler_house = chart.house_place_for_sign(asc_ruler_pos.sign)
    asc_ruler_dignity = next(d for d in dignities if d.planet is asc_ruler)

    strongest = max(dignities, key=lambda d: d.score, default=None)
    weakest = min(dignities, key=lambda d: d.score, default=None)

    chart_centers = {asc_ruler, sect_report.sect_light}
    loud_partile = next(
        (a for a in aspects if a.is_partile and (a.first in chart_centers or a.second in chart_centers)),
        None,
    ) or next((a for a in aspects if a.is_partile and a.kind.harmony is Harmony.HARD), None)

    sentences: list[str] = []
    day_or_night = "diurnal" if sect_report.sect is Sect.DIURNAL else "nocturnal"
    sentences.append(
        f"Taken together, the chart's gravitational center sits at the meeting of three factors: the "
        f"**{asc.display_name} Ascendant** (carried by {asc_ruler.display_name} into the "
        f"{dl.ordinal(asc_ruler_house.value)} house), the **{day_or_night} sect** (with "
        f"{sect_report.benefic.display_name} as the help-planet and {sect_report.malefic.display_name} as the "
        f"pressure-planet), and the **{sect_report.sect_light.display_name} as sect light** in the "
        f"{dl.ordinal(sect_report.sect_light_house.value)} house."
    )

    if asc_ruler_dignity.score >= 3:
        sentences.append(
            f"{asc_ruler.display_name} — the chart's helmsman — is well-dignified (essential dignity score "
            f"{asc_ruler_dignity.score}), which is structurally favorable: the planet carrying the native through the life is "
            f"doing so from a position of strength (HA Ch. 11)."
        )
    elif asc_ruler_dignity.score <= -4:
        sentences.append(
            f"{asc_ruler.display_name} — the chart's helmsman — is in essential debility (dignity score "
            f"{asc_ruler_dignity.score}). This is structurally load-bearing: the planet that carries the native operates "
            f"against friction (HA Ch. 8; AATP I Ch. 4). The work is not glamorous but it is foundational."
        )
    else:
        sentences.append(
            f"{asc_ruler.display_name} — the chart's helmsman — operates at a middle register of essential dignity. The "
            f"conditions of the {dl.ordinal(asc_ruler_house.value)} house and the aspects to {asc_ruler.display_name} are where "
            f"to read how the life is being carried (HA Ch. 11)."
        )

    if strongest is not None and strongest.score >= 4:
        sentences.append(
            f"The chart's most powerful significator is **{strongest.planet.display_name}** in {strongest.sign.display_name} "
            f"(dignity score {strongest.score}) — a working source of strength wherever its house affairs are touched."
        )
    if weakest is not None and weakest.score <= -4:
        sentences.append(
            f"The chart's most compromised significator is **{weakest.planet.display_name}** in {weakest.sign.display_name} "
            f"(dignity score {weakest.score}). None of this prevents {weakest.planet.display_name} from operating; it does "
            f"describe the cost of admission (AAS Chs. 4–6)."
        )

    if loud_partile is not None:
        kind_label = loud_partile.kind.value
        sentences.append(
            f"The chart's loudest single configuration is **{loud_partile.first.display_name} {kind_label} "
            f"{loud_partile.second.display_name}** {aspect_pair_library.orb_qualifier(loud_partile)} — "
            f"one of the structural facts to keep in view when reading any topic that touches either planet (HA Ch. 9)."
        )

    sentences.append(
        "All delineations describe tendencies and thematic pressures, not fixed outcomes. The chart is a map of the terrain, "
        "not the journey itself."
    )

    return "**IX. Chart Summary — The Structural Narrative**\n\n" + " ".join(sentences)


def _build_planet_reading(planet: Planet, chart: NatalChart, sect_report: SectReport,
                          dignities: list[DignityReport]) -> PlanetReading:
    position = chart.position(planet)
    assert position is not None
    house = chart.house_place_for_sign(position.sign)
    dignity = next(d for d in dignities if d.planet is planet)

    title_line = f"**{planet.display_name} — {dl.format_degree(position)}, {dl.ordinal(house.value)} House**"
    status_block = dl.planet_status_block(planet, position, dignity, sect_report, house)

    sign_line = planet_in_sign_library.delineation(planet, position.sign)
    house_line = planet_in_house_library.delineation(planet, house)
    house_structural_line = dl.house_structural_note(house)
    dignity_line = dl.dignity_narrative(dignity)
    sect_line = _sect_status_line(planet, sect_report)
    retrograde_line = (" It is retrograde at birth — its significations turn inward, against the flow, "
                       "and ripen later (HA Ch. 5).") if position.is_retrograde else ""

    prose_parts = [sign_line, house_line, house_structural_line, dignity_line + retrograde_line, sect_line]
    prose = " ".join(p for p in prose_parts if p)

    paragraph = "\n\n".join([title_line, status_block, prose])
    return PlanetReading(planet=planet, sign=position.sign, house=house, paragraph=paragraph, dignity_score=dignity.score)


def _sect_status_line(planet: Planet, sect_report: SectReport) -> str:
    day_or_night = "day" if sect_report.sect is Sect.DIURNAL else "night"
    if planet == sect_report.benefic:
        return (f"Because this is a {day_or_night} chart, {planet.display_name} is your 'benefic of sect' — the helpful planet "
                f"best able to deliver good in your life. Wherever {planet.display_name} sits is where help most readily flows in.")
    if planet == sect_report.contrary_benefic:
        return (f"{planet.display_name} is the 'benefic contrary to sect' — still a helpful planet, but its gifts are quieter "
                f"and require more cultivation than the benefic of sect.")
    if planet == sect_report.malefic:
        return (f"Because this is a {day_or_night} chart, {planet.display_name} is your 'malefic contrary to sect' — the planet "
                f"most able to bring difficulty in your life. Its house and the topics it touches are the chart's area of greatest friction.")
    if planet == sect_report.contrary_malefic:
        return (f"{planet.display_name} is your 'malefic of sect' — still capable of harm, but moderated by being on the team "
                f"that matches your chart's sect. Its difficulties tend to be workable rather than acute.")
    if planet == sect_report.sect_light:
        return (f"{planet.display_name} is your 'sect light' — the luminary that leads a {day_or_night} chart. The affairs of "
                f"the house it occupies are where the soul keeps returning.")
    return ""


def _build_lot_table(chart: NatalChart) -> list[str]:
    rows: list[str] = []
    for kind in ALL_LOTS:
        lot = chart.lot(kind)
        lot_house = chart.house_place_for_sign(lot.sign)
        lord = DOMICILE_RULER[lot.sign]
        lord_pos = chart.position(lord)
        assert lord_pos is not None
        lord_house = chart.house_place_for_sign(lord_pos.sign)
        aspect_label = _lord_to_lot_aspect_label(lord_pos.sign, lot.sign)
        rows.append(lot_library.table_row(kind, lot, lot_house, lord, lord_house, aspect_label))
    return rows


def _lord_to_lot_aspect_label(lord_sign: ZodiacSign, lot_sign: ZodiacSign) -> str:
    delta = (int(lord_sign) - int(lot_sign)) % 12
    return {
        0: "same sign", 6: "opposition",
        4: "trine", 8: "trine",
        3: "square", 9: "square",
        2: "sextile", 10: "sextile",
    }.get(delta, "aversion (lord cannot see the lot)")


def _build_lot_reading(kind: HermeticLot, chart: NatalChart) -> LotReading:
    lot = chart.lot(kind)
    lot_sign = lot.sign
    house = chart.house_place_for_sign(lot_sign)

    lot_ruler = DOMICILE_RULER[lot_sign]
    ruler_pos = chart.position(lot_ruler)
    assert ruler_pos is not None
    ruler_house = chart.house_place_for_sign(ruler_pos.sign)

    topic_line = lot_library.topic(kind)
    placement = (f"In your chart, the {kind.display_name} sits in {lot_sign.display_name}, in your "
                 f"{dl.ordinal(house.value)} house — {house.topic.lower()}.")
    ruler_line = (f"The planet that rules {lot_sign.display_name} is {lot_ruler.display_name}, and "
                  f"{lot_ruler.display_name} sits in your {dl.ordinal(ruler_house.value)} house "
                  f"({ruler_house.topic.lower()}). In Hellenistic technique, that ruling planet is the one that "
                  f"'carries' the lot — its placement and condition shape how the lot's significations actually reach you.")
    example = lot_library.life_example(kind, house, ruler_house)

    paragraph = "\n\n".join([topic_line, placement, ruler_line, example])
    return LotReading(lot=kind, sign=lot_sign, house=house, paragraph=paragraph)


def _build_positive(chart: NatalChart, sect_report: SectReport,
                    dignities: list[DignityReport]) -> list[str]:
    notes: list[str] = []
    strongest = sorted(dignities, key=lambda d: -d.score)[:2]
    for d in strongest:
        if d.score < 3:
            continue
        house = chart.house_place_for_sign(d.sign)
        notes.append(
            f"**Lean on {d.planet.display_name} deliberately.** {d.planet.display_name} in {d.sign.display_name} is "
            f"well-dignified (essential dignity score {d.score}) — a working source of strength in the chart (HA Ch. 8). "
            f"The practical implication: the topics of the {dl.ordinal(house.value)} house, and what {d.planet.display_name} "
            f"signifies elsewhere by aspect, are areas where the chart says *yes* with the least friction.\n\n"
            f"**Chart basis:** {d.planet.display_name} in {d.sign.display_name} (essential dignity score {d.score}); "
            f"house: {dl.ordinal(house.value)}."
        )

    ben_pos = chart.position(sect_report.benefic)
    if ben_pos is not None:
        house = chart.house_place_for_sign(ben_pos.sign)
        day_or_night = "day" if sect_report.sect is Sect.DIURNAL else "night"
        notes.append(
            f"**Engage the affairs of the {dl.ordinal(house.value)} house deliberately.** {sect_report.benefic.display_name}, "
            f"the benefic of sect, sits there — the chart's primary delivery vehicle for good (HA Ch. 7). The practical "
            f"implication: when the native turns toward {house.topic.lower()}, help arrives more readily than it does anywhere "
            f"else in the chart.\n\n"
            f"**Chart basis:** {sect_report.benefic.display_name} (benefic of sect, {day_or_night} chart) in the "
            f"{dl.ordinal(house.value)} house."
        )

    for d in dignities:
        if not d.rejoices_in_house:
            continue
        joy_house = PLANETARY_JOY[d.planet]
        notes.append(
            f"**Let {d.planet.display_name} lead in matters of {joy_house.topic.lower()}.** {d.planet.display_name} rejoices in "
            f"the {joy_house.value}{dl.ordinal_suffix(joy_house.value)} house (HA Ch. 10) — a positional dignity that lets the "
            f"planet act in its most characteristic way. The practical implication: this is where {d.planet.display_name}'s "
            f"nature finds its most native channel.\n\n"
            f"**Chart basis:** {d.planet.display_name} in joy in the {dl.ordinal(joy_house.value)} house."
        )

    if not notes:
        notes.append(
            "**Read the chart through its quiet supports.** No planet is in strong essential dignity, but every chart has "
            "working resources (AAS Chs. 4–6). Look to the sect light, the ruler of the Ascendant, and any planets configured "
            "by Ptolemaic aspect to the 1st for the chart's reliable channels.\n\n"
            "**Chart basis:** absence of strong essential dignity; sect light and chart ruler as fallback significators (HA Chs. 7, 11)."
        )
    return notes


def _build_negative(chart: NatalChart, sect_report: SectReport, dignities: list[DignityReport],
                    aspects: list[Aspect]) -> list[str]:
    notes: list[str] = []

    weakest = sorted(dignities, key=lambda d: d.score)[:2]
    for d in weakest:
        if d.score > -4:
            continue
        house = chart.house_place_for_sign(d.sign)
        condition = "detriment" if d.is_in_detriment else "fall"
        notes.append(
            f"**Expect friction in matters of {house.topic.lower()}; plan the work.** {d.planet.display_name} is in essential "
            f"debility in {d.sign.display_name} (dignity score {d.score} — {condition}) (HA Ch. 8; AATP I Ch. 4). The practical "
            f"implication: {d.planet.display_name}'s significations arrive with delay, distortion, or extra cost. None of this "
            f"prevents {d.planet.display_name} from operating; it does describe the cost of admission.\n\n"
            f"**Chart basis:** {d.planet.display_name} in {d.sign.display_name} (dignity score {d.score}); "
            f"house: {dl.ordinal(house.value)}."
        )

    mal_pos = chart.position(sect_report.malefic)
    if mal_pos is not None:
        house = chart.house_place_for_sign(mal_pos.sign)
        day_or_night = "day" if sect_report.sect is Sect.DIURNAL else "night"
        notes.append(
            f"**The {dl.ordinal(house.value)} house is the chart's loudest pressure-point.** "
            f"{sect_report.malefic.display_name}, the malefic contrary to sect, occupies it (HA Ch. 7). The practical "
            f"implication: the affairs of this house demand effort, attention, and resilience — and the work done here, slowly, "
            f"is where the chart's deepest mastery is forged.\n\n"
            f"**Chart basis:** {sect_report.malefic.display_name} (malefic contrary to sect, {day_or_night} chart) in the "
            f"{dl.ordinal(house.value)} house."
        )

    averted = [pos for pos in chart.positions
               if chart.house_place_for_sign(pos.sign).is_in_aversion_to_ascendant]
    if averted:
        phrases = ", ".join(
            f"{p.planet.display_name} ({dl.ordinal(chart.house_place_for_sign(p.sign).value)} — "
            f"{chart.house_place_for_sign(p.sign).hellenistic_name})"
            for p in averted
        )
        notes.append(
            f"**Bring averted significations across the threshold through external channels.** Planets in aversion to the "
            f"rising sign: {phrases}. These planets cannot configure to the 1st by any Ptolemaic aspect (HA Ch. 11), so their "
            f"significations actualize with difficulty — the topics they govern tend to arrive through hidden, oblique, or "
            f"external channels rather than through the native's direct will. The practical implication: assume the topics "
            f"they govern need external structure or witness to land cleanly.\n\n"
            f"**Chart basis:** aversion of the listed planets to the Ascendant."
        )

    light_pos = chart.position(sect_report.sect_light)
    if light_pos is not None:
        light_lord = DOMICILE_RULER[light_pos.sign]
        lord_pos = chart.position(light_lord)
        if lord_pos is not None:
            delta = (int(lord_pos.sign) - int(light_pos.sign)) % 12
            if delta in (1, 5, 7, 11):
                notes.append(
                    "**Don't expect the sect light's house to deliver without scaffolding.** The sect light's domicile lord "
                    f"({light_lord.display_name}) is in aversion to the sect light itself (HA Ch. 11) — the luminary leading the "
                    "chart cannot fully draw on its own ruler's support. The practical implication: the soul's leading edge has "
                    "to find its scaffolding from elsewhere in the chart.\n\n"
                    f"**Chart basis:** {sect_report.sect_light.display_name} (sect light) in aversion to its domicile lord "
                    f"{light_lord.display_name}."
                )

    for a in aspects:
        if a.kind.harmony is not Harmony.HARD:
            continue
        if a.first != sect_report.malefic and a.second != sect_report.malefic:
            continue
        other = a.second if a.first == sect_report.malefic else a.first
        notes.append(
            f"**Watch what {other.display_name} signifies — {sect_report.malefic.display_name} is pressing on it.** "
            f"{sect_report.malefic.display_name} is in {a.kind.value} with {other.display_name} "
            f"{aspect_pair_library.orb_qualifier(a)}. This is a notable affliction (HA Ch. 6) — the chart's loudest pressure-"
            f"planet has a direct line to {other.display_name}'s significations. The practical implication: the topics "
            f"{other.display_name} carries will run hotter than the native's chart-as-a-whole would suggest.\n\n"
            f"**Chart basis:** {sect_report.malefic.display_name} (malefic contrary to sect) {a.kind.value} "
            f"{other.display_name} {aspect_pair_library.orb_qualifier(a)}."
        )

    if not notes:
        notes.append(
            "**No flagged challenges — but every chart has friction; read it from the houses of the malefics.** This chart has "
            "no glaring afflictions in essential dignity, sect, or aspect. The practical implication: the malefics are "
            f"reasonably contained, so the chart's ordinary friction will be felt where {sect_report.malefic.display_name} and "
            f"{sect_report.contrary_malefic.display_name} sit by house, not from acute partile hits.\n\n"
            "**Chart basis:** no major essential debilities; no partile hard aspects from the malefic contrary to sect."
        )
    return notes
