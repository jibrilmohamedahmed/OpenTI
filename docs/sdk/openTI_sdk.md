# OpenTI SDK v0.1

The OpenTI SDK provides the tools to deploy deterministic, persistent, and governed multi-agent AI systems.

---

## Modules

### 1. Agent Orchestration API

Provides deterministic multi-agent execution.

**Functions:**
- `create_agent(agent_id, config)` – Initializes a new agent  
- `define_workflow(agent_list, workflow_graph)` – Define sequential/parallel workflows  
- `execute_workflow(workflow_id)` – Execute a defined workflow  
- `terminate_agent(agent_id)` – Safely terminate an agent  

---

### 2. Cognitive Memory API

Persistent cognition layer for agents.

**Functions:**
- `write_memory(node_id, data)` – Write a node to the Cognitive Memory Graph  
- `read_memory(query)` – Query memory nodes  
- `link_memory(node_a, node_b)` – Connect two memory nodes  
- `snapshot_cognition()` – Create a snapshot of agent/system state  

---

### 3. Governance & Policy API

Control plane for institutional compliance.

**Functions:**
- `define_policy(policy_id, rules)` – Create governance rules  
- `enforce_policy(agent_id)` – Apply policy to an agent  
- `permission_control(entity_id, access_level)` – Role-based access  
- `compute_budget_limit(agent_id)` – Apply cost or resource limits  

---

### 4. Replay & Audit API

Enables deterministic reproducibility.

**Functions:**
- `replay_decision(trace_id)` – Replay a decision path  
- `export_audit_log()` – Export logs for regulatory audit  
- `compare_runs(run_A, run_B)` – Compare two executions  

---

### Example Usage

```python
from sdk.agent_workflow import AgentOrchestrator

orchestrator = AgentOrchestrator()
orchestrator.create_agent("alpha_bot")
orchestrator.define_workflow(["alpha_bot"], workflow_graph="sample_graph")
orchestrator.execute_workflow("sample_graph")
