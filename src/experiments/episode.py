import sys

from src.physics.record import BlackBox
from src.physics.strategy import DeepStrategy
from src.physics.controler import Controler
from src.physics.train import Train


class Episode:
    def __init__(self, args, model=None, train=None, controler=None):
        objective, speed = parse_args(args)
        self.model = model
        self.controler = controler or Controler(objective, DeepStrategy(model))
        self.train = train or Train(initial_position=0,
                                    initial_speed=speed,
                                    controler=self.controler,
                                    black_box=BlackBox(objective))

    def run(self):
        while self.train.speed > 0:
            self.train.move(1)
        self.train.black_box.make_report(sys.stdout)


def parse_args(args):
    x_objective = None
    initial_speed = None

    for opt, arg in args:
        if opt == "-h":
            print("python train.py run -x x_coordinate_of_objective -s initial_speed")
            sys.exit(2)
        if opt == "-x":
            x_objective = int(arg)
        if opt == "-s":
            initial_speed = int(arg)

    objective = x_objective or 100
    speed = initial_speed or 10
    return objective, speed
