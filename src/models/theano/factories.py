import tensorflow as tf

from src.models.theano.models import NeuralNetwork


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.01)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


class NeuralNetworkFactory:
    def __init__(self, input_shape, layers):
        self.input_shape = input_shape
        self._layers = layers

    def build(self, session):
        x = tf.placeholder("float", shape=[None, self.input_shape[1]], name="x")
        y = tf.placeholder("float", shape=[None], name="y")

        Nout0 = 10
        Nout1 = 10

        W0 = weight_variable([self.input_shape[1], Nout0])
        b0 = bias_variable([Nout0])

        W1 = weight_variable([Nout0, Nout1])
        b1 = bias_variable([Nout1])

        W2 = weight_variable([Nout1, 1])
        b2 = bias_variable([1])

        hidden0 = tf.nn.relu(tf.matmul(x, W0) + b0)
        hidden1 = tf.nn.relu(tf.matmul(hidden0, W1) + b1)
        y_pred = tf.nn.relu6(tf.matmul(hidden1, W2) + b2) / 6

        return NeuralNetwork(x, y, y_pred, session)
