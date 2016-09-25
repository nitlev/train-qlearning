from __future__ import print_function
import getopt
import sys
import tensorflow as tf

from src.physics.record import BlackBox


def main(argv):
    opts, args = getopt.getopt(args=argv[1:], shortopts="hs:x:", longopts=["speed=", "xobjective="])

    if argv[0] == "train":
        pass
    elif argv[0] == "run":
        return run(opts)
    else:
        raise ValueError("valid arguments are train or run")


def run(opts):
    from src.physics.strategy import DeepStrategy
    from src.physics.controler import Controler
    from src.physics.train import Train

    objective, speed = parse_args(opts)

    with tf.Session() as sess:
        controler = Controler(objective, DeepStrategy(session=sess))
        train = Train(initial_position=0,
                      initial_speed=speed,
                      controler=controler,
                      black_box=BlackBox(objective),
                      max_braking_power=3)
        while train.speed > 0:
            train.move(1)

    train.black_box.make_report(sys.stdout)


def parse_args(opts):
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
    return objective, speed

if __name__ == '__main__':
    argv = sys.argv
    main(argv[1:])
