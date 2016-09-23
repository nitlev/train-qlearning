from lasagne.layers import InputLayer, DenseLayer
from lasagne.nonlinearities import linear
import Theano.tensor as T
from numpy import random


class DeepQNetworkFactory:
    def __init__(self, *layers):
        self._layers = layers

    def build(self):
        input_layer = InputLayer(3, name='input_layer')
        layer1 = DenseLayer(input_layer, 5)
        layer2 = DenseLayer(layer1, 5)
        layer3 = DenseLayer(layer2, 1, nonlinearity=linear)
        return layer3


class DeepQNetwork:
    def __init__(self, model, epsilon=0.1):
        self.model = model
        self.epsilon = epsilon

    def predict(self, position, speed, objective):
        r = random.rand()
        if r < self.epsilon:
            return 10 * random.rand()
        else:
            X_t = T.tensor4()
