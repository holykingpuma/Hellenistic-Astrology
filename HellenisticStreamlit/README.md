# Hellenistic Astrology — Streamlit web version

Web port of the iOS Hellenistic Astrology app for cross-platform user testing.
Same calculation engine (Swiss Ephemeris via `pyswisseph`), same Hellenistic
doctrine (whole-sign houses, sect, five-fold essential dignity, Ptolemaic
aspects, seven Hermetic Lots), same source-grounded delineation prose.

## Local run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Open http://localhost:8501 in any browser.

## Deploy to testers

The fastest path is Streamlit Community Cloud (free):
1. Push this folder to a GitHub repo.
2. At https://share.streamlit.io connect the repo, point at `app.py`.
3. Share the public URL with testers.

## Validation native

The test chart used to verify output parity with the iOS app:
- June 24 1993, 14:36 EDT, Quebec City (46.81°N, 71.21°W)
- Expected: Libra Asc 22.84°, Cancer Sun 3.24° (10th), Virgo Moon 4.34° (12th),
  Cancer Mercury 26.46° (10th), Taurus Venus 18.11° (8th — domicile),
  Virgo Mars 0.84° (12th), Libra Jupiter 5.58° (1st), Pisces Saturn 0.16° R (6th)
- Day chart; Mars-Saturn partile opposition (0.68° from exact)

## Source texts

Doctrine cross-referenced against:
- Brennan, *Hellenistic Astrology* (primary canonical reference)
- George, *Ancient Astrology in Theory and Practice* Vols I & II
- George, *Astrology and the Authentic Self*
- Avelar & Ribeiro, *On the Heavenly Spheres*
- Nicholas, *You Were Born for This* (accessible voice)

Citation conventions used inline in delineation prose:
HA = Brennan; AATP I/II = George manuals; AAS = George (Authentic Self);
OHS = Avelar & Ribeiro; YBFT = Nicholas.
