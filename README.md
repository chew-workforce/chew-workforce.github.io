# chew-workforce.github.io

Static GitHub Pages site for the first public release of **Inference Dashboard**, a live publication on workforce demand, curriculum supply, and credential pathways.

## Structure

- `content/skillcurrent_publication_live.md`: primary editable source for the staged publication site.
- `content/skillcurrent_publication_draft.md`: original longer working draft retained as the baseline source.
- `scripts/build_site.py`: local generator that converts the markdown source into the publication pages and copies selected visual assets into the repo.
- `assets/site.css`: publication styling.
- `assets/site.js`: lightweight client-side interactions, including PNG zoom.
- `assets/viz/`: checked-in dashboard assets copied from the local analysis outputs.

## Rebuild

Run:

```bash
python3 scripts/build_site.py
```

The script regenerates the staged publication pages from `content/skillcurrent_publication_live.md` when present, and refreshes the copied visualization assets.

## Preview

Run:

```bash
bash scripts/serve_preview.sh
```

Then open `http://localhost:4173`.

## Push workflow

This clone is intended to avoid the shared macOS keychain GitHub credential. Use the local helper to push:

```bash
bash scripts/push_with_account.sh
```

Optional explicit account selection:

```bash
bash scripts/push_with_account.sh chew-workforce
```

If no account is provided, the script prompts for one and then runs an interactive HTTPS push with repository-local credential settings.
