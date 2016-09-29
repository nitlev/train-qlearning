from __future__ import print_function
import sys

from src.trainqlearning.experiments.record import ExperimentRecord
from src.trainqlearning.experiments.targets import mini_batch_train_set
from src.trainqlearning.experiments.transitions import Transition
from src.trainqlearning.physics.record import BlackBox
from src.trainqlearning.physics.controler import Controler
from src.trainqlearning.physics.strategy import DeepStrategy
from src.trainqlearning.physics.train import Train


class Episode:
    def __init__(self, args, model=None, train=None, controler=None,
                 record=None):
        objective, speed = parse_args(args)
        self.record = record or ExperimentRecord()
        self.controler = controler or Controler(objective, DeepStrategy(model))
        self.model = self.controler.strategy.model
        self.train = train or Train(initial_position=0,
                                    initial_speed=speed,
                                    controler=self.controler,
                                    black_box=BlackBox(objective))

    def run(self, learn=False):
        while self.train.speed > 0:
            self.train.move(1)
            Transition(self).save(record=self.record)
            x, y = mini_batch_train_set(self)
            if learn:
                self.model.train(x, y)
        #self.train.black_box.make_report(sys.stdout)


def parse_args(args):
    x_objective = None
    initial_speed = None

    for opt, arg in args:
        if opt == "-h":
            print("python train.py run -x "
                  "x_coordinate_of_objective -s initial_speed")
            sys.exit(2)
        if opt == "-x":
            x_objective = int(arg)
        if opt == "-s":
            initial_speed = int(arg)

    objective = x_objective or 100
    speed = initial_speed or 10
    return objective, speed
