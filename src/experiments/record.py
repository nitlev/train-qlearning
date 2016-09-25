import numpy as np


class ExperimentRecord:
    def __init__(self):
        self.transitions = []

    def save_transition(self, state):
        self.transitions.append(state)

    def get_some_transitions(self, size=10):
        return np.random.choice(self.transitions, size=size)
