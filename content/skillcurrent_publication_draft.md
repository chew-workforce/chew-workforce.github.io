---
title: "A Unified Language Layer for Workforce Development"
subtitle: "A live, evidence-first platform for comparing employer skill demand, curriculum skill supply, and credential pathways"
author: "Northeastern University — Shipyard of the Future / Workforce Intelligence Project"
status: "Working publication draft for GitHub Pages"
last_updated: "2026-05-14"
---

# SkillCurrent: A Unified Language Layer for Workforce Development

## Recommended project name

**SkillCurrent**

**Tagline:** *A live language layer for translating jobs, curriculum, and credentials into a shared workforce signal.*

**Why this name works:**

- **Current** signals that the platform is live, versioned, and refreshable rather than a static report.
- **Skill** anchors the publication around the unit of comparison that matters across employers, learners, curriculum designers, and credentialing bodies.
- The name avoids implying that the system is a universal taxonomy. It is better framed as a **current, evidence-grounded translation layer** between different sources of workforce evidence.

**Alternates worth holding:**

1. **CommonSkill** — stronger emphasis on a shared language, but less distinctive.
2. **Workforce Rosetta** — clear metaphor, but may create brand/trademark friction and overpromises translation equivalence.
3. **SkillSignal Atlas** — strong for the dashboard layer, but “signal” is already widely used in HR analytics.
4. **SkillMap Live** — accessible, but less publication-grade.
5. **SkillCommons** — good public-interest framing, but less specific to live inference and comparison.

My recommendation is to publish the site as **SkillCurrent** with the subtitle **“A Unified Language Layer for Workforce Development.”**

---

# Publication abstract

The United States is entering a new manufacturing cycle defined by reshoring, defense industrial-base expansion, semiconductor investment, automation, and renewed attention to middle-skill technical work. Yet workforce development systems still lack a reliable, shared, and refreshable language for comparing what employers ask for, what training programs teach, and what credentials validate. SkillCurrent addresses this gap by using a locally deployed, evidence-first language inference pipeline to extract granular skills from job descriptions and curriculum documents, normalize those skills into a common vocabulary, organize them into auditable skill families, and connect them to credential pathways.

The platform is designed as both a research publication and a living dashboard. Rather than treating job postings, curricula, and credentials as separate artifacts, SkillCurrent treats them as three views of the same workforce alignment problem: employer demand, instructional supply, and portable validation. The pipeline runs on-premises to protect proprietary curriculum and employer intelligence, maintains traceability from every derived skill back to source evidence, and supports iterative validation rather than one-time expert coding. Initial application focuses on advanced manufacturing, maritime, and defense supply-chain roles, with the intent of generalizing to other industries and regions.

The contribution is methodological and infrastructural. Methodologically, the project demonstrates a defensible workflow for skill extraction, normalization, hierarchy induction, and instruction-depth scoring using local language models, embeddings, graph structure, and repair loops. Infrastructurally, it proposes a live public-facing publication model where methods, interactive figures, and aggregate results can be updated as new data are processed. The expected result is a lower-friction pathway for aligning employer needs, academic training, micro-credentials, apprenticeships, and regional workforce investment.

---

# 1. The premise

## 1.1 Manufacturing is returning as a strategic national capability, not as nostalgia

The U.S. manufacturing conversation is no longer only about preserving legacy industrial employment. It is increasingly about national capability: defense production, shipbuilding, semiconductors, energy systems, automation, advanced materials, and resilient supply chains. Manufacturing USA describes advanced manufacturing as foundational to U.S. economic strength and a platform for “good jobs” and a resurgent middle class, while also emphasizing that reshoring and advanced technology adoption depend on access to skilled workers.[^mfgusa_framework]

That matters because the current manufacturing transition is not a simple return to the twentieth-century shop floor. The work is becoming more skill-intensive and technology-mediated. Workers are expected to operate, maintain, troubleshoot, and improve systems that combine mechanical equipment, digital controls, robotics, metrology, cyber-physical systems, quality systems, and documentation practices. The “new” manufacturing economy therefore resembles a hybrid of older industrial production and newer AI- and data-enabled systems. The analogy is not a literal return to the 1920s; it is a recurrence of a broader pattern: large-scale industrial investment, new production technologies, and the need to reorganize training systems around a changing technical base.

The workforce stakes are large. Deloitte and The Manufacturing Institute estimate that U.S. manufacturing could need as many as **3.8 million** additional workers between 2024 and 2033, and that **1.9 million** of those positions could go unfilled if workforce challenges are not addressed.[^mi_deloitte_2024] Semiconductor policy makes the same point in a strategically concentrated way: the CHIPS and Science Act includes dedicated semiconductor workforce training and education investments, and federal STEM programs are explicitly tied to expanding the technical talent base.[^nsf_chips]

## 1.2 The training system needs a demand signal that is more precise than “industry says it needs workers”

Universities, community colleges, technical high schools, training centers, unions, apprenticeship sponsors, and workforce boards all hear the same broad message: industry needs talent. The problem is that “talent” is not a curriculum design unit. A training provider cannot build a module from “advanced manufacturing.” It needs to know whether the regional labor market is asking for CNC setup, GD&T interpretation, blueprint reading, PLC troubleshooting, dimensional inspection, non-destructive testing, welding process qualification, SAP/MRP use, cybersecurity fundamentals, additive manufacturing design, or robotics maintenance.

The premise of SkillCurrent is that workforce alignment depends on translating broad labor-market concern into **granular, evidence-backed, comparable skill statements**. Job descriptions provide one imperfect but useful demand signal: they show what employers are willing to ask for in active hiring. Curriculum documents provide a parallel supply signal: they show what training programs claim, teach, practice, assess, or merely mention. Credentials provide the validation layer: they show which combinations of skills can be made portable and recognizable outside a single course or employer.

## 1.3 Training must move toward the worker, not only pull the worker toward the training center

A central assumption of the project is that training friction is itself a workforce bottleneck. Training centers that require workers to leave the job for long periods will struggle to support incumbent workers, career changers, and small manufacturers with thin staffing capacity. Micro-credentials and modular training are not a complete answer, but they offer an important structural advantage: they can be shorter, more targeted, and easier to align with a specific skill gap. The European Commission’s micro-credential framework emphasizes short-term learning experiences that certify learning outcomes and can support flexible, personalized learning and career pathways across institutions, sectors, and borders.[^eu_microcredentials]

SkillCurrent therefore treats curriculum not merely as a list of courses, but as a structured set of skill outcomes with associated evidence depth: explicit instruction, guided practice, independent practice, assessment, or mention-only. This distinction is essential. A skill that is mentioned in a slide deck is not equivalent to a skill that is practiced repeatedly and formally assessed.

## 1.4 The cultural shift is from transaction work to skill-heavy value work

The project also rests on a workforce philosophy: durable regional growth depends on moving away from a purely transactional view of labor. Employers do not merely need bodies to fill roles. They need people who can build proficiency, adapt to new processes, use technology responsibly, and retain tacit and technical knowledge inside organizations. Industry 5.0 scholarship frames this shift as a move beyond technology-first automation toward human-centric, sustainable, and resilient production systems.[^industry5_oeij] In that view, workers are not residual inputs after automation; they are the adaptive capacity of the industrial system.

SkillCurrent operationalizes this philosophy by making skill evidence visible. The platform does not claim that dashboards solve training. Instead, it makes the skill conversation specific enough that industry, academia, and government partners can decide where to invest, what to teach, what to credential, and what evidence is still missing.

---

# 2. The opportunity gap

## 2.1 The missing layer is not another taxonomy; it is a translation layer

There are already skill and competency systems. O*NET describes occupations in terms of knowledge, skills, abilities, tasks, activities, and other descriptors across the U.S. economy.[^onet] ESCO provides a multilingual European classification of occupations and skills and explicitly aims to help work and education/training communicate more effectively.[^esco] Lightcast maintains a large market-derived skills taxonomy from job postings, resumes, and profiles.[^lightcast_open_skills] Manufacturing USA’s 2025 framework provides a common language for advanced manufacturing occupations, skills, and competencies across institutes, employers, trainers, and workers.[^mfgusa_framework]

The gap is not the absence of taxonomies. The gap is the lack of a **local, refreshable, evidence-first layer** that can infer skills from proprietary curriculum and current job descriptions, normalize them into a shared vocabulary, and preserve the trace back to the original text. Existing frameworks are valuable reference systems, but they do not automatically answer the regional question: *What are employers in this specific supply chain asking for now, and where is the corresponding training evidence?*

## 2.2 Credential ecosystems are large, fragmented, and hard to navigate

Credential Engine’s 2025 count reports **1,850,034** unique credentials and opportunities in the United States offered by more than **134,000** providers.[^credential_engine_2025] This is both a strength and a problem. A diverse credential ecosystem gives learners multiple pathways, but it also creates search and trust costs. Learners, employers, and training providers need to know which credentials are relevant, which skills they validate, which providers offer them, and how they stack.

Manufacturing USA makes a similar point for advanced manufacturing: credentialing activity has grown, but efforts remain fragmented, making it difficult for workers to navigate opportunities and for industry-wide adoption to occur.[^mfgusa_framework] The 2025 All-Island Industry 4.0 Future Skills report for Ireland and Northern Ireland reaches an analogous conclusion from a regional perspective: fragmented systems, dispersed course listings, and weak alignment between industry and training providers create friction for learners and employers.[^skillsvista_2025]

## 2.3 Job descriptions, curricula, and credentials each see only part of the system

The project treats the workforce system as three partial views:

- **Job descriptions** show employer demand, but are noisy. They include boilerplate, inflated requirements, legacy HR templates, and inconsistent language.
- **Curriculum documents** show instructional supply, but are also noisy. They may include topics, examples, safety notes, and procedures that are not all learnable skills.
- **Credentials** show formal validation, but often lack transparent alignment to the exact skills being asked for by employers or taught in a course.

The opportunity is to build a shared skill layer where these sources can be compared without forcing them into a rigid taxonomy at the outset. This is the practical meaning of a “unified language” for workforce development: not a universal vocabulary imposed from above, but a repeatable inference and evidence structure that makes local demand and local supply comparable.

## 2.4 Universities can serve as specialized centers and ecosystem coordinators

Large universities have a role that is broader than course delivery. They can serve as applied research centers, neutral validators, data stewards, conveners, and methodological infrastructure providers. Manufacturing USA’s network model is instructive: public-private collaboration across federal agencies, institutes, industry partners, and workforce programs is treated as a mechanism for accelerating technology development and workforce development.[^mfgusa_report_to_congress]

In regional deployment, a university can be the “general contractor” for the analytical infrastructure while community colleges, technical high schools, union programs, apprenticeship sponsors, and employer training centers remain the main delivery partners. This avoids the mistake of making universities the only training provider. The stronger model is: universities provide credibility, evidence infrastructure, specialized technical capacity, and cross-institutional coordination; delivery partners provide reach, equipment, local access, and worker-centered training.

---

# 3. The approach: a live, local, evidence-first skill inference platform

## 3.1 Summary of the approach

SkillCurrent is a local inference platform that processes two primary source types:

1. **Employer job descriptions** from a defined industry ecosystem.
2. **Curriculum documents** from training providers and educational programs.

Both are passed through the same final staged skill extraction algorithm so that demand-side skills and supply-side skills are represented in the same vocabulary and hierarchy.

The output is a set of linked artifacts:

```text
source document
  → evidence span
  → granular skill
  → normalized skill
  → canonical skill
  → skill family
  → credential candidate
  → provider / program pathway
```

The core methodological principle is simple:

> Extract only what is evidenced, normalize only what is semantically equivalent, and build higher-level groupings only from lower-level evidence.

## 3.2 Why local/on-premises inference is a design requirement

The system is designed for on-premises deployment because the inputs can include proprietary curriculum, employer-specific job intelligence, supply-chain mapping, and regional strategy documents. Sending those materials to external APIs would create governance, data-sharing, and intellectual-property concerns. Local inference also improves reproducibility: the model, prompts, checkpoints, configuration, and data version can be stored with each run.

The current implementation uses local open models for language inference and embeddings. The working stack is intentionally pragmatic rather than maximalist: a model large enough to reason over skill boundaries, plus embeddings and graph methods to reduce the number of expensive semantic decisions. The governing tradeoff is not “largest model wins.” It is **defensible output per unit of local compute**.

## 3.3 The algorithm at a high level

The final algorithm used for job descriptions and curriculum data follows an evidence-first, multi-layer architecture:

1. **Ingest and segment source text.** Source documents are cleaned, chunked, and assigned source metadata.
2. **Extract granular skill candidates.** The local LLM extracts skill-like units only when supported by an evidence span.
3. **Reject weak or non-skill candidates.** Topic labels, procedural fragments, vague abstractions, examples, and meta-instructions are quarantined or rejected.
4. **Normalize phrasing.** Equivalent phrasings are normalized into clean verb-object skill statements.
5. **Retrieve candidate matches.** Embeddings identify likely neighbors, but do not decide equivalence.
6. **Adjudicate semantic equivalence.** The LLM decides whether candidate pairs are same-skill, related-but-distinct, parent-child, or unrelated.
7. **Build normalized-skill graphs.** Graph structure preserves relations and prevents one-shot global clustering from creating catch-all categories.
8. **Induce canonical skills and families.** Canonicals and families are created from local coherent neighborhoods, with merge audits and coherence gates.
9. **Validate and repair.** Oversized, incoherent, generic, or cross-domain clusters are flagged for targeted repair rather than full reruns.
10. **Publish aggregate outputs.** Public outputs show aggregate skill demand, curriculum coverage, instruction depth, and credential alignment while protecting source documents.

This architecture deliberately separates **retrieval** from **semantic judgment**. Embeddings are used to find plausible neighbors; LLMs adjudicate meaning; graph structure preserves lineage. This is important because embeddings alone can collapse unrelated skills that share generic verbs or nearby context.

## 3.4 Why the same algorithm must process curriculum and job descriptions

The central methodological requirement is an apples-to-apples comparison. If job descriptions are processed with one extraction method and curricula with another, observed gaps may reflect pipeline artifacts rather than true workforce alignment gaps. For that reason, the final job-description skill extraction workflow is used as the common algorithm for both datasets.

The curriculum side adds an additional evidence dimension: **instructional mode**. A skill can be identified as explicitly taught, guided, independently practiced, assessed, or merely mentioned. This lets the results section distinguish “coverage” from “credential readiness.” A curriculum may mention robotics, for example, without providing enough practice or assessment evidence to support a credential claim.

## 3.5 Positioning relative to existing work

Skill extraction from job postings is now a recognized NLP research area. Senger et al. describe skill extraction and classification from job postings as core tasks in computational job market analysis and note the need for clearer datasets and terminology.[^senger_2024] Course-Skill Atlas demonstrates the adjacent education-side problem: systematically inferring skills from course syllabi at national scale to understand how higher education contributes to workforce skill development.[^course_skill_atlas]

SkillCurrent differs from these efforts in five ways:

1. It compares **job descriptions and curriculum documents** using a common pipeline.
2. It operates locally to handle proprietary curriculum and regional employer intelligence.
3. It preserves **evidence lineage** from every skill back to source text.
4. It scores **instructional depth**, not just skill presence.
5. It is designed as a **live dashboard publication**, not only a static dataset.

## 3.6 Dashboard and publication architecture

The GitHub website should be built as a static publication with dynamic charts generated from versioned data artifacts. Recommended implementation:

```text
skillcurrent-site/
  README.md
  index.md
  methods.md
  results.md
  dashboard.md
  data-dictionary.md
  limitations.md
  references.md
  assets/
    figures/
    html/
  data/
    public/
      skill_families_summary.csv
      canonical_skill_demand.csv
      curriculum_instruction_depth.csv
      credential_alignment_summary.csv
      run_metadata.json
  scripts/
    build_site.py
    validate_public_data.py
```

Recommended site stack:

- **Quarto** if the team wants paper-like narrative, citations, and executable notebooks.
- **GitHub Pages + static HTML/Plotly/D3** if the main goal is a lightweight public dashboard.
- **Jekyll** only if the team wants a traditional GitHub Pages blog/docs structure.

Recommended publication rule:

> Keep raw curriculum, raw job descriptions, and employer-sensitive excerpts out of the public repository. Publish only aggregate skill counts, de-identified evidence examples where permitted, methodology, model cards, run metadata, and interactive charts.

---

# 4. Results

> This section is intentionally structured for Codex and the analysis scripts to fill with final run outputs. The prose below is written so that charts can be inserted without rewriting the argument.

## 4.1 Demand-side skill signal from job descriptions

The demand-side analysis begins with active job descriptions from the target employer ecosystem. After scope filtering and text enrichment, the pipeline extracts skill evidence from job descriptions, normalizes equivalent phrasing, and aggregates demand by canonical skill and skill family.

**Insert Figure 1: Demand-side skill family distribution**  
*Interactive stacked bar or treemap showing canonical skills by family, weighted by job count, employer tier, and posting count.*

**Draft interpretation:**

The demand-side signal should be interpreted as a structured view of employer language, not a full census of all workforce needs. Job descriptions capture hiring-visible skills. They underrepresent tacit skills, internal incumbent-worker gaps, and skills taught informally on the job. They may overrepresent generic requirements repeated across templates. For that reason, the pipeline includes scope filters, boilerplate rejection, skill typing, coherence gates, and source lineage checks.

The most analytically useful outputs are not simply the most frequent skills. They are:

- skills with high demand across multiple employers;
- skills concentrated in strategically important employer tiers;
- skills that appear across multiple job families;
- skills with high demand but weak curriculum or credential coverage;
- emerging technical skills with low current training coverage but strong evidence in job descriptions.

**Data slots to fill:**

| Metric | Value | Source artifact |
|---|---:|---|
| Employers in scoped ecosystem | `[Codex fill]` | `employer_network_summary.json` |
| Job postings harvested | `[Codex fill]` | `job_database.csv` |
| Job descriptions with usable full text | `[Codex fill]` | `job_database_text_enriched.csv` |
| Granular skill candidates extracted | `[Codex fill]` | `s1_extract.csv` |
| Normalized skills after filtering | `[Codex fill]` | `s2_normalized.csv` |
| Canonical skills after graph/dedup | `[Codex fill]` | `s8_final_canonical_skills.csv` |
| Skill families | `[Codex fill]` | `s8_final_families.csv` |

## 4.2 Supply-side skill signal from curriculum

The curriculum-side analysis applies the same extraction and normalization logic to training materials. The critical difference is that curriculum evidence is classified by instructional mode. This allows the dashboard to distinguish skills that are actually taught and assessed from skills that appear only as context.

**Insert Figure 2: Curriculum skill hierarchy sunburst**  
*Skill family → canonical skill → instructional mode evidence.*

**Insert Figure 3: Canonical skill × instruction method heatmap**  
*Rows: canonical skills. Columns: explicit instruction, guided practice, independent practice, assessed, mention-only. Values: normalized evidence proportions.*

**Draft interpretation:**

Curriculum coverage should not be interpreted as binary. A skill may be present but weakly supported. A training program that explicitly teaches and assesses blueprint reading is different from a program that mentions drawings in a safety discussion. For credentialing, the strongest claims should come from skills with direct evidence of practice and assessment.

This method can also identify underused curriculum assets. A program may already teach a skill demanded by employers, but the evidence may be buried in documents that are not visible to learners, employers, or credentialing bodies. In that case, the intervention is not necessarily new curriculum development; it may be better documentation, assessment alignment, modularization, or credential packaging.

**Data slots to fill:**

| Metric | Value | Source artifact |
|---|---:|---|
| Curriculum source documents processed | `[Codex fill]` | `curriculum_manifest.csv` |
| Raw curriculum skill candidates | `[Codex fill]` | `curriculum_s1_extract.csv` |
| Normalized curriculum skills | `[Codex fill]` | `curriculum_s2_normalized.csv` |
| Canonical curriculum skills | `[Codex fill]` | `curriculum_final_canonical_skills.csv` |
| Skills with assessed evidence | `[Codex fill]` | `instruction_depth_summary.csv` |
| Skills that are mention-only | `[Codex fill]` | `instruction_depth_summary.csv` |

## 4.3 Demand-supply alignment

The central dashboard view compares demand-side canonical skills from job descriptions with supply-side canonical skills from curriculum.

**Insert Figure 4: Demand vs. curriculum coverage matrix**  
*X-axis: employer demand intensity. Y-axis: curriculum evidence depth. Bubble size: credential availability. Color: gap pressure.*

**Proposed core metric: Skill Gap Pressure**

```text
Gap Pressure(skill) = Demand Intensity(skill)
                      × Strategic Weight(skill)
                      × (1 - Curriculum Coverage(skill))
                      × (1 - Credential Coverage(skill))
```

Where:

- **Demand Intensity** is based on job count, employer count, and source frequency.
- **Strategic Weight** can include employer tier, supply-chain position, defense relevance, or regional priority.
- **Curriculum Coverage** is weighted by instructional mode, with assessed and practiced skills weighted higher than mention-only evidence.
- **Credential Coverage** reflects whether a recognizable credential or micro-credential validates the skill.

This should be presented as a prioritization score, not an absolute truth. It is meant to guide review, not replace expert judgment.

## 4.4 Credential and pathway alignment

The credential layer should answer four questions:

1. Which high-demand skills already map to recognized credentials?
2. Which skills are taught but not credentialed?
3. Which credentials exist but are not clearly connected to local demand?
4. Which high-pressure gaps are best addressed by micro-credentials, apprenticeships, incumbent-worker modules, or full program redesign?

**Insert Figure 5: Credential pathway graph**  
*Canonical skill → credential → provider → delivery modality.*

Credential matching should remain conservative. A credential should not be treated as covering a skill unless there is explicit evidence in its description, competency list, assessment objectives, or linked standards. Keyword overlap alone is insufficient.

## 4.5 Method of instruction breakdown

Instruction mode is the bridge from skill extraction to credential readiness. A credential claim is strongest when curriculum evidence shows that a skill is:

1. explicitly taught,
2. practiced with guidance,
3. practiced independently,
4. assessed with observable criteria.

A weak signal is a skill that appears only as a mention, example, heading, or safety aside.

**Insert Figure 6: Instruction depth by skill family**  
*Stacked bars showing assessed/practiced/explicit/mention-only evidence by family.*

**Draft interpretation:**

The instruction-depth breakdown should be used to identify where a training provider already has the ingredients for a credential and where it has only topical exposure. This distinction is essential for employers. Employers do not merely need to know that a curriculum includes “metrology”; they need to know whether learners actually use calipers, micrometers, gauges, drawings, tolerances, and inspection documentation in assessed tasks.

---

# 5. Implications

## 5.1 A more robust trainee-to-employee pipeline

SkillCurrent supports a trainee-to-employee pipeline by making training outcomes legible to employers and employer demand legible to training providers. The practical output is not just a list of “skills in demand.” It is a set of evidence-backed claims:

- This skill is requested by employers.
- This curriculum teaches it.
- This instructional evidence supports the claim.
- This credential validates it or could be designed to validate it.
- This provider can deliver it.

That chain is what allows a learner, employer, and training partner to talk about the same capability without relying on vague labels.

## 5.2 Less friction in aligning desired skills with trained skills

The main value of a shared language layer is reducing translation cost. Employers often express demand in job-description language. Curriculum designers express supply in course and outcome language. Credentialing bodies express validation in standards and competency language. Learners experience all of this as a confusing pathway problem.

A live skill layer lowers this friction by creating a common unit of comparison. It does not eliminate the need for human judgment. Instead, it makes the human review more focused: reviewers can inspect a skill, see its source evidence, view its curriculum coverage, and decide whether the proposed alignment is legitimate.

## 5.3 Faster assessment of opportunity gaps across industries and regions

Because the pipeline is domain-agnostic at the prompt and architecture level, the same approach can be deployed in another region or industry. The data will change; the method should not need to be rebuilt. That matters for scalability. A workforce board or university center should be able to run the method on healthcare, clean energy, construction, IT, maritime, or aerospace datasets and produce comparable demand-supply-credential maps.

The claim should be framed carefully: the method is **industry-agnostic**, but not **validation-free**. Each new domain needs evaluation for extraction precision, false merges, domain-specific terminology, and source bias.

## 5.4 New roles for universities and public-private partnerships

The project supports a model in which universities function as workforce intelligence infrastructure. They can host local inference systems, maintain evidence standards, support validation, coordinate with training providers, and publish living dashboards. This aligns with broader public-private models in advanced manufacturing where government, academia, and industry collaborate to accelerate technology adoption and workforce development.[^mfgusa_report_to_congress]

A university-led platform also gives credibility to credentials, especially when the credential is connected to evidence from curriculum, job demand, and assessment. The goal is not to centralize all training in the university. The goal is to let universities help the ecosystem coordinate.

## 5.5 Equity and access implications

A skill-first language layer can support equity only if it is designed carefully. OECD’s skills-first work emphasizes that skills-first approaches can improve transparency and matching, but implementation challenges remain and public policy matters.[^oecd_skills_first] The risk is that skill dashboards can become another opaque sorting mechanism. The mitigation is to make skill evidence, pathway options, credential requirements, and training availability transparent to learners, not only to employers and institutions.

A learner-facing version of SkillCurrent should answer:

- What skills am I learning?
- How are those skills assessed?
- Which employers ask for them?
- Which credentials validate them?
- Which adjacent skills would improve mobility?
- Which training option is closest, shortest, lowest-cost, or most stackable?

---

# 6. Methodology

## 6.1 Study design

SkillCurrent is a mixed computational and applied workforce research system. It combines:

- structured employer ecosystem definition;
- job posting collection and enrichment;
- local LLM-based skill extraction;
- embedding-assisted candidate retrieval;
- LLM semantic adjudication;
- graph-based hierarchy induction;
- curriculum instruction-depth scoring;
- credential candidate matching;
- dashboard publication;
- human validation and repair loops.

The intended unit of analysis is the **canonical skill**, not the job title, course title, or credential title. Job titles and course titles are too coarse for curriculum alignment. Individual extracted phrases are too noisy. Canonical skills provide a middle layer: granular enough to be actionable, normalized enough to aggregate.

## 6.2 Data sources

Public-facing publication should describe data sources at the appropriate level of detail:

1. **Employer ecosystem sources:** federal contracting records, employer career pages, job boards, and confirmed employer network metadata.
2. **Job description corpus:** active postings from scoped employers during the defined collection window.
3. **Curriculum corpus:** proprietary or partner-provided training documents, syllabi, modules, lesson plans, slides, assessment descriptions, and related materials.
4. **Credential sources:** Credential Engine, provider catalogs, industry credential descriptions, apprenticeship standards, and state-recognized credential lists.

The public site should publish run metadata and aggregate outputs, not raw proprietary documents.

## 6.3 Skill extraction model

The extraction model is constrained by rules:

- Extract only skills supported by source text.
- Prefer atomic verb-object statements.
- Reject topic labels that are not demonstrable skills.
- Reject vague abstractions unless a concrete action-object pair is recoverable.
- Preserve evidence text and source identifiers.
- Assign skill type and confidence.
- Quarantine ambiguous or weakly supported items.

The model is not asked to invent future skills. It is asked to infer what is present in the source.

## 6.4 Normalization and hierarchy induction

Normalization occurs only when skills are semantically equivalent or near-equivalent within a narrow operational meaning. The system avoids merging parent-child, tool-task, or related-but-distinct skills. Canonical skills are induced from normalized skills and must be the narrowest valid abstraction over their members. Skill families are induced from canonical skills and must avoid becoming generic bins.

This is a key defensibility point. The system does not begin with a rigid taxonomy and force every skill into it. Instead, it induces structure from evidence and can later map the resulting skills to external frameworks such as O*NET, ESCO, Manufacturing USA, or Credential Engine.

## 6.5 Validation plan

The public methodology should include a validation plan with at least six checks:

1. **Extraction precision audit:** stratified human review of extracted granular skills by source type and skill family.
2. **False rejection audit:** sample rejected candidates to estimate missed skills.
3. **Normalization audit:** review same-skill merges, parent-child near misses, and related-but-distinct pairs.
4. **Canonical coherence audit:** inspect oversized or low-coherence groups.
5. **Curriculum instruction-depth audit:** validate whether evidence mode labels correspond to actual instructional use.
6. **Stability audit:** rerun selected samples to test sensitivity to model version, chunking, and prompt updates.

Recommended public reporting metrics:

| Metric | Definition |
|---|---|
| Granular extraction precision | Share of sampled extracted skills judged valid and evidenced |
| False rejection rate | Share of sampled rejected candidates that should have been retained |
| Normalization precision | Share of sampled merges judged true same-skill equivalences |
| Canonical coherence | Share of members judged to belong under the canonical label |
| Instruction-depth agreement | Human agreement with mode label: taught/practiced/assessed/mentioned |
| Cross-run stability | Similarity of canonical outputs across repeat runs |
| Source lineage completeness | Share of public claims traceable to source evidence |

## 6.6 Limitations

This system should be pressure-tested around known weaknesses.

### Job posting limitations

Job descriptions are not perfect demand data. They can be stale, inflated, copied across roles, written by HR rather than supervisors, or biased toward formal qualifications over tacit work. The system mitigates this by de-duplicating postings, scope filtering, preserving source evidence, and aggregating across employers rather than treating each posting as ground truth.

### Curriculum limitations

Curriculum documents do not always represent actual instruction. Some skills are taught informally but absent from documents; others appear in documents but are not meaningfully taught. Instruction-depth scoring reduces this risk but does not eliminate it. Human validation with instructors remains necessary.

### LLM limitations

Local LLMs can hallucinate, over-normalize, under-normalize, or misclassify skills. The pipeline mitigates this through constrained prompts, JSON schemas, evidence requirements, type tagging, pairwise adjudication, graph coherence checks, repair loops, and human audits. Model outputs should be treated as structured inferences, not facts.

### Credential matching limitations

Credential descriptions vary widely in specificity. A credential may imply a skill without explicitly naming it, or may list broad competencies that are difficult to map to granular skills. For public reporting, the system should distinguish between **confirmed**, **probable**, and **candidate** credential matches.

### Generalizability limitations

The architecture is intended to generalize across domains, but each new domain requires validation. Healthcare, construction, software, energy, maritime, and advanced manufacturing have different terminology, regulatory structures, and credentialing ecosystems.

---

# 7. Recommended GitHub Pages structure

## 7.1 Navigation

1. **Home** — thesis, key findings, interactive summary.
2. **Premise** — why skill alignment matters now.
3. **Opportunity Gap** — why current systems are fragmented.
4. **Methodology** — pipeline, models, validation, limitations.
5. **Results** — interactive charts and narrative interpretation.
6. **Dashboard** — filterable skill demand/supply/credential views.
7. **Data Dictionary** — definitions, fields, run IDs, scoring formulas.
8. **Validation** — audit design, metrics, quality flags.
9. **Implications** — policy, training, credential, learner pathways.
10. **References** — external sources only.

## 7.2 Chart inventory

| Chart | Purpose | Data artifact |
|---|---|---|
| Skill demand treemap | Show employer demand by family and canonical skill | `canonical_skill_demand.csv` |
| Curriculum sunburst | Show taught skill hierarchy | `curriculum_skill_hierarchy.csv` |
| Instruction-depth heatmap | Show taught/practiced/assessed/mentioned | `curriculum_instruction_depth.csv` |
| Demand-supply matrix | Identify high-demand / low-supply gaps | `skill_gap_pressure.csv` |
| Credential pathway graph | Link skills to credentials and providers | `credential_skill_edges.csv` |
| Employer tier demand bars | Weight demand by strategic employer tier | `employer_tier_skill_counts.csv` |
| Evidence lineage table | Allow audit of aggregate claims | `public_evidence_samples.csv` |

## 7.3 Public data governance

The public repository should include:

- aggregate counts;
- de-identified examples where allowed;
- run metadata;
- prompt versions;
- model versions;
- scoring formulas;
- chart-ready CSV/JSON files;
- limitations and validation notes.

The public repository should exclude:

- proprietary curriculum source documents;
- raw job descriptions if licensing or privacy is uncertain;
- employer-sensitive internal annotations;
- personal data;
- unredacted evidence spans from restricted documents.

---

# 8. What not to overclaim

To keep the publication defensible, avoid these claims:

1. **Do not claim the pipeline measures all skills required in the industry.** It measures skills visible in available job descriptions and curriculum documents.
2. **Do not claim job postings equal true demand.** They are a useful but biased demand signal.
3. **Do not claim curriculum documents equal actual teaching.** They are documentary evidence of intended or represented instruction.
4. **Do not claim credentials fully validate skills unless assessment evidence is explicit.** Use graded confidence.
5. **Do not claim a universal taxonomy has been solved.** The contribution is a repeatable language-inference layer with evidence lineage.
6. **Do not claim local LLM outputs are automatically correct.** The defensibility comes from constraints, traceability, validation, and repair loops.
7. **Do not publish sensitive source text unless permissions are clear.** Public dashboards should rely on aggregate outputs.

---

# 9. Near-term work plan

## Publication build

1. Create GitHub Pages scaffold.
2. Add this draft as `index.md` or `paper.md`.
3. Add chart placeholders with stable IDs.
4. Add public data dictionary.
5. Add citation file if using Quarto/Zotero/BibTeX.
6. Add methodology diagrams.
7. Add run metadata and validation dashboard.

## Analysis completion

1. Finalize latest skill extraction run for jobs and curriculum.
2. Export canonical skill demand and curriculum coverage tables.
3. Generate instruction-depth scorecard.
4. Add credential candidate mapping.
5. Run validation audit sample.
6. Freeze a versioned public data release.

## Publication readiness checks

1. Confirm source permissions.
2. Redact sensitive evidence spans.
3. Verify all claims against public artifacts.
4. Run link checker.
5. Include a clear version and update date.
6. Add a limitations section on every dashboard page.

---

# References

[^mfgusa_framework]: Manufacturing USA. “2025 Advanced Manufacturing Occupation & Competency Framework.” https://www.manufacturingusa.com/reports/2025-advanced-manufacturing-occupation-competency-framework

[^mi_deloitte_2024]: The Manufacturing Institute and Deloitte. “Manufacturers Need as Many as 3.8 Million New Employees by 2033.” https://themanufacturinginstitute.org/manufacturers-need-as-many-as-3-8-million-new-employees-by-2033/

[^nsf_chips]: U.S. National Science Foundation. “CHIPS and Science.” https://www.nsf.gov/chips

[^eu_microcredentials]: European Commission, European Education Area. “A European approach to micro-credentials.” https://education.ec.europa.eu/education-levels/higher-education/micro-credentials

[^industry5_oeij]: Oeij, P. R. A., Lenaerts, K., Dhondt, S., Van Dijk, W., Schartinger, D., Sorko, S. R., & Warhurst, C. (2024). “A Conceptual Framework for Workforce Skills for Industry 5.0: Implications for Research, Policy and Practice.” Journal of Innovation Management. https://doi.org/10.24840/2183-0606_012.001_0010

[^onet]: U.S. Department of Labor. “O*NET.” https://www.dol.gov/agencies/eta/onet

[^esco]: European Commission. “European Skills/Competences, Qualifications and Occupations (ESCO).” https://employment-social-affairs.ec.europa.eu/policies-and-activities/skills-and-qualifications/skills-jobs/european-skillscompetences-qualifications-and-occupations-esco_en

[^lightcast_open_skills]: Lightcast. “Open Skills Taxonomy.” https://lightcast.io/open-skills

[^credential_engine_2025]: Credential Engine. “New Report Finds 1.85 Million Credentials and Opportunities for Learners, Workers, and Employers.” https://credentialengine.org/2025/12/09/new-report-finds-1-85-million-credentials-and-opportunities/

[^skillsvista_2025]: Skillsvista. “Identification and Analysis of the Advanced and Sustainable Manufacturing Future Skills on the Island of Ireland.” https://amtce.ie/wp-content/uploads/2025/06/Skillsvista-V2-report-2025_Digital-FINAL.pdf

[^mfgusa_report_to_congress]: Manufacturing USA. “2025 Report to Congress.” https://www.manufacturingusa.com/sites/manufacturingusa.com/files/2026-03/Manufacturing%20USA%20Report%20to%20Congress_2025_0.pdf

[^oecd_skills_first]: OECD. “Empowering the Workforce in the Context of a Skills-First Approach.” https://www.oecd.org/en/publications/empowering-the-workforce-in-the-context-of-a-skills-first-approach_345b6528-en.html

[^senger_2024]: Senger, E., Zhang, M., van der Goot, R., & Plank, B. (2024). “Deep Learning-based Computational Job Market Analysis: A Survey on Skill Extraction and Classification from Job Postings.” ACL Anthology. https://aclanthology.org/2024.nlp4hr-1.1/

[^course_skill_atlas]: Javadian Sabet, A., Bana, S. H., Yu, R., & Frank, M. R. (2024). “Course-Skill Atlas: A national longitudinal dataset of skills taught in U.S. higher education curricula.” Scientific Data. https://www.nature.com/articles/s41597-024-03931-8
