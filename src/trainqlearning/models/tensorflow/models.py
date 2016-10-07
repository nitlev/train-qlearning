import tensorflow as tf


class NeuralNetwork:
    def __init__(self, x, y, y_, session):
        self.x = x
        self.y = y
        self.y_ = y_
        self.session = session
        self.loss = tf.nn.l2_loss(self.y_ - self.y)
        self.train_method = tf.train.AdamOptimizer(0.1).minimize(self.loss)
        self.session.run(tf.initialize_all_variables())

    def predict(self, states):
        y_pred = self.session.run(self.y_, feed_dict={self.x: states})
        return y_pred

    def train(self, records, targets):
        self.train_method.run(feed_dict={self.x: records, self.y: targets})
