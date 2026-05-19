# Deploying for user testing

The fastest path to a shareable URL is **Streamlit Community Cloud** — free,
GitHub-backed, and built for this exact use case.

## Step 1 — Run locally first

```bash
cd HellenisticStreamlit
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 tests/test_validation.py   # should print "All validation tests passed."
streamlit run app.py
```

Open http://localhost:8501. Cast the test native (June 24 1993, 14:36,
Quebec City, Canada) to confirm the output matches the iOS app.

## Step 2 — Push to GitHub

Create a new repo (private or public — Streamlit Community Cloud supports
both). The HellenisticStreamlit folder is the deployment root.

```bash
cd HellenisticStreamlit
git init
git add .
git commit -m "Hellenistic Astrology — Streamlit MVP"
git branch -M main
git remote add origin git@github.com:YOUR_USERNAME/hellenistic-streamlit.git
git push -u origin main
```

## Step 3 — Deploy on Streamlit Community Cloud

1. Go to https://share.streamlit.io/ and sign in with GitHub.
2. Click **New app**.
3. Repo: pick the repo from step 2.
4. Branch: `main`.
5. Main file path: `app.py`.
6. Click **Deploy**.

First build takes ~2–3 minutes (it installs pyswisseph, which compiles
native code). After that, you'll have a public URL like
`https://your-app-name.streamlit.app`.

## Step 4 — Share with testers

Just send the URL. No accounts needed — anyone with the link can cast a
chart. If you want a private beta, set the repo to private and use
Streamlit Cloud's "Viewer access" controls under app settings.

## What testers will see

- A sidebar for entering name, birth date, birth time, and place.
- Free geocoding via OpenStreetMap (Nominatim) → automatic time zone resolution.
- A chart wheel rendered inline, plus a "Key Facts" panel (Asc/MC/sect/sect light).
- Four tabs: Reading Guide, General Analysis, Lots, Topical Advice — same
  structure and prose voice as the iOS app.

## When you're ready to leave Streamlit

When user testing tells you the output is worth productizing, you'll have
two paths:

1. **Keep the Python engine, rebuild the UI.** Wrap `astrology/` + `analysis/`
   in a FastAPI backend. Build a Next.js or SvelteKit frontend on top.
   Deploy backend on Render or Fly.io, frontend on Vercel.

2. **Compile the engine to WebAssembly.** Possible with pyodide, but
   browser-side pyswisseph is heavy. Probably not worth it unless you
   want an offline PWA.

Most realistic next step from here: a Next.js + Supabase rewrite of the UI,
with this Python service kept as the calculation API. That preserves your
investment in delineation prose while giving you accounts, saved charts,
and a polished web product.
