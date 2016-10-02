import numpy as np


class ExperimentRecord:
    def __init__(self):
        self.episodes = []

    @property
    def all_transitions(self):
        return [x for episode in self.episodes for x in episode["transitions"]]

    @property
    def rewards(self):
        return [e["reward"] for e in self.episodes]

    def set_new_episode(self, episode_id):
        self.episodes.append({"episode_id": episode_id,
                              "transitions": [],
                              "reward": 0})

    def save_transition(self, transition):
        self.episodes[-1]["transitions"].append(transition)
        self.episodes[-1]["reward"] += transition.reward

    def get_last_transitions(self, size=10):
        m = min(size, len(self.all_transitions))
        return self.all_transitions[-m:]

    def get_some_transitions(self, size=10):
        return np.random.choice(self.all_transitions,
                                size=min(size, len(self.all_transitions)))

    def __len__(self):
        return len(self.all_transitions)

    def __repr__(self):
        return "\n".join([str(episode) for episode in self.episodes])
