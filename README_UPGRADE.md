Upgrade notes — Pelican modernisation

Steps to get a modern, reproducible environment:

1. Create and activate a virtual environment (macOS / zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Build the site locally:

```bash
make html
```

Notes:
- I removed the hard-coded `PLUGIN_PATHS` from `pelicanconf.py`; prefer installing plugins into the venv and adding their import names to `PLUGINS`.
- The Makefile now writes output to `docs/`, matching `OUTPUT_PATH` in `pelicanconf.py`.
- If you use a CJK spacing plugin, uncomment it in `requirements.txt`, install it, and add it to `PLUGINS`.

Next steps I can take for you (pick any):
- Install packages and run a build here (I will modify the environment).
- Add common plugins and enable CJK handling.
- Run the build and fix any errors that appear.
