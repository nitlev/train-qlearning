import numpy as np


class ExperimentRecord:
    def __init__(self):
        self.transitions = []

    def save_transition(self, transition):
        self.transitions.append(transition)

    def get_last_transitions(self, size=10):
        m = min(size, len(self.transitions))
        return self.transitions[-m:]

    def get_some_transitions(self, size=10):
        return np.random.choice(self.transitions,
                                size=min(size, len(self.transitions)))
