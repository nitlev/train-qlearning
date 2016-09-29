
class ConstantModel:
    def __init__(self, value):
        self.value = value

    def predict(self, states):
        return self.value

    def train(self, records, targets):
        pass
