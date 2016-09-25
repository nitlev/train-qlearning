import tensorflow as tf
import numpy as np
from numpy import random


class NeuralNetwork:
    def __init__(self, x, y, y_):
        self.x = x
        self.y = y
        self.y_ = y_
        self.loss = tf.nn.l2_loss(self.y_ - self.y)
        self.train = tf.train.AdamOptimizer(5e-5).minimize(self.loss)

    def predict(self, states, session):
        session.run(tf.initialize_all_variables())

        y_pred = session.run(self.y_, feed_dict={self.x: states})
        return y_pred

    def train(self, records, targets):
        self.train.run(feed_dict={self.x: records, self.y: targets})
