class ExperimentRecord:
    def __init__(self):
        self.states = []

    def record_state(self, state):
        self.states.append(state)

    def get_some_states(self, p=0.5):
        return np.random.choice(self.states, p=p)
