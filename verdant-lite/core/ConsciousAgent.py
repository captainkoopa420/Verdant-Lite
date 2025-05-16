# ConsciousAgent.py

import random

class ConsciousAgent:
    """
    👁️ Conscious Agent: Selects meaningful thoughts and chooses action.
    """

    def __init__(self, memory_system, subconscious, decision_threshold=0.6):
        self.memory = memory_system
        self.subconscious = subconscious
        self.threshold = decision_threshold
        self.past_decisions = []

    def make_decision(self):
        """Evaluates top thoughts and picks the most resonant one."""
        candidates = sorted(
            self.memory.memory_store.items(),
            key=lambda x: x[1]["stability"],
            reverse=True
        )
        if not candidates:
            return None

        top = candidates[0][0]
        score = self.evaluate(top)
        if score >= self.threshold:
            print(f"✅ DECISION: {top} (Score: {score:.2f})")
            self.past_decisions.append((top, score))
            return top
        else:
            print(f"⏸️ Skipped: {top} (Score: {score:.2f})")
            return None

    def evaluate(self, label):
        """Calculates a synthetic decision score."""
        base = self.memory.memory_store[label]["stability"]
        related = self.memory.retrieve_related_thoughts(label)
        connection_weight = sum(
            self.memory.memory_store[c]["stability"]
            for c in related if c in self.memory.memory_store
        ) / (len(related) + 1)
        noise = random.uniform(0.8, 1.2)
        return ((base + connection_weight) / 2) * noise
