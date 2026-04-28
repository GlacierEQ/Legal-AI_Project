# Memory OS Control Plane

## Purpose

This document defines the control-plane architecture for a multi-layer memory system spanning MemoryPlugin, Airtable, GitHub, Dropbox, and Aspen Grove.

## Layer model

### 1. Bootstrap memory
**System:** MemoryPlugin

Use for:
- identity
- preferences
- standing operating rules
- active mission headline
- cross-model continuity

### 2. Live control plane
**System:** Airtable

Use for:
- systems registry
- task registry
- repo registry
- memory pointers
- applications registry
- export ingestion index
- Aspen event summary index

### 3. Durable source of truth
**System:** GitHub

Use for:
- code
- schemas
- docs
- bridge logic
- organized exports
- Aspen Grove raw logs

### 4. Archive mirror
**System:** Dropbox

Use for:
- raw exports
- large media
- evidence mirrors
- cold archive

### 5. Event spine
**System:** Aspen Grove

Use for:
- append-only event logging
- PR creation logs
- sync logs
- ingestion logs
- decision history

## Memory categories

1. identity / preferences
2. active missions
3. legal core
4. AI systems core
5. business / work
6. personal / family
7. applications / opportunities
8. event / audit memory
9. archive / cold storage

## Durable vs operational split

### Durable memory
Store:
- user preferences
- standing instructions
- active system architecture
- active case baseline
- durable project identities

### Operational memory
Store:
- active PRs
- active tasks
- current repo target
- latest ingestion state
- current blockers

### Event memory
Store:
- tool calls
- branch creation
- PR creation
- sync events
- export parse events

### Archive memory
Store:
- raw zips
- raw exports
- old prompt packs
- superseded designs
- old notes pending triage

## Airtable tables

### Systems
- Name
- Status
- Purpose
- Primary Repo
- Current Mission
- Bootstrap Memory
- Next Action

### Repos
- Repo Name
- GitHub URL
- Purpose
- Status
- Active PR
- Public Ready
- Risk Notes
- Next Commit

### Memory Pointers
- Pointer Name
- MemoryPlugin Command
- Scope
- Priority
- Last Used
- Notes

### Tasks
- Task
- Status
- Priority
- System
- Repo
- Owner Agent
- Next Step
- Evidence Link

### Applications
- Company
- Role
- URL
- Fit Score
- Status
- Statement of Exceptional Work
- Repo Link
- Outreach Target
- Next Action

### Aspen Events
- Event ID
- Timestamp
- Source Agent
- Event Type
- Repo
- Summary
- GitHub Link
- Raw JSON

## Folder structure

```text
MemoryOS/
  00_Control_Plane/
    systems/
    tasks/
    repos/
    applications/
    memory_pointers/
  01_Legal/
    case_1FDV-23-0001009/
      motions/
      orders/
      research/
      evidence/
      timelines/
      actor_profiles/
  02_AI_Systems/
    memory_architecture/
    bridge_core/
    agents/
    prompts/
    connectors/
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
  04_Business/
    hi-class-home-services/
  05_Personal/
    health/
    relationships/
    education/
  99_Archive/
    cold/
    legacy/
    unsorted/
```

## Design rule

- MemoryPlugin remembers the mission.
- Airtable tracks the state.
- GitHub stores the work.
- Dropbox mirrors the archive.
- Aspen Grove records what happened.
