"""Source-grounded short delineations for each of the 7 planets across the 12 signs.

84 entries. Ported verbatim from Swift `Analysis/PlanetInSignLibrary.swift`.
Where the placement carries an essential dignity (domicile, exaltation, fall,
detriment) it is named directly.

References: Brennan, Hellenistic Astrology, Chs. 4-5, 8; George, AATP Vol II;
Avelar & Ribeiro, On the Heavenly Spheres, Ch. 5.
"""
from __future__ import annotations

from models.planet import Planet
from models.zodiac import ZodiacSign


_TABLE: dict[Planet, dict[ZodiacSign, str]] = {

    Planet.SUN: {
        ZodiacSign.ARIES:       "The Sun is exalted in Aries — vitality and identity find their most honored expression in this cardinal fire sign of initiative. There is courage in the way the native pursues recognition.",
        ZodiacSign.TAURUS:      "The Sun in Taurus moves at the pace of growth and embodiment. Identity gathers slowly, through steady accumulation rather than declaration.",
        ZodiacSign.GEMINI:      "The Sun in Gemini shines through speech, exchange, and the work of meaning-making. Identity becomes plural — the native carries multiple selves and moves between them.",
        ZodiacSign.CANCER:      "The Sun in Cancer shines through caring, lineage, and protection of what is private. Identity is bound up with belonging — what the native nurtures, the native becomes.",
        ZodiacSign.LEO:         "The Sun is at home in Leo. Identity is sovereign, generous, and built to be seen; the native shines as themselves with little effort.",
        ZodiacSign.VIRGO:       "The Sun in Virgo shines through discernment, craft, and quiet service. Identity is refined through what the native attends to with care.",
        ZodiacSign.LIBRA:       "The Sun is in its fall in Libra — identity routes through relation rather than self-assertion. The native often defines themselves in dialogue, sometimes at the cost of their own light.",
        ZodiacSign.SCORPIO:     "The Sun in Scorpio shines through depth, intensity, and confrontation with what others avoid. Identity is forged in transformation.",
        ZodiacSign.SAGITTARIUS: "The Sun in Sagittarius shines through vision, seeking, and the journey outward. The native's identity is bound up with what they pursue beyond the horizon.",
        ZodiacSign.CAPRICORN:   "The Sun in Capricorn shines through structure, mastery, and time. Identity is built — not given — and grows in authority across the long arc.",
        ZodiacSign.AQUARIUS:    "The Sun in Aquarius shines through individuation and the outsider's vantage. The native often becomes themselves in distinction from a collective they nonetheless belong to.",
        ZodiacSign.PISCES:      "The Sun in Pisces shines through permeability and devotion — the boundaries of identity are porous, and the native often dissolves into what they love.",
    },

    Planet.MOON: {
        ZodiacSign.ARIES:       "The Moon in Aries needs activity and stimulus to feel itself. The body and feelings move quickly; emotional weather changes like a struck flint.",
        ZodiacSign.TAURUS:      "The Moon is exalted in Taurus — body and feeling settle into rhythm, comfort, and slow gathering. Stability is itself the native's nutrition.",
        ZodiacSign.GEMINI:      "The Moon in Gemini needs novelty, speech, and varied input. The body and feelings move through information.",
        ZodiacSign.CANCER:      "The Moon is at home in Cancer. Body and feeling are at ease — the native carries an inner shelter that they offer reflexively to others.",
        ZodiacSign.LEO:         "The Moon in Leo needs recognition, warmth, and creative expression. Feelings are large and visible; the native dramatizes their emotional life into the room.",
        ZodiacSign.VIRGO:       "The Moon in Virgo needs order, usefulness, and attention to detail to feel grounded. The body settles through care of small things.",
        ZodiacSign.LIBRA:       "The Moon in Libra needs relationship, aesthetic harmony, and fair exchange. The native often regulates their inner weather through their relationships.",
        ZodiacSign.SCORPIO:     "The Moon is in its fall in Scorpio — feeling runs deep and dark, and the body holds what it cannot release. The native's daily life is marked by intensity others may not access.",
        ZodiacSign.SAGITTARIUS: "The Moon in Sagittarius needs scope, travel, and meaning. The native is fed by horizon and idea more than by hearth.",
        ZodiacSign.CAPRICORN:   "The Moon in Capricorn needs structure, mastery, and time. Feelings are restrained — the body holds itself together with discipline, sometimes at a cost.",
        ZodiacSign.AQUARIUS:    "The Moon in Aquarius needs distance, ideas, and chosen company. Feelings flow through abstractions; the native's body resists possession.",
        ZodiacSign.PISCES:      "The Moon in Pisces needs permeability, devotion, and time alone with the imaginal. Feeling is oceanic, and the native dissolves easily into mood.",
    },

    Planet.MERCURY: {
        ZodiacSign.ARIES:       "Mercury in Aries thinks fast, speaks sharp, and moves first. The mind is a blade; ideas come out as initiatives.",
        ZodiacSign.TAURUS:      "Mercury in Taurus thinks slowly and concretely. Speech is deliberate; what the native learns, they learn through the body and through time.",
        ZodiacSign.GEMINI:      "Mercury is at home in Gemini. Speech, learning, and exchange flow naturally — the mind is plural and quick, in love with information.",
        ZodiacSign.CANCER:      "Mercury in Cancer thinks through feeling and memory. Speech protects, soothes, or remembers; ideas carry an emotional weight.",
        ZodiacSign.LEO:         "Mercury in Leo thinks dramatically and declares. Speech wants an audience; ideas are arranged for performance.",
        ZodiacSign.VIRGO:       "Mercury is doubly dignified in Virgo — at home and exalted. Discernment, craft, and analytical precision are signatures of the native's mind.",
        ZodiacSign.LIBRA:       "Mercury in Libra thinks relationally and in balance. Speech weighs both sides; ideas are tested through dialogue.",
        ZodiacSign.SCORPIO:     "Mercury in Scorpio thinks beneath the surface. The native sees through pretense; speech is investigative, sometimes piercing.",
        ZodiacSign.SAGITTARIUS: "Mercury in Sagittarius thinks in vision and broad pattern. The native sees the forest first; speech tends toward philosophy.",
        ZodiacSign.CAPRICORN:   "Mercury in Capricorn thinks structurally and across time. Speech is measured; ideas are built to last.",
        ZodiacSign.AQUARIUS:    "Mercury in Aquarius thinks systemically and from outside. The native's mind is at home in abstraction and pattern.",
        ZodiacSign.PISCES:      "Mercury is in its fall and detriment in Pisces. Speech and analysis dissolve into feeling and image — the native may struggle to render thought in words, but the imaginal range is wider than most.",
    },

    Planet.VENUS: {
        ZodiacSign.ARIES:       "Venus in Aries loves directly and with appetite. Beauty is found in vitality and contest; the native is drawn to what initiates.",
        ZodiacSign.TAURUS:      "Venus is at home in Taurus. Love is sensual, steady, and embodied; beauty is in slow accumulation and the senses well-tended.",
        ZodiacSign.GEMINI:      "Venus in Gemini loves through speech and curiosity. Multiple attractions, multiple sweetnesses; the native is drawn to what converses.",
        ZodiacSign.CANCER:      "Venus in Cancer loves through care and shelter. Beauty is found in lineage, home, and emotional safety.",
        ZodiacSign.LEO:         "Venus in Leo loves theatrically and generously. The native is drawn to what shines and what receives them in return.",
        ZodiacSign.VIRGO:       "Venus is in its fall in Virgo — love is filtered through discernment, attention to detail, and acts of service. The native may struggle to receive love that doesn't pass through usefulness.",
        ZodiacSign.LIBRA:       "Venus is at home in Libra. Love is gracious, relational, and aesthetically refined; partnership is itself a value.",
        ZodiacSign.SCORPIO:     "Venus in Scorpio loves intensely and through depth. Beauty is found in what is hidden, intimate, or transformative.",
        ZodiacSign.SAGITTARIUS: "Venus in Sagittarius loves across distance and through meaning. The native is drawn to what expands them — travel, philosophy, foreign places.",
        ZodiacSign.CAPRICORN:   "Venus in Capricorn loves through structure and commitment. Beauty is found in mastery, age, and what endures.",
        ZodiacSign.AQUARIUS:    "Venus in Aquarius loves at a distance and in friendship. The native is drawn to the unusual, the chosen, the kind of love that does not demand merging.",
        ZodiacSign.PISCES:      "Venus is exalted in Pisces — love is devotional, dissolving, and permeated by compassion. The native loves easily and risks losing themselves in it.",
    },

    Planet.MARS: {
        ZodiacSign.ARIES:       "Mars is at home in Aries. Drive, courage, and the will to act flow naturally; the native cuts and initiates with little hesitation.",
        ZodiacSign.TAURUS:      "Mars in Taurus moves slowly and lastingly. Anger and effort take time to gather, but once moving they are immovable.",
        ZodiacSign.GEMINI:      "Mars in Gemini fights with words and quick movement. Drive is mental and verbal; the native skirmishes rather than wars.",
        ZodiacSign.CANCER:      "Mars is in its fall in Cancer — drive is filtered through feeling, family, and protection. Anger is indirect, sometimes turned inward; the native fights for those they shelter.",
        ZodiacSign.LEO:         "Mars in Leo fights with display and pride. The native acts to be seen acting; drive is theatrical.",
        ZodiacSign.VIRGO:       "Mars in Virgo channels drive into craft and discernment. Anger sharpens detail; the native cuts with precision.",
        ZodiacSign.LIBRA:       "Mars in Libra fights relationally — through partnership, debate, and negotiation. Drive is mediated and easily blunted.",
        ZodiacSign.SCORPIO:     "Mars is at home in Scorpio. Drive runs deep, strategic, and unrelenting; the native acts from beneath the surface.",
        ZodiacSign.SAGITTARIUS: "Mars in Sagittarius fights for vision and meaning. Drive aims at horizons; the native is a crusader more than a fighter.",
        ZodiacSign.CAPRICORN:   "Mars is exalted in Capricorn — drive is structured, disciplined, and patient. The native conquers through time, not flash.",
        ZodiacSign.AQUARIUS:    "Mars in Aquarius fights for ideas and from the outside. Drive is detached and principled.",
        ZodiacSign.PISCES:      "Mars in Pisces moves through feeling, image, and indirection. Drive can scatter; the native fights subtly or not at all.",
    },

    Planet.JUPITER: {
        ZodiacSign.ARIES:       "Jupiter in Aries blesses initiative and courage. Expansion comes through pursuit; the native's good fortune lies in beginning.",
        ZodiacSign.TAURUS:      "Jupiter in Taurus blesses material steadiness and embodiment. Abundance gathers slowly, through patience and the senses.",
        ZodiacSign.GEMINI:      "Jupiter is in detriment in Gemini — expansion through information, but the native may scatter rather than deepen. Many small blessings, fewer large ones.",
        ZodiacSign.CANCER:      "Jupiter is exalted in Cancer. Abundance flows through home, lineage, and emotional nurture; the native carries an inner generosity.",
        ZodiacSign.LEO:         "Jupiter in Leo blesses recognition, creative expression, and largeness of presence. Good fortune arrives through being seen.",
        ZodiacSign.VIRGO:       "Jupiter is in detriment in Virgo — expansion is filtered through discernment and craft. The native struggles with bigness; their gifts come refined and small.",
        ZodiacSign.LIBRA:       "Jupiter in Libra blesses partnership, justice, and aesthetic refinement. Abundance comes through relationships and graceful exchange.",
        ZodiacSign.SCORPIO:     "Jupiter in Scorpio blesses depth and transformative work. Good fortune comes through what is hidden, inherited, or shared in intimacy.",
        ZodiacSign.SAGITTARIUS: "Jupiter is at home in Sagittarius. Vision, travel, philosophy, and meaning expand the native's life; good fortune flows through the search for truth.",
        ZodiacSign.CAPRICORN:   "Jupiter is in its fall in Capricorn — expansion is restrained by structure, time, and limit. The native's gifts arrive late and through earned authority rather than easy increase.",
        ZodiacSign.AQUARIUS:    "Jupiter in Aquarius blesses the unusual, the visionary, and the chosen community. Abundance comes through alliances and ideas.",
        ZodiacSign.PISCES:      "Jupiter is at home in Pisces. Devotion, compassion, and imaginal range bless the native; good fortune flows through what dissolves rather than what builds.",
    },

    Planet.SATURN: {
        ZodiacSign.ARIES:       "Saturn is in its fall in Aries — restriction meets the will to begin. Initiative is hampered or self-policed; the native learns mastery through restrained courage.",
        ZodiacSign.TAURUS:      "Saturn in Taurus restricts material flow and embodiment. Resources gather slowly, with effort; mastery is in the long discipline of the senses.",
        ZodiacSign.GEMINI:      "Saturn in Gemini structures speech, learning, and exchange. The native's mind is exact, careful, sometimes cold.",
        ZodiacSign.CANCER:      "Saturn is in detriment in Cancer — restriction meets the emotional waters. The native may feel unmothered, or burdened by family; sheltering is hard-won.",
        ZodiacSign.LEO:         "Saturn is in detriment in Leo — restriction meets the will to shine. The native's self-expression is filtered, ashamed, or earned through long discipline.",
        ZodiacSign.VIRGO:       "Saturn in Virgo masters craft, detail, and useful service. The native builds expertise through patient refinement.",
        ZodiacSign.LIBRA:       "Saturn is exalted in Libra. Justice, structure, and mastered relationship are the native's territory — they bring weight and authority to what they balance.",
        ZodiacSign.SCORPIO:     "Saturn in Scorpio masters depth and confrontation. The native works at the level of the buried; mastery comes through enduring what others flee.",
        ZodiacSign.SAGITTARIUS: "Saturn in Sagittarius structures meaning, vision, and belief. The native's philosophy is hard-earned and conservative.",
        ZodiacSign.CAPRICORN:   "Saturn is at home in Capricorn. Mastery, structure, and time are the native's medium — they build what lasts.",
        ZodiacSign.AQUARIUS:    "Saturn is at home in Aquarius. The native's mastery is in systems, in the outsider's vantage, in what gives form to a community.",
        ZodiacSign.PISCES:      "Saturn in Pisces structures devotion, imagination, and dissolution. The native gives shape to what others cannot hold — they discipline the dream.",
    },
}


def delineation(planet: Planet, sign: ZodiacSign) -> str:
    return _TABLE.get(planet, {}).get(
        sign,
        f"{planet.display_name} in {sign.display_name} takes on the coloration of the sign and its ruler.",
    )
