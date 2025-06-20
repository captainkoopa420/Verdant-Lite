import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.MemorySystem import MemorySystem
from core.SubconsciousProcessor import SubconsciousProcessor
from core.ConsciousAgent import ConsciousAgent
from utils.visualization import visualize_memory_graph

memory = MemorySystem()
subconscious = SubconsciousProcessor(memory)
conscious = ConsciousAgent(memory, subconscious)

seed_concepts = ["Ethics", "Curiosity", "Emotion", "Knowledge", "Imagination"]
for concept in seed_concepts:
    print(f"🧠 Injecting Thought: {concept}")
    memory.add_thought(concept)

for cycle in range(5):
    print(f"\n🔄 Evolution Cycle {cycle+1}/5")
    subconscious.blend_thoughts()
    subconscious.perturb_thoughts()
    subconscious.recursive_expansion(seed_concepts[cycle % len(seed_concepts)], depth=2)
    decision = conscious.make_decision()
    if decision:
        memory.reinforce_memory(decision)
    memory.decay_memory()

visualize_memory_graph(memory)
