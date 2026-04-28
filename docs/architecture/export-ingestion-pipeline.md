# ChatGPT / Grok Export Ingestion Pipeline

## Goal

Transform raw ChatGPT and Grok exports into structured, searchable, categorized knowledge that can be mirrored into GitHub and Dropbox and indexed in Airtable.

## Input

- raw zip export
- raw JSON / HTML / markdown / attachments

## Output per conversation

- `metadata.json`
- `summary.md`
- `facts.md`
- `projects.md`
- `actors.md`
- `actions.md`
- `memory_candidates.md`

## Classification axes

- model: chatgpt / grok
- domain: legal / AI / business / personal
- project
- case number
- actor
- artifact type
- urgency
- recurrence value

## Target folders

```text
03_Exports/
  chatgpt/
    raw/
    parsed/
    categorized/
    indexed/
  grok/
    raw/
    parsed/
    categorized/
    indexed/
```

## Pipeline by piston

### Pillar
`pillar_exports_ingestion`

### Pistons
1. `piston_ingest_raw_export`
2. `piston_unzip_or_parse`
3. `piston_extract_conversation_units`
4. `piston_extract_metadata`
5. `piston_classify_domain`
6. `piston_identify_projects`
7. `piston_identify_actors`
8. `piston_identify_memory_candidates`
9. `piston_write_summary`
10. `piston_write_index`
11. `piston_mirror_github`
12. `piston_mirror_dropbox`
13. `piston_log_aspen`

## Diamond pass

- **Router**: determine export type and processing route
- **Research**: extract facts, metadata, dates, actors, projects
- **Build**: produce categorized files and summaries
- **Critic**: verify categories, missing fields, contradictions, duplicate conversations

## Spiral passes

### Pass 1
- raw metadata
- file inventory
- attachment references

### Pass 2
- domain classification
- project mapping
- case linkage

### Pass 3
- actor extraction
- action extraction
- reusable prompt extraction

### Pass 4
- memory compression
- durable memory candidate selection
- event memory candidate selection

### Pass 5
- GitHub write
- Dropbox mirror
- Airtable index
- Aspen event log

## Double helix mapping

### Helix A — Truth
- files
- timestamps
- messages
- attachments
- explicit facts
- structured metadata

### Helix B — Action
- project value
- strategic use
- memory value
- next actions
- dependency mapping

## Reconstruction outputs

From multiple exports, reconstruct:
- master timeline
- actor maps
- motion issue matrix
- system architecture ideas
- memory candidates
- reusable prompts
- contradiction lists

## Mandatory ingestion rules

1. keep raw export untouched
2. never overwrite raw files
3. write parsed outputs separately
4. always generate a summary
5. always generate memory candidates
6. always generate an index record
7. always write an Aspen ingestion event
8. mirror structured outputs to GitHub and Dropbox

## Control-plane fields to populate

### Airtable: Exports Index (recommended additional table)
- Export ID
- Source Model
- Source File
- Date Imported
- Project
- Domain
- Case Number
- Key Actors
- Summary Path
- GitHub Path
- Dropbox Path
- Memory Candidate Count
- Aspen Event ID

## Why this matters

Raw exports are archive.
Structured outputs are knowledge.
Indexed outputs are operational memory.
