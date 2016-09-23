from __future__ import print_function


class BlackBox:
    def __init__(self):
        self.position_record = []
        self.speed_record = []

    def record(self, position, speed):
        self.position_record.append(position)
        self.speed_record.append(speed)

    def make_report(self, file):
        for i, record in enumerate(zip(self.position_record, self.speed_record)):
            self.make_one_report(i, record, file)

    def make_one_report(self, time, record, file):
        position, speed = record
        print("At t={time}: x = {position}, s={speed}".format(time, position, speed), file=file)
