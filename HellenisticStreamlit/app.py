"""Streamlit entrypoint for the Hellenistic Astrology web app.

Two screens:
1. Birth data entry → cast button.
2. Cast result: chart wheel + general analysis + topical advice (tabs).
"""
from __future__ import annotations
import sys
from datetime import date as date_cls, datetime, time as time_cls
from pathlib import Path

# Ensure project root is importable.
_PROJECT_ROOT = Path(__file__).resolve().parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

import streamlit as st

from analysis import general_analyzer, topical_analyzer
from analysis.topic_library import LifeTopic
from astrology import chart_calculator
from models.birth_data import BirthData
from ui.chart_wheel import render_svg
from ui.geocoding import geocode


st.set_page_config(
    page_title="Hellenistic Astrology — Chart Cast",
    page_icon="☉",
    layout="wide",
)


# ----- Session state -----

if "chart" not in st.session_state:
    st.session_state.chart = None
if "geocode" not in st.session_state:
    st.session_state.geocode = None
if "birth_data" not in st.session_state:
    st.session_state.birth_data = None


# ----- Sidebar: birth input -----

with st.sidebar:
    st.title("☉ Cast a chart")
    st.caption("Hellenistic-tradition natal chart. Whole-sign houses, sect, "
               "five-fold essential dignity, the seven Hermetic Lots.")

    name = st.text_input("Name (for display only)", value=st.session_state.get("name", ""))

    col_d, col_t = st.columns(2)
    with col_d:
        birth_date = st.date_input(
            "Birth date",
            value=st.session_state.get("birth_date", date_cls(1990, 1, 1)),
            min_value=date_cls(1800, 1, 1),
            max_value=date_cls(2100, 12, 31),
        )
    with col_t:
        birth_time = st.time_input(
            "Birth time (local)",
            value=st.session_state.get("birth_time", time_cls(12, 0)),
            step=60,
        )

    place_input = st.text_input(
        "Birth place (city, country)",
        value=st.session_state.get("place_input", ""),
        placeholder="e.g. Quebec City, Canada",
    )

    if st.button("Look up location", use_container_width=True, disabled=not place_input):
        with st.spinner("Geocoding..."):
            result = geocode(place_input)
        if result is None:
            st.error("Couldn't find that place. Try adding the country.")
        else:
            st.session_state.geocode = result
            st.session_state.place_input = place_input

    if st.session_state.geocode is not None:
        g = st.session_state.geocode
        st.info(
            f"📍 **{g.place_name}**\n\n"
            f"{g.latitude:.4f}°N, {g.longitude:.4f}°E\n\n"
            f"Time zone: `{g.tz_id}`"
        )

    cast_disabled = st.session_state.geocode is None
    if st.button("Cast chart", type="primary", use_container_width=True, disabled=cast_disabled):
        g = st.session_state.geocode
        bd = BirthData(
            name=name or "Unnamed native",
            local_birth_moment=datetime.combine(birth_date, birth_time),
            tz_id=g.tz_id,
            latitude=g.latitude,
            longitude=g.longitude,
            place_name=g.place_name,
        )
        st.session_state.birth_data = bd
        st.session_state.chart = chart_calculator.cast(bd)
        # Persist user inputs.
        st.session_state.name = name
        st.session_state.birth_date = birth_date
        st.session_state.birth_time = birth_time

    st.markdown("---")
    st.caption(
        "Doctrine cross-referenced against Brennan, *Hellenistic Astrology*; "
        "George, *AATP* I & II; Avelar & Ribeiro, *On the Heavenly Spheres*; "
        "Nicholas, *You Were Born for This*."
    )


# ----- Main area -----

chart = st.session_state.chart
bd = st.session_state.birth_data

if chart is None:
    st.title("Hellenistic Astrology")
    st.markdown(
        """
        A Hellenistic-tradition natal chart app — whole-sign houses, sect-aware
        delineation, the five-fold essential dignity system, Ptolemaic aspects,
        and the seven Hermetic Lots of the planets.

        **To begin:** enter a birth date, time, and place in the sidebar,
        then click *Look up location* and *Cast chart*.

        The interpretive voice draws on Chris Brennan's *Hellenistic Astrology*,
        Demetra George's *Ancient Astrology in Theory and Practice* (Vols I & II)
        and *Astrology and the Authentic Self*, Avelar & Ribeiro's *On the
        Heavenly Spheres*, and Chani Nicholas's *You Were Born for This*.
        """
    )
    st.info(
        "Try the test native to see the output: **June 24 1993, 14:36, Quebec City, Canada.** "
        "Day chart, Libra Ascendant 22.84°, Venus domicile in Taurus 8th, "
        "Mars-Saturn partile opposition at 0.68°."
    )
else:
    analysis = general_analyzer.analyze(chart)

    st.title(f"{bd.name}'s Chart")
    st.caption(
        f"{bd.local_birth_moment.strftime('%B %-d, %Y at %-I:%M %p')} "
        f"({bd.tz_id}) — {bd.place_name}"
    )

    # ---- Chart wheel + key facts side-by-side ----
    wheel_col, facts_col = st.columns([3, 2])
    with wheel_col:
        st.markdown(render_svg(chart), unsafe_allow_html=True)
    with facts_col:
        st.markdown("### Key Facts")
        asc_deg = chart.ascendant_longitude % 30
        mc_deg = chart.midheaven_longitude % 30
        st.markdown(
            f"**Ascendant:** {chart.ascendant_sign.display_name} {asc_deg:.2f}°  \n"
            f"**Midheaven:** {chart.midheaven_sign.display_name} {mc_deg:.2f}°  \n"
            f"**Sect:** {chart.sect.value.capitalize()}  \n"
            f"**Sect light:** {analysis.sect_report.sect_light.display_name}  \n"
            f"**Benefic of sect:** {analysis.sect_report.benefic.display_name}  \n"
            f"**Malefic contrary to sect:** {analysis.sect_report.malefic.display_name}"
        )
        st.markdown("---")
        st.markdown("### Positions")
        for p in chart.positions:
            house = chart.house_place_for_sign(p.sign).value
            retro = " ℞" if p.is_retrograde else ""
            st.markdown(
                f"{p.planet.glyph} **{p.planet.display_name}** "
                f"— {p.sign.display_name} {p.sign_degree:.2f}°{retro} (house {house})"
            )

    # ---- Tabs: Reading Guide, General Analysis, Lots, Topical Advice ----
    tab_guide, tab_analysis, tab_lots, tab_topical = st.tabs(
        ["📖 Reading Guide", "🔭 General Analysis", "✦ Lots", "🎯 Topical Advice"]
    )

    with tab_guide:
        st.markdown(analysis.glossary)

    with tab_analysis:
        st.markdown(analysis.summary)
        st.markdown("---")
        st.markdown("**III. Per-planet readings**")
        for r in analysis.planet_readings:
            with st.expander(
                f"{r.planet.glyph} {r.planet.display_name} — "
                f"{r.sign.display_name}, {r.house.value}th house (dignity {r.dignity_score:+d})",
                expanded=False,
            ):
                st.markdown(r.paragraph)
        st.markdown("---")
        st.markdown("**IV. Aspects**")
        for ar in analysis.aspect_readings:
            tag = "💥" if ar.aspect.is_partile else "·"
            st.markdown(
                f"{tag} **{ar.aspect.first.display_name} {ar.aspect.kind.value} "
                f"{ar.aspect.second.display_name}** — {ar.paragraph}"
            )
        st.markdown("---")
        st.markdown(analysis.structural_narrative)
        st.markdown("---")
        st.markdown("**V. Activating the Strengths**")
        for note in analysis.positive_highlights:
            st.markdown(note)
            st.markdown("")
        st.markdown("**VI. Working with the Challenges**")
        for note in analysis.negative_highlights:
            st.markdown(note)
            st.markdown("")

    with tab_lots:
        st.markdown("### The 7 Hermetic Lots")
        st.caption("Sensitive points marking specific life themes (Brennan Ch. 17).")
        for row in analysis.lot_table:
            st.markdown(row)
        st.markdown("---")
        for lr in analysis.lot_readings:
            with st.expander(
                f"{lr.lot.display_name} — {lr.sign.display_name} "
                f"({lr.house.value}th house)",
                expanded=False,
            ):
                st.markdown(lr.paragraph)

    with tab_topical:
        st.markdown("### Topical Advice")
        st.caption(
            "Per-topic readings: the topical house, its ruler's placement, and "
            "(where applicable) the topic's natural significator."
        )
        for advice in topical_analyzer.analyze_all(chart):
            with st.expander(advice.topic.headline, expanded=False):
                st.markdown(advice.paragraph)
