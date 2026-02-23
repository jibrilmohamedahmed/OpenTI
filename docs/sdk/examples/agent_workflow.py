
---

# **6. sdk/examples/agent_workflow.py**

```python
from sdk.agent_workflow import AgentOrchestrator

# Initialize orchestrator
orchestrator = AgentOrchestrator()

# Create agents
orchestrator.create_agent("research_agent")
orchestrator.create_agent("compliance_agent")

# Define workflow
orchestrator.define_workflow(
    ["research_agent", "compliance_agent"],
    workflow_graph="sample_graph"
)

# Execute workflow
orchestrator.execute_workflow("sample_graph")
