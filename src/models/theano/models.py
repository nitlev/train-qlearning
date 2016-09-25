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


class DeepQNetwork:
    def __init__(self, model, epsilon=0.1):
        self.model = model
        self.epsilon = epsilon

    def predict(self, position, speed, objective, session):
        r = random.rand()
        if r < self.epsilon:
            return random.choice(range(11)) / 10.
        else:
            states = [[position, speed, objective, brake / 10.] for brake in range(11)]
            preditions = self.model.predict(states=states, session=session)
            best_action = np.argmax(preditions) / 10.
            best_prediction = np.max(preditions)
            return best_action

    def train(self, records, targets):
        self.model.train(records, targets)


class ExperimentRecord:
    def __init__(self):
        self.states = []

    def record_state(self, state):
        self.states.append(state)

    def get_some_states(self, p=0.5):
        return np.random.choice(self.states, p=p)
