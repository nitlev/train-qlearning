from __future__ import print_function

import getopt
import sys

import tensorflow as tf

from src.trainqlearning.experiments.record import ExperimentRecord
from src.trainqlearning.models.tensorflow.factories import NeuralNetworkFactory
from src.trainqlearning.experiments.episode import Episode


def main(argv):
    opts, args = getopt.getopt(args=argv[1:], shortopts="hs:x:n:",
                               longopts=["speed=", "xobjective="])

    if argv[0] == "train":
        pass
    elif argv[0] == "run":
        return run(opts)
    else:
        raise ValueError("valid arguments are train or run")


def run(opts):
    with tf.Session() as sess:
        n, opts = get_n(opts)
        model = NeuralNetworkFactory([1, 4], [4, 10, 10]).build(session=sess)
        record = ExperimentRecord()
        for i in range(n):
            episode = Episode(opts, episode_id=i, model=model, record=record)
            episode.run(learn=True)
            if i % 100 == 0:
                print('\r', "Episode " + str(i), end='')
        print()
        print(record[-1])
        print()
        print(record.rewards)


def get_n(opts):
    n_tuple = [x for x in opts if x[0] == '-n']
    if len(n_tuple) == 0:
        return 10, opts
    else:
        return int(n_tuple[0][1]), [x for x in opts if x[0] != '-n']


if __name__ == '__main__':
    argv = sys.argv
    main(argv[1:])
