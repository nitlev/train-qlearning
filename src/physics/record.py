from __future__ import print_function


class BlackBox:
    def __init__(self):
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

    @staticmethod
    def make_one_report(time, record, file):
        position, speed, brake = record
        print("At t={time}: x = {position}, s={speed} (b={brake})".format(time=time,
                                                                          position=position,
                                                                          speed=speed,
                                                                          brake=brake), file=file)
