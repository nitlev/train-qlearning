import numpy as np
from numpy import random

class Strategy:
    def __init__(self):
        pass

    def define_braking_strength(self, position, speed, objective):
        pass


class ConstantBrakeStrategy(Strategy):
    def __init__(self, strength):
        Strategy.__init__(self)
        self.braking_strengh = strength

    def define_braking_strength(self, position, speed, objective):
        return self.braking_strengh


class DeepStrategy(Strategy):
    def __init__(self, model, session, epsilon=0.1):
        Strategy.__init__(self)
        self.session = session
        self.model = model
        self.epsilon = epsilon

    def define_braking_strength(self, position, speed, objective):
        r = random.rand()
        if r < self.epsilon:
            return random.choice(range(11)) / 10.
        else:
            states = [[position, speed, objective, brake / 10.] for brake in range(11)]
            preditions = self.model.predict(states=states, session=self.session)
            best_action = np.argmax(preditions) / 10.
            best_prediction = np.max(preditions)
            return best_action


