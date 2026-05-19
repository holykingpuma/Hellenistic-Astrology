"""SVG chart wheel — whole-sign houses, angular cusps bolded, ASC at 9 o'clock.

Mirrors the iOS ChartWheelView layout:
- Cusp lines extend from the outer rim to a small central margin so house
  numbers sit in a visually-bounded band.
- Angular cusps (1, 4, 7, 10) are drawn with a thicker stroke.
- An 'ASC →' indicator sits on the outer rim at the 9 o'clock position.
- Planet markers are placed forward inside their sector by degree fraction.
"""
from __future__ import annotations
from math import cos, pi, sin

from models.lot import HermeticLotPosition
from models.natal_chart import NatalChart
from models.planet import PlanetaryPosition
from models.zodiac import ZodiacSign


# Geometry constants.
SIZE = 560
CX = CY = SIZE / 2
R_OUTER = 260
R_SIGN_RING = 230     # ring where sign glyphs sit
R_HOUSE_NUM = 90      # ring where house numbers sit
R_INNER = 60          # inner margin for cusp lines
R_PLANET = 165        # ring where planet markers sit
R_LOT = 195           # ring where lot markers sit


def _angle_for_longitude(longitude: float, asc_longitude: float) -> float:
    """Astrology convention: Ascendant on the left (180° in SVG terms), zodiac
    runs counterclockwise. Return the SVG angle (radians) where this longitude sits.
    """
    # Degrees counterclockwise from the Ascendant.
    delta = (longitude - asc_longitude) % 360.0
    # SVG: 0° is east (3 o'clock), goes clockwise. We want 180° in SVG = Asc.
    # Counterclockwise in math, so we subtract from 180°.
    return (180.0 - delta) * pi / 180.0


def _point_on(radius: float, angle_rad: float) -> tuple[float, float]:
    # SVG y is flipped (positive = down), so we negate sin to get math convention.
    return CX + radius * cos(angle_rad), CY - radius * sin(angle_rad)


def render_svg(chart: NatalChart) -> str:
    asc_long = chart.ascendant_longitude
    elements: list[str] = []

    # Outer ring
    elements.append(
        f'<circle cx="{CX}" cy="{CY}" r="{R_OUTER}" fill="#fbf8f3" stroke="#8a7a55" stroke-width="2"/>'
    )
    elements.append(
        f'<circle cx="{CX}" cy="{CY}" r="{R_SIGN_RING}" fill="none" stroke="#c4b58d" stroke-width="1"/>'
    )
    elements.append(
        f'<circle cx="{CX}" cy="{CY}" r="{R_INNER}" fill="none" stroke="#c4b58d" stroke-width="1"/>'
    )

    # House cusps — 12 evenly-spaced lines starting at the Ascendant.
    # The 1st house cusp = the Ascendant. Subsequent cusps every 30° in
    # whole-sign order, but they line up with sign boundaries.
    asc_sign = chart.ascendant_sign
    for i in range(12):
        sign = asc_sign.advanced(i)
        cusp_longitude = float(int(sign) * 30)  # boundary of the sign
        angle = _angle_for_longitude(cusp_longitude, asc_long)
        x1, y1 = _point_on(R_INNER, angle)
        x2, y2 = _point_on(R_OUTER, angle)
        place_num = i + 1
        is_angular = place_num in (1, 4, 7, 10)
        stroke_width = 2.0 if is_angular else 1.0
        stroke_color = "#5a4f3a" if is_angular else "#a09372"
        elements.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke_color}" stroke-width="{stroke_width}"/>'
        )

        # Sign glyph at the middle of each sign sector.
        mid_long = cusp_longitude + 15.0
        mid_angle = _angle_for_longitude(mid_long, asc_long)
        sx, sy = _point_on(R_SIGN_RING - 12, mid_angle)
        elements.append(
            f'<text x="{sx:.1f}" y="{sy:.1f}" text-anchor="middle" '
            f'dominant-baseline="middle" font-size="20" fill="#4a3f2a">{sign.glyph}</text>'
        )

        # House number — same midpoint, smaller radius.
        hx, hy = _point_on(R_HOUSE_NUM, mid_angle)
        elements.append(
            f'<text x="{hx:.1f}" y="{hy:.1f}" text-anchor="middle" '
            f'dominant-baseline="middle" font-size="14" fill="#8a7a55" '
            f'font-weight="{("bold" if is_angular else "normal")}">{place_num}</text>'
        )

    # ASC → indicator at 9 o'clock (the Ascendant marker).
    elements.append(
        f'<text x="{CX - R_OUTER - 16}" y="{CY}" text-anchor="end" '
        f'dominant-baseline="middle" font-size="14" font-weight="bold" '
        f'fill="#5a4f3a">ASC →</text>'
    )

    # Planet markers — placed by exact longitude (degree fraction inside sector).
    # Group by sector to spread out conjuncts.
    sector_map: dict[int, list[PlanetaryPosition]] = {}
    for p in chart.positions:
        sector_map.setdefault(int(p.longitude / 30), []).append(p)

    for sector, ps in sector_map.items():
        ps_sorted = sorted(ps, key=lambda p: p.longitude)
        for offset_idx, p in enumerate(ps_sorted):
            r = R_PLANET - (offset_idx % 3) * 18  # ladder conjuncts inward
            angle = _angle_for_longitude(p.longitude, asc_long)
            x, y = _point_on(r, angle)
            retro_mark = "ᴿ" if p.is_retrograde else ""
            elements.append(
                f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" '
                f'dominant-baseline="middle" font-size="20" '
                f'fill="#2a2018">{p.planet.glyph}{retro_mark}</text>'
            )

    # Lots — small markers in their own ring, monochrome.
    lot_sector_map: dict[int, list[HermeticLotPosition]] = {}
    for lot in chart.lots:
        lot_sector_map.setdefault(int(lot.longitude / 30), []).append(lot)
    for sector, lots in lot_sector_map.items():
        lots_sorted = sorted(lots, key=lambda l: l.longitude)
        for offset_idx, lot in enumerate(lots_sorted):
            r = R_LOT - (offset_idx % 3) * 12
            angle = _angle_for_longitude(lot.longitude, asc_long)
            x, y = _point_on(r, angle)
            label = lot.kind.display_name.replace("Lot of ", "")[0]  # F, S, E, N, C, V, ...
            elements.append(
                f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" '
                f'dominant-baseline="middle" font-size="11" '
                f'fill="#7a6a45" font-style="italic">{label}</text>'
            )

    body = "\n".join(elements)
    return (
        f'<svg viewBox="0 0 {SIZE} {SIZE}" xmlns="http://www.w3.org/2000/svg" '
        f'width="100%" style="max-width:560px;display:block;margin:0 auto;">\n{body}\n</svg>'
    )
