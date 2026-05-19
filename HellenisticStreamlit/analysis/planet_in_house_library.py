"""Source-grounded delineations for each planet across the 12 whole-sign houses.

84 entries, ported verbatim from Swift `Analysis/PlanetInHouseLibrary.swift`.
Where a placement coincides with the planet's joy (Brennan Ch. 10, Fig 10.5),
it is named directly.

References: Brennan, Hellenistic Astrology, Chs. 10-12; George, AATP Vol II;
Avelar & Ribeiro, On the Heavenly Spheres, Ch. 7.
"""
from __future__ import annotations

from models.house import HousePlace
from models.planet import Planet


_TABLE: dict[Planet, dict[HousePlace, str]] = {

    Planet.SUN: {
        HousePlace.FIRST:    "The Sun in the 1st — vitality and identity are written directly on the body. The native is visible, sovereign, and rises into their own light early.",
        HousePlace.SECOND:   "The Sun in the 2nd — identity is bound up with livelihood and resources. The native shines through what they possess and provide.",
        HousePlace.THIRD:    "The Sun in the 3rd — identity expresses through siblings, neighbors, and daily communication. The native shines in short journeys and exchanges.",
        HousePlace.FOURTH:   "The Sun in the 4th — identity is rooted in home, parents, and ancestry. The native shines from the private foundation; their light is inherited.",
        HousePlace.FIFTH:    "The Sun in the 5th — identity expresses through children, pleasure, and creative output. The native shines in play and erotic life.",
        HousePlace.SIXTH:    "The Sun in the 6th — identity expresses through labor, illness, and service. The native shines through what wears them; vocation is bound up with bodily life.",
        HousePlace.SEVENTH:  "The Sun in the 7th — identity expresses through partnership. The native often shines in dialogue with the significant other, and is sometimes obscured by them.",
        HousePlace.EIGHTH:   "The Sun in the 8th — identity expresses through depth, death, and others' resources. The native shines through what passes through their hands.",
        HousePlace.NINTH:    "The Sun rejoices in the 9th. Identity expresses through travel, philosophy, and the search for meaning; the native shines through learning and pilgrimage.",
        HousePlace.TENTH:    "The Sun in the 10th — identity expresses through public action and vocation. The native shines in their work and reputation.",
        HousePlace.ELEVENTH: "The Sun in the 11th — identity expresses through friends, alliances, and hopes. The native shines through the company that lifts them.",
        HousePlace.TWELFTH:  "The Sun in the 12th — identity is hidden and threatened by undoing. The native often shines from the dark, from solitude, or through hostile forces overcome.",
    },

    Planet.MOON: {
        HousePlace.FIRST:    "The Moon in the 1st — body and feeling are visible. The native carries their inner weather on the surface; presence is fluid and responsive.",
        HousePlace.SECOND:   "The Moon in the 2nd — body and feeling are bound to resources. Livelihood comes through what nurtures; emotional stability is tied to material flow.",
        HousePlace.THIRD:    "The Moon rejoices in the 3rd. Body and feeling are expressed in siblings, daily life, and movement; the native is fed by exchange.",
        HousePlace.FOURTH:   "The Moon in the 4th — body and feeling are rooted in home and ancestry. The native carries the mother in the body; private life is the seat of stability.",
        HousePlace.FIFTH:    "The Moon in the 5th — body and feeling are expressed through children, pleasure, and creative output. The native nurtures through play.",
        HousePlace.SIXTH:    "The Moon in the 6th — body and feeling are bound to labor and illness. The native serves through care of bodily life; health is the territory.",
        HousePlace.SEVENTH:  "The Moon in the 7th — body and feeling are expressed through partnership. The native nurtures and is nurtured by the significant other.",
        HousePlace.EIGHTH:   "The Moon in the 8th — body and feeling are drawn into depth and shared resources. Emotional life is fed by what is shared, hidden, or inherited.",
        HousePlace.NINTH:    "The Moon in the 9th — body and feeling are expressed through travel, philosophy, and foreign places. The native is fed by horizon.",
        HousePlace.TENTH:    "The Moon in the 10th — body and feeling are visible in public life. The native nurtures through work; emotional weather is legible to the world.",
        HousePlace.ELEVENTH: "The Moon in the 11th — body and feeling are expressed through friendship and chosen company. The native is fed by alliances.",
        HousePlace.TWELFTH:  "The Moon in the 12th — body and feeling withdraw into the hidden. The native's emotional life runs in private; isolation is a structural condition, not an accident.",
    },

    Planet.MERCURY: {
        HousePlace.FIRST:    "Mercury rejoices in the 1st. Speech, mind, and exchange are written directly on the body; the native is identified by their voice.",
        HousePlace.SECOND:   "Mercury in the 2nd — speech and mind are bound to livelihood. The native earns through communication and exchange.",
        HousePlace.THIRD:    "Mercury in the 3rd — speech and mind are expressed through siblings, neighbors, daily life. A natural communicator at the local level.",
        HousePlace.FOURTH:   "Mercury in the 4th — speech and mind are rooted in home and ancestry. The native's voice carries the family.",
        HousePlace.FIFTH:    "Mercury in the 5th — speech and mind are expressed through children, pleasure, and creative output. Wit becomes an erotic and creative currency.",
        HousePlace.SIXTH:    "Mercury in the 6th — speech and mind are bound to labor and service. The native works through skilled communication; health is bound up with mental life.",
        HousePlace.SEVENTH:  "Mercury in the 7th — speech and mind are expressed through partnership. The native is drawn to and challenged by other minds.",
        HousePlace.EIGHTH:   "Mercury in the 8th — speech and mind are drawn into depth, death, others' resources. The native's voice is investigative; they speak what others bury.",
        HousePlace.NINTH:    "Mercury in the 9th — speech and mind are expressed through travel, study, and philosophy. The native is a student or teacher of the larger frameworks.",
        HousePlace.TENTH:    "Mercury in the 10th — speech and mind are expressed in public action. The native is known for their voice; vocation is communication.",
        HousePlace.ELEVENTH: "Mercury in the 11th — speech and mind are expressed through friends and alliances. The native exchanges with their chosen company.",
        HousePlace.TWELFTH:  "Mercury in the 12th — speech and mind withdraw into hidden territory. The native's voice runs in solitude or in the dark — sometimes silenced, sometimes prophetic.",
    },

    Planet.VENUS: {
        HousePlace.FIRST:    "Venus in the 1st — beauty and love are written on the body. The native is graceful, attractive, and identified by their relationship to pleasure.",
        HousePlace.SECOND:   "Venus in the 2nd — beauty and love are bound to livelihood. The native earns through what they love; resources flow gracefully.",
        HousePlace.THIRD:    "Venus in the 3rd — beauty and love are expressed in siblings, neighbors, and daily life. The native makes daily life graceful.",
        HousePlace.FOURTH:   "Venus in the 4th — beauty and love are rooted in home and ancestry. The native's private life is the seat of beauty.",
        HousePlace.FIFTH:    "Venus rejoices in the 5th. Beauty and love flow through children, pleasure, and creative output; eros is at home here.",
        HousePlace.SIXTH:    "Venus in the 6th — beauty and love are bound to labor and service. The native loves through what they make and do for others.",
        HousePlace.SEVENTH:  "Venus in the 7th — beauty and love are expressed through partnership. The native finds their other in someone who carries Venus.",
        HousePlace.EIGHTH:   "Venus in the 8th — beauty and love are drawn into depth and shared resources. Eros runs through what is hidden and intimate.",
        HousePlace.NINTH:    "Venus in the 9th — beauty and love are expressed through travel, foreign places, and philosophy. The native loves across distance.",
        HousePlace.TENTH:    "Venus in the 10th — beauty and love are expressed in public life. The native's vocation is graceful, or carries Venusian themes.",
        HousePlace.ELEVENTH: "Venus in the 11th — beauty and love are expressed through friends and alliances. The native's chosen company is itself the source of grace.",
        HousePlace.TWELFTH:  "Venus in the 12th — beauty and love withdraw into the hidden. The native loves in private, in solitude, or for what cannot return the love.",
    },

    Planet.MARS: {
        HousePlace.FIRST:    "Mars in the 1st — drive and anger are written on the body. The native is forceful, direct, identified by their cutting edge.",
        HousePlace.SECOND:   "Mars in the 2nd — drive and anger are bound to livelihood. The native fights for resources; money comes through effort or contest.",
        HousePlace.THIRD:    "Mars in the 3rd — drive and anger are expressed through siblings, neighbors, and daily communication. Conflict in the local field.",
        HousePlace.FOURTH:   "Mars in the 4th — drive and anger are rooted in home and ancestry. The native may inherit conflict from the family or fight to claim the foundation.",
        HousePlace.FIFTH:    "Mars in the 5th — drive and anger are expressed through children, pleasure, and creative output. Eros is forceful; children may be contested.",
        HousePlace.SIXTH:    "Mars rejoices in the 6th. Drive flows through labor and service; the native works hard, and illness or injury are signatures of the place.",
        HousePlace.SEVENTH:  "Mars in the 7th — drive and anger are expressed through partnership. The native fights with or for the significant other.",
        HousePlace.EIGHTH:   "Mars in the 8th — drive and anger are drawn into depth and others' resources. Inheritance, intimacy, and death carry contest.",
        HousePlace.NINTH:    "Mars in the 9th — drive and anger are expressed through travel, philosophy, and foreign places. The native is a crusader.",
        HousePlace.TENTH:    "Mars in the 10th — drive and anger are expressed in public action. Career is contest; the native fights to be seen.",
        HousePlace.ELEVENTH: "Mars in the 11th — drive and anger are expressed through friends and alliances. Conflict in chosen company.",
        HousePlace.TWELFTH:  "Mars in the 12th — drive and anger withdraw into hidden territory. Self-undoing, hostile forces, internal warfare; the native often fights what cannot be seen.",
    },

    Planet.JUPITER: {
        HousePlace.FIRST:    "Jupiter in the 1st — expansion and good fortune are written on the body. The native is large in presence, often blessed, often lucky.",
        HousePlace.SECOND:   "Jupiter in the 2nd — expansion and good fortune in livelihood. Resources flow easily; the native is materially fortunate.",
        HousePlace.THIRD:    "Jupiter in the 3rd — expansion and good fortune in siblings, neighbors, and daily life. The native is gifted in local exchange and short journeys.",
        HousePlace.FOURTH:   "Jupiter in the 4th — expansion and good fortune in home and ancestry. The native inherits gift from the family or makes their home a place of generosity.",
        HousePlace.FIFTH:    "Jupiter in the 5th — expansion and good fortune in children, pleasure, and creative output. The native is fertile and generous in play.",
        HousePlace.SIXTH:    "Jupiter in the 6th — expansion and good fortune in labor and service. The native is gifted in skilled work; health benefits or excesses are signatures.",
        HousePlace.SEVENTH:  "Jupiter in the 7th — expansion and good fortune in partnership. The native is blessed by the significant other.",
        HousePlace.EIGHTH:   "Jupiter in the 8th — expansion and good fortune in depth and shared resources. Inheritance, intimacy, and transformation are productive.",
        HousePlace.NINTH:    "Jupiter in the 9th — expansion and good fortune in travel, philosophy, and foreign places. The native is gifted in the larger frameworks; pilgrimage is itself the work.",
        HousePlace.TENTH:    "Jupiter in the 10th — expansion and good fortune in public life. The native is gifted in their vocation, often visibly blessed.",
        HousePlace.ELEVENTH: "Jupiter rejoices in the 11th. Expansion and good fortune flow through friends, alliances, and hopes; the native is lifted by their company.",
        HousePlace.TWELFTH:  "Jupiter in the 12th — expansion and good fortune in hidden territory. The native is gifted in solitude, contemplation, or what undoes others — perhaps a hermetic or contemplative gift.",
    },

    Planet.SATURN: {
        HousePlace.FIRST:    "Saturn in the 1st — restriction and mastery are written on the body. The native is grave, structured, often older than their years; presence is austere.",
        HousePlace.SECOND:   "Saturn in the 2nd — restriction and mastery in livelihood. Resources come slowly and through effort; mastery of money is hard-earned.",
        HousePlace.THIRD:    "Saturn in the 3rd — restriction and mastery in siblings and daily life. The native's local field is austere; communication is careful.",
        HousePlace.FOURTH:   "Saturn in the 4th — restriction and mastery in home and ancestry. The native carries weight from the family — sometimes an absence, sometimes a burden.",
        HousePlace.FIFTH:    "Saturn in the 5th — restriction and mastery in children, pleasure, and creative output. Eros is restrained; the native may delay or restrict play.",
        HousePlace.SIXTH:    "Saturn in the 6th — restriction and mastery in labor and service. Hard work, chronic illness, or mastered craft are the territory.",
        HousePlace.SEVENTH:  "Saturn in the 7th — restriction and mastery in partnership. The significant other carries weight; relationship is built across time, often with elders or those carrying authority.",
        HousePlace.EIGHTH:   "Saturn in the 8th — restriction and mastery in depth and others' resources. The native masters what others fear; death, inheritance, and intimacy are domains of authority.",
        HousePlace.NINTH:    "Saturn in the 9th — restriction and mastery in travel, philosophy, foreign places. The native's worldview is hard-earned and structured.",
        HousePlace.TENTH:    "Saturn in the 10th — restriction and mastery in public life. The native builds career through patience; authority comes late but lasts.",
        HousePlace.ELEVENTH: "Saturn in the 11th — restriction and mastery in friends and alliances. The native's chosen company is limited but loyal.",
        HousePlace.TWELFTH:  "Saturn rejoices in the 12th. The native is at home with isolation, hidden things, and contemplative or hermetic work; suffering becomes a teacher.",
    },
}


def delineation(planet: Planet, place: HousePlace) -> str:
    return _TABLE.get(planet, {}).get(
        place,
        f"{planet.display_name} occupies the {place.value} place; its significations color the affairs of {place.topic.lower()}.",
    )
