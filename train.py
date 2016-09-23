from __future__ import print_function
import getopt
import sys


def main(argv):
    opts, args = getopt.getopt(args=argv[1:], shortopts="hs:x:", longopts=["speed=", "xobjective="])

    if argv[0] == "train":
        pass
    elif argv[0] == "run":
        return run(opts)
    else:
        raise ValueError("valid arguments are train or run")


def run(opts):
    from src.physics.strategy import ConstantBrakeStrategy
    from src.physics.controler import Controler
    from src.physics.train import Train

    x_objective = None
    initial_speed = None
    for opt, arg in opts:
        if opt == "-h":
            print("python train.py run -x x_coordinate_of_objective -s initial_speed")
            sys.exit(2)
        if opt == "-x":
            x_objective = int(arg)
        if opt == "-s":
            initial_speed = int(arg)

    objective = x_objective or 100
    speed = initial_speed or 10
    strategy = ConstantBrakeStrategy(15)
    controler = Controler(objective, strategy)
    train = Train(0, speed, controler)
    while train.speed > 0:
        print("Train currently at x={} (s={})".format(train.position, train.speed))
        train.move(1)
    print("Train stopped at x={} (objective was {})".format(train.position, objective))


if __name__ == '__main__':
    argv = sys.argv
    main(argv[1:])
