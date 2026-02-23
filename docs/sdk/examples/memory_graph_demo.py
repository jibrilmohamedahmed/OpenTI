from sdk.memory_graph import CognitiveMemory

memory = CognitiveMemory()

# Write node
memory.write_memory("decision_001", {"outcome": "buy", "confidence": 0.92})

# Link node to context
memory.link_memory("decision_001", "context_market_data")

# Query memory
result = memory.read_memory({"agent": "research_agent"})
print("Memory query result:", result)
