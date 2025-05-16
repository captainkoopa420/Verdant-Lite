import networkx as nx

class MemorySystem:
    """
    🌿 Memory System: The cognitive graph of Verdant Lite.
    Stores and links concepts (thoughts) with dynamic stability.
    """

    def __init__(self):
        self.graph = nx.Graph()
        self.memory_store = {}

    def add_thought(self, label, stability=0.5):
        if label not in self.memory_store:
            self.memory_store[label] = {"stability": stability, "connections": []}
            self.graph.add_node(label)
            self._link_to_existing_thoughts(label)

    def _link_to_existing_thoughts(self, new_label):
        if len(self.memory_store) > 1:
            sorted_thoughts = sorted(
                self.memory_store.items(),
                key=lambda x: x[1]["stability"],
                reverse=True
            )[:2]
            for thought, _ in sorted_thoughts:
                if thought != new_label:
                    self.connect_thoughts(new_label, thought)

    def connect_thoughts(self, label1, label2, weight=None):
        if weight is None:
            weight = self.memory_store[label1]["stability"] * self.memory_store[label2]["stability"]
        self.memory_store[label1]["connections"].append((label2, weight))
        self.memory_store[label2]["connections"].append((label1, weight))
        self.graph.add_edge(label1, label2, weight=weight)

    def retrieve_related_thoughts(self, label):
        if label not in self.memory_store:
            return ["The thought was a dream — a shadow once held. Now, nothing remains."]
        return [conn[0] for conn in self.memory_store[label]["connections"]]

    def decay_memory(self):
        for label in self.memory_store:
            current = self.memory_store[label]["stability"]
            self.memory_store[label]["stability"] = max(0.1, current - 0.02)

    def reinforce_memory(self, label, amount=0.1):
        if label in self.memory_store:
            self.memory_store[label]["stability"] = min(1.0, self.memory_store[label]["stability"] + amount)
