from src.physics.record import BlackBox


class Train:
    def __init__(self, initial_position, initial_speed, controler, black_box=None):
        self.position = initial_position
        self.speed = initial_speed
        self.max_brake_strength = 10
        self.controler = controler
        self.controler.set_train(self)
        self.black_box = black_box or BlackBox()
        self.black_box.record(self.position, self.speed)

    def move(self, duration):
        self._update_position_and_speed(duration)
        self.black_box.record(self.position, self.speed)

    def _update_position_and_speed(self, duration):
        self._update_position(duration)
        self._update_speed(duration)

    def _update_position(self, duration):
        self.position += self.speed * duration

    def _update_speed(self, duration):
        self.controler.brake(duration)