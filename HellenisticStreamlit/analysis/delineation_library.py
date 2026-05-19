"""Short, source-grounded text snippets composed into the prose analysis.

Ported from Swift `Analysis/DelineationLibrary.swift`. Citation conventions:
HA       — Brennan, Hellenistic Astrology
AATP I   — Demetra George, Ancient Astrology in Theory and Practice, Vol. I
AATP II  — Demetra George, Ancient Astrology in Theory and Practice, Vol. II
AAS      — Demetra George, Astrology and the Authentic Self
OHS      — Avelar & Ribeiro, On the Heavenly Spheres
YBFT     — Chani Nicholas, You Were Born for This
"""
from __future__ import annotations

from astrology.dignity_calculator import DignityReport
from astrology.sect_analyzer import SectReport
from models.aspect import Aspect, AspectKind
from models.house import HousePlace
from models.planet import Planet, PlanetaryPosition
from models.sect import Sect
from models.zodiac import ZodiacSign


def ordinal_suffix(n: int) -> str:
    if n == 1: return "st"
    if n == 2: return "nd"
    if n == 3: return "rd"
    return "th"


def ordinal(n: int) -> str:
    return f"{n}{ordinal_suffix(n)}"


# ----- Formatting helpers -----

def format_degree(position: PlanetaryPosition) -> str:
    """'Sign DD°MM'' — the inline precision used throughout."""
    deg = int(position.sign_degree)
    minutes = int((position.sign_degree - deg) * 60.0)
    return f"{position.sign.display_name} {deg}°{minutes:02d}'"


# ----- Sign / planet keywords (one-line significations) -----

def sign_keywords(sign: ZodiacSign) -> str:
    return {
        ZodiacSign.ARIES:       "initiative, courage, contest, the will to begin",
        ZodiacSign.TAURUS:      "embodiment, stability, the senses, slow accumulation",
        ZodiacSign.GEMINI:      "speech, exchange, multiplicity, learning by movement",
        ZodiacSign.CANCER:      "shelter, lineage, emotional memory, the work of caring",
        ZodiacSign.LEO:         "vital presence, generosity, recognition, sovereign self",
        ZodiacSign.VIRGO:       "discernment, craft, service, the refinement of detail",
        ZodiacSign.LIBRA:       "relation, justice, aesthetic, weighing and balancing",
        ZodiacSign.SCORPIO:     "depth, intensity, what is hidden, transformation through loss",
        ZodiacSign.SAGITTARIUS: "vision, search for meaning, the journey outward and upward",
        ZodiacSign.CAPRICORN:   "structure, mastery, time, the long arc of building",
        ZodiacSign.AQUARIUS:    "individuation, vision of the collective, the outsider's wisdom",
        ZodiacSign.PISCES:      "permeability, devotion, dissolution, the contemplative",
    }[sign]


def planet_keywords(planet: Planet) -> str:
    return {
        Planet.SUN:     "vitality, identity, the soul's direction, what one shines as",
        Planet.MOON:    "body, feeling, daily rhythm, the texture of needing and being needed",
        Planet.MERCURY: "mind, voice, exchange, the work of making meaning",
        Planet.VENUS:   "love, beauty, what attracts and is attracted, the gentling presence",
        Planet.MARS:    "drive, conflict, separation, the cutting edge that clears the way",
        Planet.JUPITER: "expansion, blessing, what protects and elevates, the generous yes",
        Planet.SATURN:  "limit, time, mastery through restriction, the cold teacher",
    }[planet]


# ----- House structural notes (Brennan Ch. 11) -----

def house_structural_note(place: HousePlace) -> str:
    return {
        HousePlace.FIRST:    "The 1st is the Hour-Marker — angular, the place of the body and the native's bearing (HA Ch. 11). Planets here imprint themselves directly on the life.",
        HousePlace.SECOND:   "The 2nd is the Gate of Hades — succedent but in aversion to the rising sign (HA Ch. 11). The planet cannot configure to the Ascendant by any Ptolemaic aspect, so its significations actualize at a remove; the topic operates indirectly.",
        HousePlace.THIRD:    "The 3rd is the Goddess — cadent, but configured to the Ascendant by sextile (HA Ch. 11). The planet IS 'seen' by the rising sign. Workable, though less prominent than the angular places.",
        HousePlace.FOURTH:   "The 4th is the Subterraneous — angular, the seat of private life and ancestry (HA Ch. 11). Planets here are written into the native's foundation.",
        HousePlace.FIFTH:    "The 5th is the place of Good Fortune — succedent and configured to the Ascendant by trine (HA Ch. 11). One of the most favorable non-angular places; planets here act in a supported register.",
        HousePlace.SIXTH:    "The 6th is the place of Bad Fortune — cadent AND in aversion to the rising sign (HA Ch. 11). One of the two darkest places in the chart; planets here struggle to actualize, and their topics tend to manifest through labor, illness, or subordination.",
        HousePlace.SEVENTH:  "The 7th is the Setting place — angular, where partnership and the significant other live (HA Ch. 11). Planets here come to the native through the other.",
        HousePlace.EIGHTH:   "The 8th is the Idle place — succedent but in aversion to the rising sign (HA Ch. 11). The planet cannot 'see' the Ascendant; its significations operate at a remove from the native's daily life, often arriving through others' resources or what passes between people.",
        HousePlace.NINTH:    "The 9th is the God place — cadent, but configured to the Ascendant by trine (HA Ch. 11). The planet IS 'seen' by the rising sign. Workable, and sacred to learning and the larger frameworks.",
        HousePlace.TENTH:    "The 10th is the Culmination — angular, the place of public action (HA Ch. 11). Planets here are visibly written into the native's vocation and reputation.",
        HousePlace.ELEVENTH: "The 11th is the place of Good Spirit — succedent and configured to the Ascendant by sextile (HA Ch. 11). Like the 5th, one of the most favorable non-angular places; planets here are lifted by chosen company.",
        HousePlace.TWELFTH:  "The 12th is the place of Bad Spirit — cadent AND in aversion to the rising sign (HA Ch. 11). The other of the two darkest places (with the 6th); planets here are most disconnected from the Ascendant, and their significations come through hidden or hostile channels.",
    }[place]


def house_topic_narrative(place: HousePlace) -> str:
    return {
        HousePlace.FIRST:    "your body and bearing, the temperament others first read in you",
        HousePlace.SECOND:   "what sustains you materially — money, possessions, resources you draw on",
        HousePlace.THIRD:    "siblings, neighbors, short journeys, the texture of daily communication",
        HousePlace.FOURTH:   "home, parents, ancestral inheritance, the private foundation of your life",
        HousePlace.FIFTH:    "children, pleasure, creative output, eros and play",
        HousePlace.SIXTH:    "labor, illness, subordinates, the body's wear and the work that wears it",
        HousePlace.SEVENTH:  "marriage, partnerships, the significant other (including open adversaries)",
        HousePlace.EIGHTH:   "death, others' resources, inheritance, what passes through your hands",
        HousePlace.NINTH:    "long journeys, philosophy, religion, the larger frameworks you live by",
        HousePlace.TENTH:    "vocation, public reputation, the action you take in the world",
        HousePlace.ELEVENTH: "friends, alliances, hopes realized, the company that lifts you",
        HousePlace.TWELFTH:  "hidden troubles, isolation, hostile forces, what undoes you from the dark",
    }[place]


# ----- Dignity narratives (Brennan Ch. 8) -----

def dignity_narrative(report: DignityReport) -> str:
    p = report.planet.display_name
    s = report.sign.display_name
    if report.is_in_domicile:
        return (f"{p} is in its domicile in {s} (HA Ch. 8). Domicile means {s} is one of the two signs {p} is said to rule — "
                f"{p} acts from strength and ease, and the topics it signifies tend toward good outcomes.")
    if report.is_in_exaltation:
        return (f"{p} is exalted in {s} (HA Ch. 8). Exaltation is a sign of honor for the planet — its influence is elevated "
                f"and tends to produce notably favorable results, sometimes with a touch of excess.")
    if report.is_in_fall:
        return (f"{p} is in its fall in {s} (HA Ch. 8; AATP I Ch. 4). Fall is the sign opposite a planet's exaltation — "
                f"{p} struggles to express itself effectively here, and what it signifies tends to come with difficulty, delay, "
                f"or distortion. None of this prevents {p} from operating; it does describe the cost of admission.")
    if report.is_in_detriment:
        return (f"{p} is in detriment in {s} (HA Ch. 8; AATP I Ch. 4). Detriment is the sign opposite a planet's domicile — "
                f"{p} is in a sign whose nature opposes its own, so its themes are challenged and require conscious work. "
                f"None of this prevents {p} from operating; it does describe the cost of admission.")
    if report.is_triplicity_ruler:
        return (f"{p} is a triplicity ruler of {s} (HA Ch. 6, citing Dorotheus' scheme). Each element has three planets that "
                f"co-rule it — one for day charts, one for night, one cooperating. {p} gets a stable, supportive footing here "
                f"even without domicile or exaltation. A working strength.")
    if report.is_in_own_bound:
        return (f"{p} sits in its own Egyptian bound within {s} (HA Ch. 8). Bounds are degree-ranges within each sign, each "
                f"owned by one of the five non-luminary planets — a subtle, degree-level dignity. In the specific degrees {p} "
                f"governs, it works with a measure of authority.")
    return (f"{p} occupies {s} without essential dignity (HA Ch. 8) — neither at home, exalted, in its triplicity, nor in its "
            f"own bound here. It takes on the coloration of {s} and the placement of {s}'s ruler.")


# ----- Sect narrative -----

def sect_narrative(sect: Sect) -> str:
    if sect is Sect.DIURNAL:
        return ("This is a day chart (HA Ch. 7). The Sun was above the horizon at birth, and the diurnal team — Sun, Jupiter, "
                "Saturn — carries the chart. Jupiter is the benefic of sect (the chart's primary help-planet), and Mars is the "
                "malefic contrary to sect (the chart's primary pressure-planet). This single fact reorients everything that follows.")
    return ("This is a night chart (HA Ch. 7). The Sun was below the horizon at birth, and the nocturnal team — Moon, Venus, "
            "Mars — carries the chart. Venus is the benefic of sect (the chart's primary help-planet), and Saturn is the "
            "malefic contrary to sect (the chart's primary pressure-planet). This single fact reorients everything that follows.")


# ----- Status block & assessment phrase -----

def assessment_phrase(planet: Planet, dignity: DignityReport, sect_report: SectReport,
                      house: HousePlace, is_retrograde: bool) -> str:
    angular = house in (HousePlace.FIRST, HousePlace.FOURTH, HousePlace.SEVENTH, HousePlace.TENTH)
    averted = house.is_in_aversion_to_ascendant
    score = dignity.score
    is_sect_light = planet == sect_report.sect_light
    is_benefic_of_sect = planet == sect_report.benefic
    is_contrary_malefic = planet == sect_report.malefic
    # Luminaries always count as "own team"; other planets check team membership.
    diurnal_team = planet in (Planet.SUN, Planet.JUPITER, Planet.SATURN)
    in_own_team = planet in (Planet.SUN, Planet.MOON) or ((sect_report.sect is Sect.DIURNAL) == diurnal_team)

    if dignity.is_in_domicile and angular and in_own_team:
        return "Chart's most powerful significator."
    if dignity.is_in_exaltation and angular:
        return "Major source of strength."
    if is_benefic_of_sect and angular:
        return "Primary delivery vehicle for good in the chart."
    if is_contrary_malefic and angular:
        return "The chart's loudest pressure-point — handle with care."
    if is_sect_light and angular:
        return "Leads the life from a structurally prominent seat."
    if dignity.is_in_detriment and averted:
        return "Doubly compromised — debility plus aversion."
    if dignity.is_in_fall and averted:
        return "Doubly compromised — debility plus aversion."
    if dignity.is_in_detriment or dignity.is_in_fall:
        return "Essential debility — gifts arrive against friction."
    if averted and score <= 0:
        return "Operates at a remove from the native's direct will."
    if score >= 5:
        return "A working source of strength."
    if score >= 3:
        return "Solidly placed; reliable significator."
    if is_retrograde and score < 0:
        return "Reduced and turned inward; significations ripen late."
    if is_retrograde:
        return "Functional but turned inward."
    if angular:
        return "Structurally prominent without major dignity."
    if averted:
        return "Workable, but at a remove from the rising sign."
    return "Operating in a middle register — neither flagged as a chart specialty nor a chart difficulty."


def planet_status_block(planet: Planet, position: PlanetaryPosition, dignity: DignityReport,
                        sect_report: SectReport, house: HousePlace) -> str:
    # Dignity phrase.
    if dignity.is_in_domicile:
        dignity_phrase = "Domicile (in its own sign)."
    elif dignity.is_in_exaltation:
        dignity_phrase = "Exaltation (sign of honor)."
    elif dignity.is_in_detriment:
        dignity_phrase = "Detriment (opposite its domicile)."
    elif dignity.is_in_fall:
        dignity_phrase = "Fall (opposite its exaltation)."
    elif dignity.is_triplicity_ruler:
        role = dignity.triplicity_role or "shared"
        dignity_phrase = f"Triplicity ruler ({role} of {position.sign.element})."
    elif dignity.is_in_own_bound:
        dignity_phrase = "In its own bound (degree-level dignity)."
    else:
        dignity_phrase = f"Peregrine (no major essential dignity in {position.sign.display_name})."

    # Sect phrase.
    day_or_night = "day" if sect_report.sect is Sect.DIURNAL else "night"
    if planet == sect_report.sect_light:
        sect_phrase = f"Sect light (the luminary leading a {day_or_night} chart)."
    elif planet == sect_report.benefic:
        sect_phrase = "Of sect — benefic of sect (chart's primary help-planet)."
    elif planet == sect_report.contrary_benefic:
        sect_phrase = "Contrary to sect — benefic, but gifts require cultivation."
    elif planet == sect_report.malefic:
        sect_phrase = "Contrary to sect — malefic (chart's primary pressure-planet)."
    elif planet == sect_report.contrary_malefic:
        sect_phrase = "Of sect — malefic, but moderated by being on the chart's team."
    else:
        sect_phrase = "Mercury takes its sect from the side of the Sun it sits on (HA Ch. 7)."

    # House phrase.
    angular = house in (HousePlace.FIRST, HousePlace.FOURTH, HousePlace.SEVENTH, HousePlace.TENTH)
    succedent = house in (HousePlace.SECOND, HousePlace.FIFTH, HousePlace.EIGHTH, HousePlace.ELEVENTH)
    cadent = house in (HousePlace.THIRD, HousePlace.SIXTH, HousePlace.NINTH, HousePlace.TWELFTH)
    averted = house.is_in_aversion_to_ascendant
    house_phrase = f"{house.value}{ordinal_suffix(house.value)} house"
    if angular:   house_phrase += " — angular."
    if succedent: house_phrase += " — succedent."
    if cadent:    house_phrase += " — cadent."
    if averted:   house_phrase += " In aversion to the rising sign."
    if dignity.rejoices_in_house:
        house_phrase += " The planet's joy."

    assess = assessment_phrase(planet, dignity, sect_report, house, position.is_retrograde)
    return (f"**Dignity:** {dignity_phrase} **Sect:** {sect_phrase} "
            f"**House:** {house_phrase} **Assessment:** {assess}")


# ----- Aspect narrative -----

def aspect_narrative(aspect: Aspect) -> str:
    p1 = aspect.first.display_name
    p2 = aspect.second.display_name
    glyph = aspect.kind.glyph
    qualifier = " (partile — within 3°, emits a strong ray)" if aspect.is_partile else ""
    return {
        AspectKind.CONJUNCTION: f"{p1} {glyph} {p2}{qualifier}: the two operate as one body, blending their significations (HA Ch. 9).",
        AspectKind.SEXTILE:     f"{p1} {glyph} {p2}{qualifier}: a moderate, supportive configuration — opportunity that requires reaching (HA Ch. 9).",
        AspectKind.SQUARE:      f"{p1} {glyph} {p2}{qualifier}: a hard configuration — friction, conflict, the demand for change between these significations (HA Ch. 9).",
        AspectKind.TRINE:       f"{p1} {glyph} {p2}{qualifier}: a harmonious flow between these significations — natural and easy expression (HA Ch. 9).",
        AspectKind.OPPOSITION:  f"{p1} {glyph} {p2}{qualifier}: polarity and tension — these significations pull in opposite directions and must be balanced (HA Ch. 9).",
    }[aspect.kind]


def bonification_footnote(planet: Planet, helper: Planet) -> str:
    return f"{helper.display_name} bonifies {planet.display_name} — a structural mitigation: the chart provides its own answer to the difficulty (HA Ch. 6)."


def maltreatment_footnote(planet: Planet, harmer: Planet) -> str:
    return f"{harmer.display_name} maltreats {planet.display_name} — an aggravation that intensifies the planet's difficulty (HA Ch. 6)."
