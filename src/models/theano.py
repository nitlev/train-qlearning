import tensorflow as tf
from numpy import random


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.001)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


class DeepQNetworkFactory:
    def __init__(self, input_shape, *layers):
        self.input_shape = input_shape
        self._layers = layers

    def build(self):
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

        return DeepQNetwork(NeuralNetwork(x, y, y_pred))


class DeepQNetwork:
    def __init__(self, model, epsilon=0.1):
        self.model = model
        self.epsilon = epsilon

    def predict(self, position, speed, objective):
        r = random.rand()
        if r < self.epsilon:
            return random.rand()
        else:
            return self.model.predict(vector=[[position, speed, objective]])


class NeuralNetwork:
    def __init__(self, x, y, y_):
        self.x = x
        self.y = y
        self.y_ = y_

    def predict(self, vector):
        with tf.Session() as sess:
            sess.run(tf.initialize_all_variables())

            y_pred = sess.run(self.y_, feed_dict={self.x: vector})
            return y_pred