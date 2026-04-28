# Unified Agent Architecture

## Core stack

The system is built as a layered architecture rather than a single agent pattern.

- **Pillars** define long-lived domains.
- **Pistons** define repeatable action loops inside each pillar.
- **Diamond** defines decision geometry.
- **Spiral** defines recursive refinement.
- **Double Helix** defines paired truth/action strands.
- **Colossal Agent** defines top-level orchestration.

## Pillars

Recommended first pillars:

1. `pillar_legal_case_intelligence`
2. `pillar_memory_context`
3. `pillar_repos_code_automation`
4. `pillar_connectors_integrations`
5. `pillar_exports_ingestion`
6. `pillar_business_ops`
7. `pillar_personal_family`
8. `pillar_applications_outreach`

## Pistons

Universal piston set:

- `piston_ingest`
- `piston_classify`
- `piston_retrieve`
- `piston_compare`
- `piston_summarize`
- `piston_generate`
- `piston_audit`
- `piston_publish`

### Example: exports pillar

- `piston_ingest_raw_export`
- `piston_extract_metadata`
- `piston_classify_domain`
- `piston_identify_memory_candidates`
- `piston_write_summary`
- `piston_index_control_plane`
- `piston_mirror_github`
- `piston_mirror_dropbox`
- `piston_log_aspen`

## Diamond geometry

```text
           intent_router
          /             \
  research_node       build_node
          \             /
            critic_node
```

### Roles

- **Router**: interpret intent and select pillar/pistons
- **Research**: collect evidence, files, metadata, context
- **Build**: generate artifacts, code, docs, structured outputs
- **Critic**: contradiction check, quality check, missing-input detection

## Spiral engine

Recursive refinement loop:

1. read current state
2. detect gaps
3. improve structure
4. improve evidence
5. improve output
6. compress memory
7. re-index state

## Double helix

### Helix A — Truth
- facts
- evidence
- metadata
- structure

### Helix B — Action
- meaning
- strategy
- decisions
- next actions

The strands cross-link at every major cycle.

## Colossal agent

The Colossal Agent should coordinate rather than do every task directly.

Responsibilities:

- choose pillar
- activate pistons
- route through diamond
- run spiral passes
- align helix strands
- update memory layers
- emit artifacts and next actions

## Control flow

```text
user_intent
  -> colossal_orchestrator
  -> pillar_selection
  -> piston_activation
  -> diamond_cycle
  -> spiral_refinement
  -> double_helix_fusion
  -> artifact + memory update + audit log
```

## Why this stack works

- **Pillar** gives order
- **Piston** gives motion
- **Diamond** gives judgment
- **Spiral** gives evolution
- **Double Helix** gives depth
- **Colossal Agent** gives command
