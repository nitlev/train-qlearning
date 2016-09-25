from src.models.theano import DeepQNetworkFactory


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
    def __init__(self, session):
        Strategy.__init__(self)
        self.session = session
        self.model = DeepQNetworkFactory([1, 3], [10, 10, 1]).build()

    def define_braking_strength(self, position, speed, objective):
        return self.model.predict(position, speed, objective, self.session)
