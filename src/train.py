class Train:
    def __init__(self, initial_position, initial_speed, controler):
        self.position = initial_position
        self.speed = initial_speed
        self.controler = controler
        self.controler.set_train(self)
        self.max_brake_strength = 10

    def move(self, duration):
        self._update_position_and_speed(duration)

    def _update_position_and_speed(self, duration):
        self._update_position(duration)
        self._update_speed(duration)

    def _update_position(self, duration):
        self.position += self.speed * duration

    def _update_speed(self, duration):
        self.controler.brake(duration)