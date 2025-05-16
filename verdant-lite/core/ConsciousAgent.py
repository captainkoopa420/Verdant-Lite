from core.MemorySystem import MemorySystem
from core.SubconsciousProcessor import SubconsciousProcessor
from core.ConsciousAgent import ConsciousAgent

class SyntheticMind:
    def __init__(self):
        self.memory = MemorySystem()
        self.subconscious = SubconsciousProcessor(self.memory)
        self.conscious = ConsciousAgent(self.memory, self.subconscious)

    def inject(self, concept, stability=0.5):
        print(f"🧠 Injecting: {concept}")
        self.memory.add_thought(concept, stability)

    def evolve(self, cycles=5):
        for i in range(cycles):
            print(f"\n🔄 Cognitive Cycle {i+1}/{cycles}")
            self.subconscious.blend_thoughts()
            self.subconscious.perturb_thoughts()
            base = self.select_seed(i)
            if base:
                self.subconscious.recursive_expansion(base, depth=2)
            decision = self.conscious.make_decision()
            if decision:
                self.memory.reinforce_memory(decision)
            self.memory.decay_memory()

    def select_seed(self, i):
        thoughts = list(self.memory.memory_store.keys())
        return thoughts[i % len(thoughts)] if thoughts else None
