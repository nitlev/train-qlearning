class Train:
    def __init__(self, initial_position, initial_speed, controler, black_box, max_braking_power=5):
        self.position = initial_position
        self.speed = initial_speed
        self.current_brake_power = 0
        self.max_brake_power = max_braking_power
        self.controler = controler
        self.black_box = black_box

        self.controler.set_train(self)
        self.black_box.record(self.position, self.speed, self.current_brake_power)

    def move(self, duration):
        self._update_position_and_speed(duration)
        self.black_box.record(self.position, self.speed, self.current_brake_power)
        self.controler.brake()

    def _update_position_and_speed(self, duration):
        self._update_speed(duration)
        self._update_position(duration)

    def _update_position(self, duration):
        self.position += self.speed * duration

    def _update_speed(self, duration):
        self.speed = max(0, self.speed - self.current_brake_power * duration)
