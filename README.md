# chew-workforce.github.io

Static GitHub Pages site for the first public release of **SkillCurrent**, a live publication on workforce demand, curriculum supply, and credential pathways.

## Structure

- `content/skillcurrent_publication_draft.md`: primary source narrative for the publication.
- `scripts/build_site.py`: local generator that converts the markdown draft into section pages and copies selected visual assets into the repo.
- `assets/site.css`: site styling.
- `assets/viz/`: checked-in dashboard assets copied from the local analysis outputs.

## Rebuild

Run:

```bash
python3 scripts/build_site.py
```

The script regenerates `index.html`, the section pages, `dashboard.html`, and refreshes the copied visualization assets.

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
