class Controler:
    def __init__(self, objective, strategy):
        self.train = None
        self.objective = objective
        self.strategy = strategy

    def set_train(self, train):
        self.train = train

    @property
    def position(self):
        return self.train.position

    @property
    def speed(self):
        return self.train.speed

    def brake(self):
        brake_power = self.strategy.define_braking_strength(self.position,
                                                            self.speed,
                                                            self.objective)
        self._brake_with_force(brake_power)

    def _brake_with_force(self, brake_power):
        actual_brake_power = min(self.train.max_brake_power * brake_power,
                                 self.train.max_brake_power)
        self.train.current_brake_power = actual_brake_power
