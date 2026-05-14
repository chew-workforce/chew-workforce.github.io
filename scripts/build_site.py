#!/usr/bin/env python3

from __future__ import annotations

import html
import re
import shutil
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LIVE_CONTENT_PATH = REPO_ROOT / "content" / "skillcurrent_publication_live.md"
DRAFT_CONTENT_PATH = REPO_ROOT / "content" / "skillcurrent_publication_draft.md"
CONTENT_PATH = LIVE_CONTENT_PATH if LIVE_CONTENT_PATH.exists() else DRAFT_CONTENT_PATH
SITE_ASSETS = REPO_ROOT / "assets"
VIZ_ROOT = SITE_ASSETS / "viz"
DISPLAY_IMAGE_WIDTHS = {
    "09a22_recursive_hub_spoke_terminal_core_split.png": 1600,
    "01_canonical_demand_by_tier.png": 1400,
    "04_tier_demand_heatmaps.png": 1600,
    "03_canonical_skill_x_instruction_mode.png": 1400,
    "04_ranked_canonical_skill_support.png": 1400,
}

SOURCE_ASSETS = {
    "jd": {
        "09a22_recursive_hub_spoke_terminal_core_split.png": Path(
            "../../jd_to_skills/viz_outputs/09a22_recursive_hub_spoke_terminal_core_split.png"
        ),
        "05_hierarchy_sunburst.html": Path(
            "../../jd_to_skills/viz_outputs/05_hierarchy_sunburst.html"
        ),
        "06_granular_canonical_family_sankey.html": Path(
            "../../jd_to_skills/viz_outputs/06_granular_canonical_family_sankey.html"
        ),
        "08_evidence_family_sunburst.html": Path(
            "../../jd_to_skills/viz_outputs/08_evidence_family_sunburst.html"
        ),
        "01_canonical_demand_by_tier.png": Path(
            "../../jd_to_skills/viz_outputs/01_canonical_demand_by_tier.png"
        ),
        "04_tier_demand_heatmaps.png": Path(
            "../../jd_to_skills/viz_outputs/04_tier_demand_heatmaps.png"
        ),
        "04_demand_signal_scatter.png": Path(
            "../../jd_to_skills/viz_outputs/04_demand_signal_scatter.png"
        ),
        "10_skill_combination_hierarchy.html": Path(
            "../../jd_to_skills/viz_outputs/10_skill_combination_hierarchy.html"
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
    },
}

PRIMARY_NAV = [
    ("The Opportunity", "opportunity.html"),
    ("The Approach", "approach.html"),
    ("The Implication", "implication.html"),
]

PAGE_FLOW = [
    "index.html",
    "opportunity.html",
    "approach.html",
    "implication.html",
    "references.html",
]

PAGE_LABELS = {
    "index.html": "Home",
    "opportunity.html": "The Opportunity",
    "approach.html": "The Approach",
    "implication.html": "The Implication",
    "references.html": "References",
}

OBSOLETE_PAGES = [
    "dashboard.html",
    "premise.html",
    "opportunity-gap.html",
    "results.html",
    "implications.html",
    "methodology.html",
    "site-structure.html",
    "overclaim.html",
    "work-plan.html",
]


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    _, rest = text.split("---\n", 1)
    raw_meta, body = rest.split("\n---\n", 1)
    meta: dict[str, str] = {}
    for line in raw_meta.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"')
    return meta, body.lstrip()


def split_top_sections(text: str) -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    current_title: str | None = None
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


def split_subsections(text: str, level: str = "## ") -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    current_title: str | None = None
    current_lines: list[str] = []
    for line in text.splitlines():
        if line.startswith(level):
            if current_title is not None:
                sections.append((current_title, "\n".join(current_lines).strip()))
            current_title = line[len(level) :].strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_title is not None:
        sections.append((current_title, "\n".join(current_lines).strip()))
    return sections


def autolink_urls(text: str) -> str:
    return re.sub(
        r'(?<!href=")(https://[^\s<]+)',
        lambda m: f'<a href="{m.group(1)}">{m.group(1)}</a>',
        text,
    )


def slugify(text: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return cleaned or "section"


def format_inline(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>',
        escaped,
    )
    escaped = re.sub(
        r"\[\^([^\]]+)\]",
        lambda m: (
            f'<sup class="footnote-ref"><a href="references.html#ref-{html.escape(m.group(1))}">'
            f"{html.escape(m.group(1))}</a></sup>"
        ),
        escaped,
    )
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    escaped = autolink_urls(escaped)
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
    return (
        '<div class="table-wrap"><table><thead><tr>'
        + thead
        + "</tr></thead><tbody>"
        + "".join(body_rows)
        + "</tbody></table></div>",
        idx,
    )


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
        if list_mode:
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
            key = html.escape(reference.group(1))
            out.append(
                f'<div class="reference-entry" id="ref-{key}">'
                f'<p><span class="reference-key">[{key}]</span> {format_inline(reference.group(2))}</p>'
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
    html_text = "\n".join(out)
    math_block = """<pre><code class="language-text">
Gap Pressure(skill) = Demand Intensity(skill)
                      × Strategic Weight(skill)
                      × (1 - Curriculum Coverage(skill))
                      × (1 - Credential Coverage(skill))
</code></pre>"""
    math_replacement = r"""
<div class="display-math">
\[
\operatorname{GapPressure}(\mathrm{skill}) =
\operatorname{DemandIntensity}(\mathrm{skill})
\times \operatorname{StrategicWeight}(\mathrm{skill})
\times \left(1-\operatorname{CurriculumCoverage}(\mathrm{skill})\right)
\times \left(1-\operatorname{CredentialCoverage}(\mathrm{skill})\right)
\]
</div>
"""
    return html_text.replace(math_block, math_replacement)


def copy_viz_assets() -> None:
    for group, files in SOURCE_ASSETS.items():
        dest_dir = VIZ_ROOT / group
        dest_dir.mkdir(parents=True, exist_ok=True)
        for name, relative_source in files.items():
            source = (REPO_ROOT / relative_source).resolve()
            if not source.exists():
                raise FileNotFoundError(f"Missing visualization asset: {source}")
            destination = dest_dir / name
            shutil.copy2(source, destination)
            if destination.suffix == ".html":
                postprocess_plotly_html(destination)
            if destination.suffix == ".png" and name in DISPLAY_IMAGE_WIDTHS:
                create_display_image(destination, DISPLAY_IMAGE_WIDTHS[name])


def postprocess_plotly_html(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if "codex-responsive-plot" in text:
        return
    injection = """
<style id="codex-responsive-plot">
html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: #ffffff;
}
body > div {
  width: 100%;
  height: 100vh;
}
.plotly-graph-div {
  width: 100% !important;
  height: 100vh !important;
}
</style>
<script>
function codexResizePlot() {
  var graphs = document.querySelectorAll('.plotly-graph-div');
  graphs.forEach(function(graph) {
    graph.style.width = '100%';
    graph.style.height = '100vh';
    if (window.Plotly && window.Plotly.Plots) {
      window.Plotly.Plots.resize(graph);
    }
  });
}
window.addEventListener('load', codexResizePlot);
window.addEventListener('resize', codexResizePlot);
</script>
"""
    if "</head>" in text:
        text = text.replace("</head>", injection + "\n</head>", 1)
    elif "<body>" in text:
        text = text.replace("<body>", "<body>\n" + injection, 1)
    path.write_text(text, encoding="utf-8")


def create_display_image(path: Path, width: int) -> None:
    display_path = path.with_name(f"{path.stem}-display{path.suffix}")
    subprocess.run(
        [
            "sips",
            "-Z",
            str(width),
            str(path),
            "--out",
            str(display_path),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def remove_obsolete_pages() -> None:
    for filename in OBSOLETE_PAGES:
        path = REPO_ROOT / filename
        if path.exists():
            path.unlink()


def render_nav(active_file: str) -> str:
    parts = ['<nav class="site-nav" aria-label="Primary">']
    for label, href in PRIMARY_NAV:
        active = ' class="active"' if href == active_file else ""
        parts.append(f'<a href="{href}"{active}>{html.escape(label)}</a>')
    parts.append("</nav>")
    return "".join(parts)


def pager_html(active_file: str) -> str:
    if active_file not in PAGE_FLOW:
        return ""
    idx = PAGE_FLOW.index(active_file)
    prev_link = None if idx == 0 else PAGE_FLOW[idx - 1]
    next_link = None if idx == len(PAGE_FLOW) - 1 else PAGE_FLOW[idx + 1]
    parts = ['<nav class="page-pager" aria-label="Page flow">']
    parts.append(
        f'<a class="pager-link prev" href="{prev_link}">Previous: {PAGE_LABELS[prev_link]}</a>'
        if prev_link
        else '<span class="pager-spacer"></span>'
    )
    parts.append(
        f'<a class="pager-link next" href="{next_link}">Continue: {PAGE_LABELS[next_link]}</a>'
        if next_link
        else '<span class="pager-spacer"></span>'
    )
    parts.append("</nav>")
    return "".join(parts)


def figure_block(label: str, caption: str, media: str) -> str:
    match = re.match(r"Figure\s+(\d+):", label)
    anchor = f' id="figure-{match.group(1)}"' if match else ""
    return f"""
<figure class="figure-block"{anchor}>
  <figcaption>
    <span class="figure-label">{html.escape(label)}</span>
    <p>{html.escape(caption)}</p>
  </figcaption>
  <div class="figure-media">{media}</div>
</figure>
"""


def iframe_media(src: str, title: str) -> str:
    return (
        f'<iframe src="{src}" title="{html.escape(title)}" loading="lazy"></iframe>'
        f'<p class="figure-open"><a href="{src}" target="_blank" rel="noopener">Open interactive figure</a></p>'
    )


def display_src(src: str) -> str:
    path = REPO_ROOT / src
    display_path = path.with_name(f"{path.stem}-display{path.suffix}")
    if display_path.exists():
        return display_path.relative_to(REPO_ROOT).as_posix()
    return src


def zoomable_image(src: str, alt: str) -> str:
    return (
        f'<a class="zoomable" href="{src}" data-lightbox-src="{src}" data-lightbox-alt="{html.escape(alt)}">'
        f'<img src="{display_src(src)}" alt="{html.escape(alt)}" loading="lazy" /></a>'
    )


def section_shell(kicker: str, title: str, intro: str, content: str) -> str:
    return f"""
<section class="page-head">
  <p class="kicker">{html.escape(kicker)}</p>
  <h1>{format_inline(title)}</h1>
  <p class="page-intro">{html.escape(intro)}</p>
</section>
{content}
"""


def page_template(meta: dict[str, str], page_title: str, active_file: str, body: str) -> str:
    nav = render_nav(active_file)
    title = f"{page_title} | Inference Dashboard"
    description = meta.get("subtitle", "")
    pager = pager_html(active_file)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}" />
  <link rel="stylesheet" href="assets/site.css" />
  <script>
    window.MathJax = {{
      tex: {{ inlineMath: [['\\\\(', '\\\\)']], displayMath: [['\\\\[', '\\\\]']] }},
      svg: {{ fontCache: 'global' }}
    }};
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
</head>
<body>
  <div class="site-frame">
    <header class="site-header">
      <a class="brand" href="index.html" aria-label="Inference Dashboard Home">
        <span>Inference</span>
        <span>Dashboard</span>
      </a>
      {nav}
    </header>
    <main class="site-main">
      {body}
      {pager}
    </main>
    <footer class="site-footer">
      <p><a href="connect.html">Connect</a></p>
      <p>Copyright 2026<br />The Center for Higher Education and Workforce at Northeastern University</p>
    </footer>
  </div>
  <div class="lightbox" id="lightbox" hidden>
    <button class="lightbox-close" type="button" aria-label="Close image viewer">Close</button>
    <img class="lightbox-image" alt="" />
  </div>
  <script src="assets/site.js"></script>
</body>
</html>
"""


def wrap_section(anchor: str, heading: str, body_html: str) -> str:
    return f"""
<section class="content-section" id="{anchor}">
  <h2>{html.escape(heading)}</h2>
  <div class="prose">
    {body_html}
  </div>
</section>
"""


def strip_leading_blockquote(text: str) -> str:
    return re.sub(r"^>\s.*?(?:\n\n|\Z)", "", text, flags=re.S)


def remove_trailing_hr(html_text: str) -> str:
    return re.sub(r"\s*<hr\s*/>\s*$", "", html_text)


def sanitize_outcome_section(text: str) -> str:
    out: list[str] = []
    lines = text.splitlines()
    skip_table = False
    skip_next_italic = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("**Insert Figure"):
            skip_next_italic = True
            continue
        if skip_next_italic and stripped.startswith("*") and stripped.endswith("*"):
            skip_next_italic = False
            continue
        skip_next_italic = False
        if stripped in {"**Draft interpretation:**", "**Data slots to fill:**"}:
            continue
        if stripped.startswith("| Metric | Value | Source artifact |"):
            skip_table = True
            continue
        if skip_table:
            if not stripped:
                skip_table = False
            continue
        out.append(line)
    return "\n".join(out).strip()


def select_subsections(text: str, allowed: list[str]) -> str:
    subsection_map = dict(split_subsections(text))
    chosen = []
    for key in allowed:
        if key in subsection_map:
            chosen.append(f"## {key}\n\n{subsection_map[key]}")
    return "\n\n".join(chosen)


def renumber_headings(text: str, replacements: dict[str, str]) -> str:
    out = text
    for old, new in replacements.items():
        out = out.replace(old, new)
    return out


def merge_methodology(methodology_body: str) -> str:
    subsections = dict(split_subsections(methodology_body))
    limitations = subsections.get("6.6 Limitations", "")
    merged_data_sources = subsections.get("6.2 Data sources", "")
    if limitations:
        merged_data_sources += (
            "\n\n### Publication constraints and limitations\n\n"
            "The public-facing site is intentionally narrower than the full internal workflow. "
            "Those constraints are part of the methodology rather than an afterthought.\n\n"
            + limitations
        )
    parts = [
        ("4.1 Study design", subsections.get("6.1 Study design", "")),
        ("4.2 Data sources", merged_data_sources),
        ("4.3 Skill extraction model", subsections.get("6.3 Skill extraction model", "")),
        (
            "4.4 Normalization and hierarchy induction",
            subsections.get("6.4 Normalization and hierarchy induction", ""),
        ),
    ]
    combined = []
    for heading, body in parts:
        if body:
            combined.append(f"## {heading}\n\n{body}")
    return "\n\n".join(combined)


def build_home(meta: dict[str, str], section_map: dict[str, str]) -> str:
    abstract_html = remove_trailing_hr(markdown_to_html(section_map["Publication abstract"]))
    dashboard_html = """
<div class="dashboard-grid">
  <div class="dashboard-stat">
    <span class="dashboard-value">647</span>
    <span class="dashboard-label">Connecticut employers mapped</span>
  </div>
  <div class="dashboard-stat">
    <span class="dashboard-value">1,479</span>
    <span class="dashboard-label">Active job postings harvested</span>
  </div>
  <div class="dashboard-stat">
    <span class="dashboard-value">1,072</span>
    <span class="dashboard-label">Postings with full text</span>
  </div>
  <div class="dashboard-stat">
    <span class="dashboard-value">247</span>
    <span class="dashboard-label">Canonical skills in the current taxonomy</span>
  </div>
  <a class="dashboard-thumb" href="implication.html#figure-1">
    <span class="thumbnail-media"><img src="assets/viz/jd/09a22_recursive_hub_spoke_terminal_core_split-display.png" alt="Employer connectome thumbnail" loading="lazy" /></span>
  </a>
  <a class="dashboard-thumb" href="implication.html#figure-6">
    <span class="thumbnail-media"><img src="assets/viz/jd/04_tier_demand_heatmaps-display.png" alt="Tier demand heatmaps thumbnail" loading="lazy" /></span>
  </a>
  <a class="dashboard-thumb" href="implication.html#figure-7">
    <span class="thumbnail-media thumbnail-iframe"><iframe src="assets/viz/jd/10_skill_combination_hierarchy.html" title="Skill hierarchy thumbnail" loading="lazy"></iframe></span>
  </a>
  <a class="dashboard-thumb" href="implication.html#figure-8">
    <span class="thumbnail-media thumbnail-iframe"><iframe src="assets/viz/jd/08_evidence_family_sunburst.html" title="Evidence family hierarchy thumbnail" loading="lazy"></iframe></span>
  </a>
</div>
"""
    acknowledgement = """
<p>This publication reflects work carried out within Northeastern University’s Shipyard of the Future and Workforce Intelligence effort, together with the curriculum and employer-side analysis streams represented in the repository.</p>
<p>The website form is deliberate: the goal is not to flatten the research into marketing copy, but to keep the argument, methods, and figures updateable as the evidence base changes.</p>
"""
    partnership = """
<p>The platform is intended to sit between employers, training providers, universities, and credentialing organizations. That means the publication has to function as both narrative and interface: readable as an argument, but navigable as a live comparative instrument.</p>
<p>Future iterations can expand the public data layer, add credential-pathway mappings, and expose filtered views for region, employer tier, and instructional depth without changing the publication structure itself.</p>
"""
    body = section_shell(
        "Interactive publication",
        "A Unified Language Layer<br>for Workforce Development",
        meta.get("subtitle", ""),
        wrap_section("abstract", "Abstract", abstract_html)
        + wrap_section("dashboard", "Dashboard", dashboard_html)
        + wrap_section("acknowledgement", "Acknowledgement", acknowledgement)
        + wrap_section("partnership", "Partnership", partnership),
    )
    return page_template(meta, "Home", "index.html", body)


def build_opportunity(meta: dict[str, str], section_map: dict[str, str]) -> str:
    body = section_shell(
        "Publication section",
        "The Opportunity",
        "The publication opens with the national manufacturing premise and then moves into the alignment gap the platform is designed to address.",
        wrap_section(
            "premise",
            "1. The Premise",
            remove_trailing_hr(markdown_to_html(section_map["1. The premise"])),
        )
        + wrap_section(
            "opportunity-gap",
            "2. The Opportunity",
            remove_trailing_hr(markdown_to_html(section_map["2. The opportunity gap"])),
        ),
    )
    return page_template(meta, "Opportunity", "opportunity.html", body)


def build_approach(meta: dict[str, str], section_map: dict[str, str]) -> str:
    approach_body = select_subsections(
        section_map["3. The approach: a live, local, evidence-first skill inference platform"],
        [
            "3.1 Summary of the approach",
            "3.2 Why local/on-premises inference is a design requirement",
            "3.3 The algorithm at a high level",
            "3.4 Why the same algorithm must process curriculum and job descriptions",
            "3.5 Positioning relative to existing work",
        ],
    )
    methodology = merge_methodology(section_map["6. Methodology"])
    body = section_shell(
        "Publication section",
        "The Approach",
        "The platform architecture comes first, followed by the methodological details required to audit the claims being made in the publication.",
        wrap_section(
            "approach-overview",
            "3. The Approach",
            remove_trailing_hr(markdown_to_html(approach_body)),
        )
        + wrap_section(
            "methodology",
            "4. Methodology",
            remove_trailing_hr(markdown_to_html(methodology)),
        ),
    )
    return page_template(meta, "Approach", "approach.html", body)


def build_implication(meta: dict[str, str], section_map: dict[str, str]) -> str:
    results_body = strip_leading_blockquote(section_map["4. Results"])
    result_sections = dict(split_subsections(results_body))
    implication_body = renumber_headings(
        section_map["5. Implications"],
        {
            "## 5.1": "## 6.1",
            "## 5.2": "## 6.2",
            "## 5.3": "## 6.3",
            "## 5.4": "## 6.4",
            "## 5.5": "## 6.5",
        },
    )
    outcomes = [
        wrap_section(
            "outcome-demand",
            "5.1 Employer demand signal",
            markdown_to_html(
                sanitize_outcome_section(result_sections["4.1 Demand-side skill signal from job descriptions"])
            )
            + figure_block(
                "Figure 1: Reading the employer network around Electric Boat in Connecticut",
                "The demand story starts with the structure of the regional ecosystem itself: the network anchors the later skill evidence in a specific Connecticut defense and maritime labor market.",
                zoomable_image(
                    "assets/viz/jd/09a22_recursive_hub_spoke_terminal_core_split.png",
                    "Employer network graph for Electric Boat in Connecticut",
                ),
            )
            + figure_block(
                "Figure 2: Aggregating job-description demand into a canonical hierarchy",
                "The hierarchy view shows how many differently worded job-description fragments are normalized into a smaller, interpretable demand structure.",
                iframe_media(
                    "assets/viz/jd/05_hierarchy_sunburst.html",
                    "Canonical demand hierarchy from job descriptions",
                ),
            )
            + figure_block(
                "Figure 3: Weighting demand by employer tier",
                "This figure distinguishes broad hiring visibility from demand concentrated in the most strategically important employers in the Connecticut network.",
                zoomable_image(
                    "assets/viz/jd/01_canonical_demand_by_tier.png",
                    "Canonical demand by employer tier",
                ),
            ),
        ),
        wrap_section(
            "outcome-curriculum",
            "5.2 Curriculum signal",
            markdown_to_html(
                sanitize_outcome_section(result_sections["4.2 Supply-side skill signal from curriculum"])
            )
            + figure_block(
                "Figure 4: Mapping curriculum evidence into the shared skill hierarchy",
                "The curriculum hierarchy makes visible where instructional material aligns with the same vocabulary used to summarize employer demand.",
                iframe_media(
                    "assets/viz/curriculum/02_sunburst_skill_family_canonical_granular.html",
                    "Curriculum hierarchy from skill family to canonical to granular",
                ),
            )
            + figure_block(
                "Figure 5: Measuring instructional depth rather than simple topic mention",
                "The heatmap helps separate skills that are taught and assessed from skills that appear only as contextual mentions in curriculum material.",
                zoomable_image(
                    "assets/viz/curriculum/03_canonical_skill_x_instruction_mode.png",
                    "Instruction-depth evidence by canonical skill",
                ),
            ),
        ),
        wrap_section(
            "outcome-alignment",
            "5.3 Demand and supply alignment",
            markdown_to_html(sanitize_outcome_section(result_sections["4.3 Demand-supply alignment"]))
            + figure_block(
                "Figure 6: Comparing demand concentration across employer tiers and families",
                "The tier-demand heatmaps provide a compact comparative view of where employer-weighted demand is strongest across the published hierarchy.",
                zoomable_image(
                    "assets/viz/jd/04_tier_demand_heatmaps.png",
                    "Tier demand heatmaps",
                ),
            )
            + figure_block(
                "Figure 7: Navigating skill combinations through the hierarchy",
                "This interactive hierarchy view is placed here because it shows how the combined skill structure can be read once demand and supply have both been translated into the same language layer.",
                iframe_media(
                    "assets/viz/jd/10_skill_combination_hierarchy.html",
                    "Skill combination hierarchy",
                ),
            )
        ),
        wrap_section(
            "outcome-credential",
            "5.4 Credential and instructional readiness",
            markdown_to_html(
                sanitize_outcome_section(result_sections["4.4 Credential and pathway alignment"])
            )
            + markdown_to_html(
                sanitize_outcome_section(result_sections["4.5 Method of instruction breakdown"])
            )
            + figure_block(
                "Figure 8: Inspecting evidence concentration before credential mapping",
                "The evidence-family hierarchy helps show which portions of the published demand signal are dense enough to support later credential and pathway design work.",
                iframe_media(
                    "assets/viz/jd/08_evidence_family_sunburst.html",
                    "Evidence-family hierarchy for job-description skills",
                ),
            ),
        ),
    ]
    body = section_shell(
        "Publication section",
        "The Implication",
        "The results are presented as outcomes first, with figures woven directly into the argument, and then extended into the broader implications for workforce infrastructure.",
        "".join(outcomes)
        + wrap_section(
            "implications",
            "6. Implications",
            remove_trailing_hr(markdown_to_html(implication_body)),
        ),
    )
    return page_template(meta, "Implication", "implication.html", body)


def build_connect(meta: dict[str, str]) -> str:
    connect_html = """
<p>This site is not meant to be a polished endpoint. It is a working publication surface for an evidence-first skill translation layer that can keep evolving as the data, methods, and partner network evolve.</p>
<p>The strongest use of the platform is collaborative: employers bring demand language, educators bring instructional evidence, and public-interest partners help translate those signals into more legible pathways for learners and workers.</p>
<h3>Partnership model</h3>
<p>The publication assumes a partnership structure in which universities coordinate analytical infrastructure, providers contribute curriculum evidence, employers contribute demand context, and credentialing organizations help validate portability.</p>
"""
    body = section_shell(
        "Publication section",
        "Connect",
        "This page frames the site as shared publication infrastructure rather than a standalone marketing artifact.",
        wrap_section("connect", "Connect", connect_html),
    )
    return page_template(meta, "Connect", "connect.html", body)


def build_references(meta: dict[str, str], section_map: dict[str, str]) -> str:
    body = section_shell(
        "Supporting material",
        "References",
        "All cited sources are listed here so the publication pages can keep footnotes lightweight while preserving direct links.",
        wrap_section("references", "References", markdown_to_html(section_map["References"])),
    )
    return page_template(meta, "References", "references.html", body)


def main() -> None:
    raw_text = CONTENT_PATH.read_text(encoding="utf-8")
    meta, body = parse_front_matter(raw_text)
    section_map = dict(split_top_sections(body))

    copy_viz_assets()
    remove_obsolete_pages()

    outputs = {
        "index.html": build_home(meta, section_map),
        "opportunity.html": build_opportunity(meta, section_map),
        "approach.html": build_approach(meta, section_map),
        "implication.html": build_implication(meta, section_map),
        "connect.html": build_connect(meta),
        "references.html": build_references(meta, section_map),
    }
    for filename, page in outputs.items():
        (REPO_ROOT / filename).write_text(page, encoding="utf-8")


if __name__ == "__main__":
    main()
