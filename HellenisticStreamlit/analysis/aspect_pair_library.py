"""Planet-pair-specific delineations for each of the 5 Ptolemaic aspects.

21 unique pairs × 5 aspects = 105 entries. Ported verbatim from Swift
`Analysis/AspectPairLibrary.swift`.

References: Brennan, Hellenistic Astrology, Ch. 9; George, AATP Vol II.
"""
from __future__ import annotations

from models.aspect import Aspect, AspectKind
from models.planet import Planet


def _pair(a: Planet, b: Planet) -> tuple[Planet, Planet]:
    """Canonical unordered pair, ordered by Planet value (lexicographic)."""
    return (a, b) if a.value <= b.value else (b, a)


_TABLE: dict[tuple[Planet, Planet], dict[AspectKind, str]] = {

    # MARK: - Sun pairs

    _pair(Planet.SUN, Planet.MOON): {
        AspectKind.CONJUNCTION: "New-moon birth — the two luminaries fuse; soul and body operate as a single current. Identity and feeling become difficult to distinguish.",
        AspectKind.SEXTILE:     "The two luminaries lend each other ease — direction and inner life support each other through small acts of alignment.",
        AspectKind.SQUARE:      "Friction between identity and feeling — what the native wants to be conflicts with what they need to feel.",
        AspectKind.TRINE:       "A flowing alignment between direction and inner life — the native's will and feelings reinforce each other naturally.",
        AspectKind.OPPOSITION:  "Full-moon birth — the two luminaries polarize. The native lives the tension between who they are and what they need.",
    },

    _pair(Planet.SUN, Planet.MERCURY): {
        AspectKind.CONJUNCTION: "Identity and mind are fused — the native thinks themselves into being; voice and self are one. (Mercury is rarely far from the Sun, so this configuration is common.)",
        AspectKind.SEXTILE:     "A graceful flow between identity and intellect — the native's mind serves their direction.",
        AspectKind.SQUARE:      "Tension between identity and mind — the native's voice contests their will, or vice versa.",
        AspectKind.TRINE:       "Identity and mind move together — speech naturally articulates self.",
        AspectKind.OPPOSITION:  "Identity and mind face each other — the native often speaks against themselves, or the inner voice contradicts the outer face.",
    },

    _pair(Planet.SUN, Planet.VENUS): {
        AspectKind.CONJUNCTION: "Identity and love are fused — the native shines through what they love; pleasure and selfhood are inseparable.",
        AspectKind.SEXTILE:     "A graceful flow between identity and love — the native's loves support their direction.",
        AspectKind.SQUARE:      "Tension between identity and love — what the native wants to be conflicts with what they want to love.",
        AspectKind.TRINE:       "Identity and love move together — relationship serves selfhood with little friction.",
        AspectKind.OPPOSITION:  "Identity and love face each other — the native must choose between the self and the beloved.",
    },

    _pair(Planet.SUN, Planet.MARS): {
        AspectKind.CONJUNCTION: "Identity and drive are fused — the native asserts themselves directly; will and action are one.",
        AspectKind.SEXTILE:     "A supportive flow between identity and drive — the native acts in line with who they are.",
        AspectKind.SQUARE:      "Friction between identity and drive — the native's actions undercut their direction, or vice versa.",
        AspectKind.TRINE:       "Identity and drive move together — the native's will is expressed in clean action.",
        AspectKind.OPPOSITION:  "Identity and drive face each other — the native's actions polarize against their direction; an inner contest plays out in the open.",
    },

    _pair(Planet.SUN, Planet.JUPITER): {
        AspectKind.CONJUNCTION: "Identity and good fortune are fused — the native shines large and is often blessed; presence carries gravity.",
        AspectKind.SEXTILE:     "A supportive flow between identity and good fortune — expansion arrives in line with who the native is.",
        AspectKind.SQUARE:      "Tension between identity and expansion — the native overreaches or feels limited by their own gifts.",
        AspectKind.TRINE:       "Identity and good fortune move together — the native's life enlarges through what they are.",
        AspectKind.OPPOSITION:  "Identity and expansion face each other — the native must choose between selfhood and the call to grow beyond it.",
    },

    _pair(Planet.SUN, Planet.SATURN): {
        AspectKind.CONJUNCTION: "Identity and restriction are fused — the native is structured, grave, often older than their years; self-mastery is a signature.",
        AspectKind.SEXTILE:     "A workable flow between identity and discipline — the native's direction is steadied by structure.",
        AspectKind.SQUARE:      "Tension between identity and restriction — the native's will meets a wall, often inherited; mastery is earned through resistance.",
        AspectKind.TRINE:       "Identity and restriction move together — the native builds themselves carefully across time.",
        AspectKind.OPPOSITION:  "Identity and restriction face each other — the native's selfhood is challenged by limit, often through authority figures or time itself.",
    },

    # MARK: - Moon pairs

    _pair(Planet.MOON, Planet.MERCURY): {
        AspectKind.CONJUNCTION: "Feeling and mind are fused — the native thinks with the body; speech carries emotional weather.",
        AspectKind.SEXTILE:     "A supportive flow between feeling and intellect — inner life and ideas converse with ease.",
        AspectKind.SQUARE:      "Tension between feeling and mind — the native's emotions undercut their thinking, or speech runs ahead of feeling.",
        AspectKind.TRINE:       "Feeling and mind move together — the native articulates inner life cleanly.",
        AspectKind.OPPOSITION:  "Feeling and mind face each other — the native's heart and head live in dialogue, sometimes in standoff.",
    },

    _pair(Planet.MOON, Planet.VENUS): {
        AspectKind.CONJUNCTION: "Feeling and love are fused — the native nurtures and is nurtured through pleasure; eros and emotional life merge.",
        AspectKind.SEXTILE:     "A graceful flow between inner life and love — the native loves comfortably and from the body.",
        AspectKind.SQUARE:      "Tension between feeling and love — the native's needs and their loves are not aligned.",
        AspectKind.TRINE:       "Feeling and love move together — the native receives love through their body and gives it through care.",
        AspectKind.OPPOSITION:  "Feeling and love face each other — needing and loving pull in opposite directions.",
    },

    _pair(Planet.MOON, Planet.MARS): {
        AspectKind.CONJUNCTION: "Feeling and drive are fused — the native's emotions are urgent, sometimes combustible; needs become actions quickly.",
        AspectKind.SEXTILE:     "A workable flow between feeling and drive — the native acts in line with their needs.",
        AspectKind.SQUARE:      "Tension between feeling and drive — emotions and actions inflame each other; reactivity is a signature.",
        AspectKind.TRINE:       "Feeling and drive move together — the native's body knows what to do.",
        AspectKind.OPPOSITION:  "Feeling and drive face each other — the native must reconcile what they need with what they pursue.",
    },

    _pair(Planet.MOON, Planet.JUPITER): {
        AspectKind.CONJUNCTION: "Feeling and good fortune are fused — the native is emotionally generous, well-fed by feeling itself; the body carries grace.",
        AspectKind.SEXTILE:     "A supportive flow between inner life and good fortune — needs are met with little strain.",
        AspectKind.SQUARE:      "Tension between feeling and expansion — emotional life inflates beyond capacity, or the native's needs and their gifts disagree.",
        AspectKind.TRINE:       "Feeling and good fortune move together — the native's body is at home with abundance.",
        AspectKind.OPPOSITION:  "Feeling and expansion face each other — the native must choose between need and gift.",
    },

    _pair(Planet.MOON, Planet.SATURN): {
        AspectKind.CONJUNCTION: "Feeling and restriction are fused — the native's emotional life is held in, structured, sometimes lonely. Maturity arrives early.",
        AspectKind.SEXTILE:     "A workable flow between feeling and discipline — the native steadies their inner life through structure.",
        AspectKind.SQUARE:      "Tension between feeling and restriction — emotional life meets a wall; the native often feels denied what they need.",
        AspectKind.TRINE:       "Feeling and restriction move together — the native masters their needs across time.",
        AspectKind.OPPOSITION:  "Feeling and restriction face each other — the native's emotional life is in dialogue with limit, often through elders or absence.",
    },

    # MARK: - Mercury pairs

    _pair(Planet.MERCURY, Planet.VENUS): {
        AspectKind.CONJUNCTION: "Mind and love are fused — the native loves through speech and finds beauty in ideas.",
        AspectKind.SEXTILE:     "A graceful flow between intellect and love — the native is articulate in matters of beauty.",
        AspectKind.SQUARE:      "Tension between mind and love — what the native thinks conflicts with what they love.",
        AspectKind.TRINE:       "Mind and love move together — the native makes love articulate.",
        AspectKind.OPPOSITION:  "Mind and love face each other — the native must reconcile thinking and loving, sometimes choosing between the two.",
    },

    _pair(Planet.MERCURY, Planet.MARS): {
        AspectKind.CONJUNCTION: "Mind and drive are fused — the native's thinking is sharp, fast, sometimes combative; speech cuts.",
        AspectKind.SEXTILE:     "A supportive flow between intellect and drive — the native acts on what they think.",
        AspectKind.SQUARE:      "Tension between mind and drive — thoughts inflame action; speech is impulsive or contested.",
        AspectKind.TRINE:       "Mind and drive move together — the native thinks and acts in line.",
        AspectKind.OPPOSITION:  "Mind and drive face each other — the native must reconcile thinking and doing, sometimes through public debate.",
    },

    _pair(Planet.MERCURY, Planet.JUPITER): {
        AspectKind.CONJUNCTION: "Mind and good fortune are fused — the native's thinking is broad, philosophical, sometimes preacher-like; speech expands.",
        AspectKind.SEXTILE:     "A supportive flow between intellect and good fortune — the native learns easily.",
        AspectKind.SQUARE:      "Tension between mind and expansion — the native's thinking inflates beyond what it can hold, or vision and detail conflict.",
        AspectKind.TRINE:       "Mind and good fortune move together — the native is gifted in study, teaching, or articulation of larger frameworks.",
        AspectKind.OPPOSITION:  "Mind and expansion face each other — the native must reconcile narrow analysis and broad vision.",
    },

    _pair(Planet.MERCURY, Planet.SATURN): {
        AspectKind.CONJUNCTION: "Mind and restriction are fused — the native's thinking is exact, careful, sometimes cold or burdened. Mastery of detail is a signature.",
        AspectKind.SEXTILE:     "A workable flow between intellect and discipline — the native structures their thinking well.",
        AspectKind.SQUARE:      "Tension between mind and restriction — speech meets a wall; the native is silenced, censored, or self-doubting.",
        AspectKind.TRINE:       "Mind and restriction move together — the native is a careful thinker, expert across time.",
        AspectKind.OPPOSITION:  "Mind and restriction face each other — the native's thinking is in dialogue with limit; sometimes silenced, sometimes magisterial.",
    },

    # MARK: - Venus pairs

    _pair(Planet.VENUS, Planet.MARS): {
        AspectKind.CONJUNCTION: "Love and drive are fused — eros is direct, embodied, sometimes urgent. The native is sexually visible.",
        AspectKind.SEXTILE:     "A supportive flow between love and drive — desire is easy and aligned.",
        AspectKind.SQUARE:      "Tension between love and drive — what the native loves and what they pursue disagree; eros becomes contested.",
        AspectKind.TRINE:       "Love and drive move together — desire and action align cleanly.",
        AspectKind.OPPOSITION:  "Love and drive face each other — the native must reconcile loving and pursuing, sometimes through a polarized partner.",
    },

    _pair(Planet.VENUS, Planet.JUPITER): {
        AspectKind.CONJUNCTION: "The two benefics are fused — love and good fortune merge; the native is graced in matters of love, beauty, and gift. Often a signature of prosperity.",
        AspectKind.SEXTILE:     "The two benefics support each other — life flows pleasantly; love and abundance meet easily.",
        AspectKind.SQUARE:      "Tension between the two benefics — love and good fortune compete; the native may overextend in either direction.",
        AspectKind.TRINE:       "The two benefics move together — love and abundance reinforce each other; an unusually fortunate signature.",
        AspectKind.OPPOSITION:  "The two benefics face each other — love and good fortune pull apart; the native may have to choose between intimate and expansive goods.",
    },

    _pair(Planet.VENUS, Planet.SATURN): {
        AspectKind.CONJUNCTION: "Love and restriction are fused — love is structured, committed, often delayed or austere. The native loves what lasts.",
        AspectKind.SEXTILE:     "A workable flow between love and discipline — the native loves carefully.",
        AspectKind.SQUARE:      "Tension between love and restriction — love meets a wall; the native is denied, delayed, or burdened in love.",
        AspectKind.TRINE:       "Love and restriction move together — the native loves slowly and across time; mastery in relationship.",
        AspectKind.OPPOSITION:  "Love and restriction face each other — the native's love is in dialogue with limit; sometimes loss, sometimes age or duty.",
    },

    # MARK: - Mars pairs

    _pair(Planet.MARS, Planet.JUPITER): {
        AspectKind.CONJUNCTION: "Drive and good fortune are fused — the native acts large; ambition is blessed; effort tends to succeed.",
        AspectKind.SEXTILE:     "A supportive flow between drive and good fortune — action expands the native's reach.",
        AspectKind.SQUARE:      "Tension between drive and expansion — ambition outruns capacity, or vision and action disagree.",
        AspectKind.TRINE:       "Drive and good fortune move together — the native acts boldly and is rewarded.",
        AspectKind.OPPOSITION:  "Drive and expansion face each other — the native must reconcile fight and faith, sometimes through public contest.",
    },

    _pair(Planet.MARS, Planet.SATURN): {
        AspectKind.CONJUNCTION: "The two malefics are fused — drive meets a wall; action is restricted, sometimes punished, sometimes mastered. A demanding placement, but mastery is possible.",
        AspectKind.SEXTILE:     "A workable flow between the two malefics — discipline channels drive; the native works hard within structure.",
        AspectKind.SQUARE:      "Tension between the two malefics — drive and restriction inflame each other; frustration, illness, or contest with authority are signatures.",
        AspectKind.TRINE:       "The two malefics move together — surprisingly, the native masters drive through structure; effort across time bears fruit.",
        AspectKind.OPPOSITION:  "The two malefics face each other — the native lives the contest between action and limit; a signature of struggle that often produces depth.",
    },

    # MARK: - Jupiter-Saturn

    _pair(Planet.JUPITER, Planet.SATURN): {
        AspectKind.CONJUNCTION: "The two great chronocrators are fused — the native carries a sense of timing, of when to expand and when to hold. A signature of long-arc judgment.",
        AspectKind.SEXTILE:     "A workable flow between expansion and discipline — the native grows in structured ways.",
        AspectKind.SQUARE:      "Tension between expansion and restriction — vision and limit disagree; the native often feels squeezed between growth and constraint.",
        AspectKind.TRINE:       "Expansion and discipline move together — the native builds carefully and large; a signature of sustained achievement.",
        AspectKind.OPPOSITION:  "Expansion and restriction face each other — the native lives the dialogue of growth and limit, often through public role or the long arc.",
    },
}


def delineation(first: Planet, second: Planet, kind: AspectKind) -> str:
    pair = _pair(first, second)
    entry = _TABLE.get(pair, {}).get(kind)
    if entry is not None:
        return entry
    return _default_delineation(first, second, kind)


def _default_delineation(first: Planet, second: Planet, kind: AspectKind) -> str:
    p1 = first.display_name
    p2 = second.display_name
    return {
        AspectKind.CONJUNCTION: f"{p1} and {p2} are fused — their significations operate as one body (HA Ch. 9).",
        AspectKind.SEXTILE:     f"{p1} and {p2} cooperate moderately — a supportive but reachable configuration (HA Ch. 9).",
        AspectKind.SQUARE:      f"{p1} and {p2} generate friction — the demand for adjustment between their significations is built into the chart (HA Ch. 9).",
        AspectKind.TRINE:       f"{p1} and {p2} flow together — their significations reinforce each other naturally (HA Ch. 9).",
        AspectKind.OPPOSITION:  f"{p1} and {p2} polarize — the native lives the tension between their significations (HA Ch. 9).",
    }[kind]


def orb_qualifier(aspect: Aspect) -> str:
    """Render the inline degree-precision used in the prose."""
    deg = int(aspect.orb)
    minutes = int((aspect.orb - deg) * 60.0)
    formatted = f"{deg}°{minutes:02d}'"
    if aspect.is_partile:
        return f"({formatted} — partile)"
    return f"({formatted} — whole-sign configuration)"
