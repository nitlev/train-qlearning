class Controler:
    def __init__(self, objetive, strategy):
        self.train = None
        self.objective = objetive
        self.strategy = strategy

    def set_train(self, train):
        self.train = train

    @property
    def position(self):
        return self.train.position

    @property
    def speed(self):
        return self.train.speed

    def brake(self, duration):
        brake_strength = self.strategy.define_braking_strength(self.position, self.speed, self.objective)
        self._brake_with_force(brake_strength, duration)

    def _brake_with_force(self, brake_strength, duration):
        actual_brake_strength = min(brake_strength, self.train.max_brake_strength)
        self.train.speed = max(0, self.train.speed - actual_brake_strength * duration)
