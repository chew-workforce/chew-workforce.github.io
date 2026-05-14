#!/usr/bin/env python3

from __future__ import annotations

import html
import os
import re
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTENT_PATH = REPO_ROOT / "content" / "skillcurrent_publication_draft.md"
SITE_ASSETS = REPO_ROOT / "assets"
VIZ_ROOT = SITE_ASSETS / "viz"

SOURCE_ASSETS = {
    "jd": {
        "05_hierarchy_sunburst.html": Path(
            "../../jd_to_skills/viz_outputs/05_hierarchy_sunburst.html"
        ),
        "06_granular_canonical_family_sankey.html": Path(
            "../../jd_to_skills/viz_outputs/06_granular_canonical_family_sankey.html"
        ),
        "08_evidence_family_sunburst.html": Path(
            "../../jd_to_skills/viz_outputs/08_evidence_family_sunburst.html"
        ),
        "10_skill_combination_hierarchy.html": Path(
            "../../jd_to_skills/viz_outputs/10_skill_combination_hierarchy.html"
        ),
        "01_canonical_demand_by_tier.png": Path(
            "../../jd_to_skills/viz_outputs/01_canonical_demand_by_tier.png"
        ),
        "04_demand_signal_scatter.png": Path(
            "../../jd_to_skills/viz_outputs/04_demand_signal_scatter.png"
        ),
    },
    "curriculum": {
        "02_sunburst_skill_family_canonical_granular.html": Path(
            "../../curriculum_to_skills/viz_outputs_passBCD_v2_20260324_012657/02_sunburst_skill_family_canonical_granular.html"
        ),
        "03_canonical_skill_x_instruction_mode.png": Path(
            "../../curriculum_to_skills/viz_outputs_passBCD_v2_20260324_012657/03_canonical_skill_x_instruction_mode.png"
        ),
        "04_ranked_canonical_skill_support.png": Path(
            "../../curriculum_to_skills/viz_outputs_passBCD_v2_20260324_012657/04_ranked_canonical_skill_support.png"
        ),
        "01_alluvial_machine_operations.png": Path(
            "../../curriculum_to_skills/viz_outputs_passBCD_v2_20260324_012657/01_alluvial_machine_operations.png"
        ),
        "01_alluvial_precision_measurement.png": Path(
            "../../curriculum_to_skills/viz_outputs_passBCD_v2_20260324_012657/01_alluvial_precision_measurement.png"
        ),
        "01_alluvial_gd_t.png": Path(
            "../../curriculum_to_skills/viz_outputs_passBCD_v2_20260324_012657/01_alluvial_gd_t.png"
        ),
    },
}

NAV_ITEMS = [
    ("Home", "index.html"),
    ("1. Premise", "premise.html"),
    ("2. Opportunity Gap", "opportunity-gap.html"),
    ("3. Approach", "approach.html"),
    ("4. Results", "results.html"),
    ("Dashboard", "dashboard.html"),
    ("5. Implications", "implications.html"),
    ("6. Methodology", "methodology.html"),
    ("7. Site Structure", "site-structure.html"),
    ("8. Overclaim", "overclaim.html"),
    ("9. Work Plan", "work-plan.html"),
    ("References", "references.html"),
]

SECTION_SLUGS = {
    "1. The premise": "premise.html",
    "2. The opportunity gap": "opportunity-gap.html",
    "3. The approach: a live, local, evidence-first skill inference platform": "approach.html",
    "4. Results": "results.html",
    "5. Implications": "implications.html",
    "6. Methodology": "methodology.html",
    "7. Recommended GitHub Pages structure": "site-structure.html",
    "8. What not to overclaim": "overclaim.html",
    "9. Near-term work plan": "work-plan.html",
    "References": "references.html",
}

RESULTS_INSERT = """
<section class="feature-grid">
  <article class="feature-card">
    <p class="eyebrow">Demand Signal</p>
    <h3>Canonical demand hierarchy</h3>
    <p>Employer-demand structure from the job-description pipeline, embedded as an interactive hierarchy.</p>
    <iframe src="assets/viz/jd/05_hierarchy_sunburst.html" title="Job demand hierarchy sunburst" loading="lazy"></iframe>
  </article>
  <article class="feature-card">
    <p class="eyebrow">Translation Layer</p>
    <h3>Granular to canonical sankey</h3>
    <p>The Sankey view shows how extracted phrasing is consolidated into canonical skills and broader families.</p>
    <iframe src="assets/viz/jd/06_granular_canonical_family_sankey.html" title="Granular to canonical skill sankey" loading="lazy"></iframe>
  </article>
</section>
<section class="figure-grid">
  <figure class="figure-card">
    <img src="assets/viz/jd/01_canonical_demand_by_tier.png" alt="Canonical demand by employer tier" loading="lazy" />
    <figcaption>Demand concentration by employer tier.</figcaption>
  </figure>
  <figure class="figure-card">
    <img src="assets/viz/jd/04_demand_signal_scatter.png" alt="Demand signal scatter plot" loading="lazy" />
    <figcaption>Demand intensity plotted against supporting evidence.</figcaption>
  </figure>
  <figure class="figure-card">
    <img src="assets/viz/curriculum/03_canonical_skill_x_instruction_mode.png" alt="Instruction mode heatmap" loading="lazy" />
    <figcaption>Curriculum instruction-depth evidence by canonical skill.</figcaption>
  </figure>
  <figure class="figure-card">
    <img src="assets/viz/curriculum/04_ranked_canonical_skill_support.png" alt="Curriculum ranked canonical support" loading="lazy" />
    <figcaption>Relative curriculum support across canonical skills.</figcaption>
  </figure>
</section>
"""

DASHBOARD_BODY = """
<section class="hero compact">
  <div class="hero-copy">
    <p class="eyebrow">Interactive Dashboard</p>
    <h1>SkillCurrent visual evidence</h1>
    <p class="lede">This first release uses existing job-description and curriculum visual outputs as the live public-facing layer while the aggregate public data schema is finalized.</p>
  </div>
</section>

<section class="dashboard-grid">
  <article class="feature-card">
    <p class="eyebrow">Jobs</p>
    <h2>Hierarchy sunburst</h2>
    <iframe src="assets/viz/jd/05_hierarchy_sunburst.html" title="Job hierarchy sunburst" loading="lazy"></iframe>
  </article>
  <article class="feature-card">
    <p class="eyebrow">Jobs</p>
    <h2>Granular to canonical sankey</h2>
    <iframe src="assets/viz/jd/06_granular_canonical_family_sankey.html" title="Job granular to canonical sankey" loading="lazy"></iframe>
  </article>
  <article class="feature-card">
    <p class="eyebrow">Jobs</p>
    <h2>Evidence family sunburst</h2>
    <iframe src="assets/viz/jd/08_evidence_family_sunburst.html" title="Job evidence family sunburst" loading="lazy"></iframe>
  </article>
  <article class="feature-card">
    <p class="eyebrow">Jobs</p>
    <h2>Skill combination hierarchy</h2>
    <iframe src="assets/viz/jd/10_skill_combination_hierarchy.html" title="Job skill combination hierarchy" loading="lazy"></iframe>
  </article>
  <article class="feature-card">
    <p class="eyebrow">Curriculum</p>
    <h2>Curriculum hierarchy sunburst</h2>
    <iframe src="assets/viz/curriculum/02_sunburst_skill_family_canonical_granular.html" title="Curriculum hierarchy sunburst" loading="lazy"></iframe>
  </article>
  <article class="feature-card">
    <p class="eyebrow">Curriculum</p>
    <h2>Instruction-depth evidence</h2>
    <img src="assets/viz/curriculum/03_canonical_skill_x_instruction_mode.png" alt="Instruction-depth evidence heatmap" loading="lazy" />
  </article>
  <article class="feature-card">
    <p class="eyebrow">Curriculum</p>
    <h2>Machine operations alluvial</h2>
    <img src="assets/viz/curriculum/01_alluvial_machine_operations.png" alt="Machine operations alluvial chart" loading="lazy" />
  </article>
  <article class="feature-card">
    <p class="eyebrow">Curriculum</p>
    <h2>Precision measurement alluvial</h2>
    <img src="assets/viz/curriculum/01_alluvial_precision_measurement.png" alt="Precision measurement alluvial chart" loading="lazy" />
  </article>
  <article class="feature-card">
    <p class="eyebrow">Curriculum</p>
    <h2>GD&amp;T alluvial</h2>
    <img src="assets/viz/curriculum/01_alluvial_gd_t.png" alt="GD&T alluvial chart" loading="lazy" />
  </article>
</section>
"""


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    _, rest = text.split("---\n", 1)
    raw_meta, body = rest.split("\n---\n", 1)
    meta = {}
    for line in raw_meta.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"')
    return meta, body.lstrip()


def split_top_sections(text: str) -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    current_title = None
    current_lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("# "):
            if current_title is not None:
                sections.append((current_title, "\n".join(current_lines).strip()))
            current_title = line[2:].strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_title is not None:
        sections.append((current_title, "\n".join(current_lines).strip()))
    return sections


def slugify(text: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return cleaned or "section"


def format_inline(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    escaped = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>',
        escaped,
    )
    escaped = re.sub(
        r"\[\^([^\]]+)\]",
        lambda m: f'<sup class="footnote-ref">{html.escape(m.group(1))}</sup>',
        escaped,
    )
    return escaped.replace("&lt;br&gt;", "<br>")


def consume_table(lines: list[str], start: int) -> tuple[str, int]:
    header = [cell.strip() for cell in lines[start].strip().strip("|").split("|")]
    idx = start + 2
    rows = []
    while idx < len(lines) and "|" in lines[idx] and lines[idx].strip():
        rows.append([cell.strip() for cell in lines[idx].strip().strip("|").split("|")])
        idx += 1
    thead = "".join(f"<th>{format_inline(cell)}</th>" for cell in header)
    body_rows = []
    for row in rows:
        cells = "".join(f"<td>{format_inline(cell)}</td>" for cell in row)
        body_rows.append(f"<tr>{cells}</tr>")
    table = (
        '<div class="table-wrap"><table><thead><tr>'
        + thead
        + "</tr></thead><tbody>"
        + "".join(body_rows)
        + "</tbody></table></div>"
    )
    return table, idx


def markdown_to_html(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    paragraph: list[str] = []
    in_code = False
    code_lang = ""
    list_mode: str | None = None
    blockquote_mode = False

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            out.append(f"<p>{format_inline(' '.join(paragraph).strip())}</p>")
            paragraph = []

    def close_list() -> None:
        nonlocal list_mode
        if list_mode is not None:
            out.append(f"</{list_mode}>")
            list_mode = None

    def close_blockquote() -> None:
        nonlocal blockquote_mode
        if blockquote_mode:
            flush_paragraph()
            out.append("</blockquote>")
            blockquote_mode = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            close_blockquote()
            close_list()
            flush_paragraph()
            if not in_code:
                in_code = True
                code_lang = stripped[3:].strip()
                out.append(f'<pre><code class="language-{html.escape(code_lang)}">')
            else:
                out.append("</code></pre>")
                in_code = False
                code_lang = ""
            i += 1
            continue

        if in_code:
            out.append(html.escape(line))
            i += 1
            continue

        if re.match(r"^\|.+\|$", stripped) and i + 1 < len(lines) and re.match(
            r"^\|?[\-\s:|]+\|?$", lines[i + 1].strip()
        ):
            close_blockquote()
            close_list()
            flush_paragraph()
            table_html, i = consume_table(lines, i)
            out.append(table_html)
            continue

        if not stripped:
            close_blockquote()
            close_list()
            flush_paragraph()
            i += 1
            continue

        if stripped == "---":
            close_blockquote()
            close_list()
            flush_paragraph()
            out.append("<hr />")
            i += 1
            continue

        if stripped.startswith("### "):
            close_blockquote()
            close_list()
            flush_paragraph()
            out.append(f'<h3 id="{slugify(stripped[4:])}">{format_inline(stripped[4:])}</h3>')
            i += 1
            continue

        if stripped.startswith("## "):
            close_blockquote()
            close_list()
            flush_paragraph()
            out.append(f'<h2 id="{slugify(stripped[3:])}">{format_inline(stripped[3:])}</h2>')
            i += 1
            continue

        ordered = re.match(r"^(\d+)\.\s+(.*)$", stripped)
        unordered = re.match(r"^-\s+(.*)$", stripped)
        reference = re.match(r"^\[\^([^\]]+)\]:\s+(.*)$", stripped)
        quote = re.match(r"^>\s?(.*)$", stripped)

        if ordered:
            close_blockquote()
            flush_paragraph()
            if list_mode != "ol":
                close_list()
                out.append("<ol>")
                list_mode = "ol"
            out.append(f"<li>{format_inline(ordered.group(2))}</li>")
            i += 1
            continue

        if unordered:
            close_blockquote()
            flush_paragraph()
            if list_mode != "ul":
                close_list()
                out.append("<ul>")
                list_mode = "ul"
            out.append(f"<li>{format_inline(unordered.group(1))}</li>")
            i += 1
            continue

        if reference:
            close_blockquote()
            close_list()
            flush_paragraph()
            out.append(
                '<div class="reference-item">'
                f'<span class="reference-key">{html.escape(reference.group(1))}</span>'
                f"<p>{format_inline(reference.group(2))}</p>"
                "</div>"
            )
            i += 1
            continue

        if quote:
            close_list()
            flush_paragraph()
            if not blockquote_mode:
                out.append("<blockquote>")
                blockquote_mode = True
            paragraph.append(quote.group(1))
            i += 1
            continue

        paragraph.append(stripped)
        i += 1

    close_blockquote()
    close_list()
    flush_paragraph()
    return "\n".join(out)


def copy_viz_assets() -> None:
    for group, files in SOURCE_ASSETS.items():
        dest_dir = VIZ_ROOT / group
        dest_dir.mkdir(parents=True, exist_ok=True)
        for name, relative_source in files.items():
            source = (REPO_ROOT / relative_source).resolve()
            if not source.exists():
                raise FileNotFoundError(f"Missing visualization asset: {source}")
            shutil.copy2(source, dest_dir / name)


def render_nav(active_file: str) -> str:
    parts = ['<nav class="site-nav" aria-label="Primary">']
    for label, href in NAV_ITEMS:
        active = ' class="active"' if href == active_file else ""
        parts.append(f'<a href="{href}"{active}>{html.escape(label)}</a>')
    parts.append("</nav>")
    return "".join(parts)


def page_template(meta: dict[str, str], page_title: str, active_file: str, body: str) -> str:
    title = f"{page_title} | SkillCurrent"
    nav = render_nav(active_file)
    subtitle = meta.get("subtitle", "")
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(subtitle)}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,500;6..72,700&family=Space+Grotesk:wght@400;500;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/site.css" />
</head>
<body>
  <div class="site-shell">
    <header class="site-header">
      <a class="brand" href="index.html">SkillCurrent</a>
      <div class="header-meta">
        <span>{html.escape(meta.get("status", ""))}</span>
        <span>Updated {html.escape(meta.get("last_updated", ""))}</span>
      </div>
      {nav}
    </header>
    <main class="page-content">
      {body}
    </main>
  </div>
</body>
</html>
"""


def build_home(meta: dict[str, str], sections: list[tuple[str, str]]) -> str:
    content_map = {title: body for title, body in sections}
    recommended = markdown_to_html(
        content_map.get("SkillCurrent: A Unified Language Layer for Workforce Development", "")
    )
    abstract = markdown_to_html(content_map.get("Publication abstract", ""))
    cards = []
    for title, href in NAV_ITEMS[1:10]:
        cards.append(
            f'<a class="nav-card" href="{href}"><span>{html.escape(title)}</span><strong>Open page</strong></a>'
        )
    body = f"""
<section class="hero">
  <div class="hero-copy">
    <p class="eyebrow">{html.escape(meta.get("author", ""))}</p>
    <h1>{html.escape(meta.get("title", "SkillCurrent"))}</h1>
    <p class="lede">{html.escape(meta.get("subtitle", ""))}</p>
  </div>
  <div class="hero-panel">
    <p class="eyebrow">Live publication</p>
    <p>This repository is the first deployable public shell for the workforce-to-credentials research program. It combines narrative sections with embedded demand-side and curriculum-side visual evidence.</p>
    <a class="cta" href="dashboard.html">Open dashboard views</a>
  </div>
</section>

<section class="content-block">
  <div class="section-label">Project naming</div>
  {recommended}
</section>

<section class="content-block">
  <div class="section-label">Abstract</div>
  {abstract}
</section>

<section class="content-block">
  <div class="section-label">Navigate the publication</div>
  <div class="nav-card-grid">
    {"".join(cards)}
  </div>
</section>

<section class="feature-grid">
  <article class="feature-card">
    <p class="eyebrow">Interactive evidence</p>
    <h3>Job-description demand hierarchy</h3>
    <iframe src="assets/viz/jd/05_hierarchy_sunburst.html" title="Job demand hierarchy" loading="lazy"></iframe>
  </article>
  <article class="feature-card">
    <p class="eyebrow">Curriculum evidence</p>
    <h3>Curriculum skill hierarchy</h3>
    <iframe src="assets/viz/curriculum/02_sunburst_skill_family_canonical_granular.html" title="Curriculum hierarchy" loading="lazy"></iframe>
  </article>
</section>
"""
    return page_template(meta, "Home", "index.html", body)


def build_section_page(meta: dict[str, str], title: str, body_md: str, filename: str) -> str:
    page_heading = re.sub(r"^\d+\.\s*", "", title)
    section_html = markdown_to_html(body_md)
    if filename == "results.html":
        section_html += RESULTS_INSERT
    body = f"""
<section class="hero compact">
  <div class="hero-copy">
    <p class="eyebrow">Publication section</p>
    <h1>{html.escape(page_heading)}</h1>
  </div>
</section>
<section class="content-block">
  {section_html}
</section>
"""
    return page_template(meta, page_heading, filename, body)


def build_dashboard(meta: dict[str, str]) -> str:
    return page_template(meta, "Dashboard", "dashboard.html", DASHBOARD_BODY)


def main() -> None:
    raw_text = CONTENT_PATH.read_text(encoding="utf-8")
    meta, body = parse_front_matter(raw_text)
    sections = split_top_sections(body)

    copy_viz_assets()
    (REPO_ROOT / "index.html").write_text(build_home(meta, sections), encoding="utf-8")
    (REPO_ROOT / "dashboard.html").write_text(build_dashboard(meta), encoding="utf-8")

    for title, section_body in sections:
        if title in {"SkillCurrent: A Unified Language Layer for Workforce Development", "Recommended project name", "Publication abstract"}:
            continue
        filename = SECTION_SLUGS.get(title)
        if not filename:
            continue
        page = build_section_page(meta, title, section_body, filename)
        (REPO_ROOT / filename).write_text(page, encoding="utf-8")


if __name__ == "__main__":
    main()
