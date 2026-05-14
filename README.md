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
