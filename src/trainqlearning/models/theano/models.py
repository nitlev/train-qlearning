import tensorflow as tf


class NeuralNetwork:
    def __init__(self, x, y, y_, session):
        self.x = x
        self.y = y
        self.y_ = y_
        self.session = session
        self.loss = tf.nn.l2_loss(self.y_ - self.y)
        self.train = tf.train.AdamOptimizer(5e-5).minimize(self.loss)

    def predict(self, states):
        self.session.run(tf.initialize_all_variables())

        y_pred = self.session.run(self.y_, feed_dict={self.x: states})
        return y_pred

    def train(self, records, targets):
        self.train.run(feed_dict={self.x: records, self.y: targets})