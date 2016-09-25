from src.experiments.state import State, PreviousState


class Transition:
    def __init__(self, episode_step):
        self.reward = compute_reward(episode_step)
        self.previous_brake_power = episode_step.train.black_box.braking_record[-1]
        self.state = State(episode_step)
        self.previous_state = PreviousState(episode_step)

    def save(self, record):
        record.save_transition(self)

    def __repr__(self):
        return "Transition(Reward {reward}, Brake {brake}, " \
               "{state}, {previous_state})".format(reward=self.reward,
                                                   brake=self.previous_brake_power,
                                                   state=self.state,
                                                   previous_state=self.previous_state)


def compute_reward(episode_step):
    distance = episode_step.train.controler.objective - episode_step.train.position
    if abs(distance) < 1:
        return 1000
    else:
        return -1
