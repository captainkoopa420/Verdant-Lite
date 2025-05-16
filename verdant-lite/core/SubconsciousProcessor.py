import random

class SubconsciousProcessor:
    def __init__(self, memory_system):
        self.memory = memory_system

    def blend_thoughts(self):
        thoughts = list(self.memory.memory_store.keys())
        if len(thoughts) < 2:
            return
        t1, t2 = random.sample(thoughts, 2)
        hybrid = f"H-{t1}-{t2}"
        self.memory.add_thought(hybrid, stability=0.4)
        self.memory.connect_thoughts(t1, hybrid, weight=0.5)
        self.memory.connect_thoughts(t2, hybrid, weight=0.5)
        print(f"🎨 Blended Thought: {hybrid}")

    def perturb_thoughts(self):
        thoughts = list(self.memory.memory_store.keys())
        if not thoughts:
            return
        base = random.choice(thoughts)
        variant = f"V-{base}-{random.randint(1, 99)}"
        self.memory.add_thought(variant, stability=0.3)
        self.memory.connect_thoughts(base, variant, weight=0.3)
        print(f"🎭 Variant Created: {variant}")

    def recursive_expansion(self, base_thought, depth=2):
        if base_thought not in self.memory.memory_store or depth == 0:
            return
        expansion = f"M-{base_thought}-{random.randint(100,999)}"
        self.memory.add_thought(expansion, stability=0.2)
        self.memory.connect_thoughts(base_thought, expansion, weight=0.25)
        print(f"🔁 Expansion: {expansion}")
        self.recursive_expansion(expansion, depth-1)
