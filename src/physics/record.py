class BlackBox:
    def __init__(self):
        self.position_record = []
        self.speed_record = []

    def record(self, position, speed):
        self.position_record.append(position)
        self.speed_record.append(speed)