# OpenTI Cognitive Memory Graph (CMG) v0.1

## Purpose
Defines an open standard for persistent cognition storage of autonomous agents.

---

## Node Types

| Node Type      | Description |
|----------------|------------|
| Agent          | AI entity with identity and state |
| Task           | Action executed by agent |
| Decision       | Outcome or reasoning result |
| Context        | Input knowledge/environment data |
| External Data  | Market, document, reference data |
| Policy         | Governance constraint |
| State          | Snapshot of agent/system state |

---

## Relationship Types

- Temporal: `before/after`  
- Causal: `caused_by`  
- Dependency: `depends_on`  
- Hierarchical: `parent/child`  
- Regulatory: `enforced_by_policy`  

---

## Required APIs

- Write cognition: `POST /cognition/write`  
- Query cognition: `GET /cognition/query`  
- Replay cognition: `POST /cognition/replay`  

---

## Determinism

Each node must include:
- Timestamp  
- Agent ID  
- Model hash  
- Execution environment hash  
- Applied policy hash  

---

## Interoperability

Supports integration with LangGraph, AutoGen, OpenAI Agents, and other agent frameworks.
