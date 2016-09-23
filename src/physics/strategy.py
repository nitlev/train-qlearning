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
    def __init__(self):
        Strategy.__init__(self)
        self.model = None

    def define_braking_strength(self, position, speed, objective):
        return self.model.predict(position, speed, objective)