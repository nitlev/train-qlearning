class BlackBox:
    def __init__(self, objective):
        self.objective = objective
        self.position_record = []
        self.speed_record = []
        self.braking_record = []

    def record(self, position, speed, brake_power):
        self.position_record.append(position)
        self.speed_record.append(speed)
        self.braking_record.append(brake_power)

    def make_report(self, file):
        for i, record in enumerate(zip(self.position_record, self.speed_record, self.braking_record)):
            self.make_one_report(i, record, file)
        self.describe_result(file)

    @staticmethod
    def make_one_report(time, record, file):
        position, speed, brake = record
        print("At t={time}: x = {position}, s={speed} (b={brake})".format(time=time,
                                                                          position=position,
                                                                          speed=speed,
                                                                          brake=brake),
              file=file)

    def describe_result(self, file):
        print("Train stopped at x = {end}; objective was {objective}".format(end=self.position_record[-1],
                                                                             objective=self.objective),
              file=file)
