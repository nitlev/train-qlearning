class State:
    def __init__(self, episode_step):
        self.position = episode_step.train.position
        self.speed = episode_step.train.speed

    def __repr__(self):
        return "State(Position {position}, Speed {speed})".format(position=self.position,
                                                                  speed=self.speed)


class PreviousState:
    def __init__(self, episode_step):
        self.position = episode_step.train.black_box.position_record[-2]
        self.speed = episode_step.train.black_box.speed_record[-2]

    def __repr__(self):
        return "State(Position {position}, Speed {speed})".format(position=self.position,
                                                                  speed=self.speed)


def compute_reward(episode_step):
    distance = episode_step.train.controler.objective - episode_step.train.position
    if abs(distance) < 1:
        return 1000
    else:
        return -1
