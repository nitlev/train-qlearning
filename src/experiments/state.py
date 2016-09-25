class State:
    def __init__(self, episode_step):
        self.reward = compute_reward(episode_step)

    def save(self, record):
        record.save_state(self)


def compute_reward(episode_step):
    distance = episode_step.objective - episode_step.train.position
    return distance
