class State:
    def __init__(self, position=None, speed=None, episode_step=None):
        self.position = position if position is not None else \
            episode_step.train.position
        self.speed = speed if speed is not None else episode_step.train.speed

    def __repr__(self):
        return "State(Position {position}, " \
               "Speed {speed})".format(position=self.position,
                                       speed=self.speed)


class PreviousState(State):
    def __init__(self, position=None, speed=None, episode_step=None):
        State.__init__(self, position, speed, episode_step)
        box = episode_step.train.black_box
        self.position = position if position is not None else \
            box.position_record[-2]
        self.speed = speed if speed is not None else box.speed_record[-2]
