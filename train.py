from __future__ import print_function

import getopt
import sys

import tensorflow as tf
from src.models.theano.factories import NeuralNetworkFactory

from src.trainqlearning.experiments import Episode


def main(argv):
    opts, args = getopt.getopt(args=argv[1:], shortopts="hs:x:", longopts=["speed=", "xobjective="])

    if argv[0] == "train":
        pass
    elif argv[0] == "run":
        return run(opts)
    else:
        raise ValueError("valid arguments are train or run")


def run(opts):
    with tf.Session() as sess:
        model = NeuralNetworkFactory([1, 4], [4, 10, 10]).build(session=sess)
        episode = Episode(opts, model)
        episode.run()
        print(episode.record.transitions)


if __name__ == '__main__':
    argv = sys.argv
    main(argv[1:])
