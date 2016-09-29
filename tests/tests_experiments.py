from mock import MagicMock
from trainqlearning.experiments.episode import Episode
from trainqlearning.experiments.transitions import Transition
from trainqlearning.physics.strategy import ConstantBrakeStrategy
from trainqlearning.physics.controler import Controler
from trainqlearning.experiments.state import State

from trainqlearning.experiments.targets import compute_q_value


class TestEpisode:
    def test_train_speed_should_be_zero_at_the_end_of_the_episode(self):
        controler = Controler(100, ConstantBrakeStrategy(5))
        episode = Episode([], controler=controler)
        episode.run()
        assert episode.train.speed == 0


class TestTargets:
    def test_compute_q_value_should_return_reward_if_final_state(self):
        state = State(position=100, speed=0)
        previous_state = State(position=90, speed=10)
        transition = MagicMock(spec=Transition)
        transition.state = state
        transition.previous_state = previous_state
        transition.reward = 10
        q_value = compute_q_value(transition, None, 0)
        assert q_value == 10

    def test_compute_q_value_should_reward_plus_max_q_value(self):
        state = State(position=100, speed=10)
        previous_state = State(position=90, speed=10)
        transition = MagicMock(spec=Transition)
        transition.state = state
        transition.previous_state = previous_state
        transition.reward = 10
        transition.previous_brake_power = 0

        model = MagicMock()
        model.predict.return_value = [0, 3, 2, 1]
        q_value = compute_q_value(transition, model, 0)
        assert q_value == 13
