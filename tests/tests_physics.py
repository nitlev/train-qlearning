from trainqlearning.physics.record import BlackBox
from trainqlearning.physics.strategy import ConstantBrakeStrategy
from trainqlearning.physics.controler import Controler
from trainqlearning.physics.train import Train

__author__ = "veltin"

STANDARD_DURATION = 1
STANDARD_OBJECTIVE = 100
STANDARD_STRATEGY = ConstantBrakeStrategy(5)


class TestTrain:
    def test_train_should_move(self):
        train = Train(0, 10, Controler(STANDARD_OBJECTIVE, STANDARD_STRATEGY), BlackBox(STANDARD_OBJECTIVE))
        train.move(STANDARD_DURATION)
        assert train.position == 10

    def test_train_should_move_and_take_into_account_duration(self):
        train = Train(0, 10, Controler(STANDARD_OBJECTIVE, STANDARD_STRATEGY), BlackBox(STANDARD_OBJECTIVE))
        train.move(2 * STANDARD_DURATION)
        assert train.position == 20


class TestBlackBox:
    def test_black_box_should_record_new_data(self):
        bb = BlackBox(100)
        bb.record(1, 10, 0)
        bb.record(2, 20, 1)
        assert bb.position_record == [1, 2]
        assert bb.speed_record == [10, 20]
        assert bb.braking_record == [0, 1]


class TestControler:
    def test_train_speed_should_decrease_if_controler_brakes(self):
        controler = Controler(STANDARD_OBJECTIVE, STANDARD_STRATEGY)
        initial_speed = 10
        train = Train(0, initial_speed, controler, BlackBox(STANDARD_OBJECTIVE))
        train.move(STANDARD_DURATION)
        assert train.speed <= initial_speed

    def test_a_controler_cannot_go_reverse(self):
        train = Train(0, 1, Controler(STANDARD_OBJECTIVE, STANDARD_STRATEGY), BlackBox(STANDARD_OBJECTIVE))
        train.move(10)
        assert train.speed >= 0

    def test_a_controler_cannot_brake_harder_than_train_max_brake(self):
        train = Train(initial_position=0,
                      initial_speed=20,
                      max_braking_power=10,
                      controler=Controler(STANDARD_OBJECTIVE,
                                          ConstantBrakeStrategy(20)),
                      black_box=BlackBox(STANDARD_OBJECTIVE))
        train.move(1)
        assert train.current_brake_power == 10
