from src.record import BlackBox
from src.strategy import ConstantBrakeStrategy
from src.train import Train

from src.physics.controler import Controler

__author__ = "veltin"

STANDARD_DURATION = 1
STANDARD_OBJECTIVE = 100
STANDARD_STRATEGY = ConstantBrakeStrategy(5)


class TestTrain:
    def test_train_should_move(self):
        train = Train(0, 10, Controler(STANDARD_OBJECTIVE, STANDARD_STRATEGY))
        train.move(STANDARD_DURATION)
        assert train.position == 10

    def test_train_should_move_and_take_into_account_duration(self):
        train = Train(0, 10, Controler(STANDARD_OBJECTIVE, STANDARD_STRATEGY))
        train.move(2 * STANDARD_DURATION)
        assert train.position == 20


class TestBlackBox:
    def test_black_box_should_record_new_data(self):
        bb = BlackBox()
        bb.record(1, 10)
        bb.record(2, 20)
        assert bb.position_record == [1, 2]
        assert bb.speed_record == [10, 20]


class TestControler:
    def test_train_speed_should_decrease_if_controler_brakes(self):
        controler = Controler(STANDARD_OBJECTIVE, STANDARD_STRATEGY)
        initial_speed = 10
        train = Train(0, initial_speed, controler)
        train.move(STANDARD_DURATION)
        assert train.speed <= initial_speed

    def test_a_controler_cannot_go_back(self):
        train = Train(0, 1, Controler(STANDARD_OBJECTIVE, STANDARD_STRATEGY))
        train.move(10)
        assert train.speed >= 0
