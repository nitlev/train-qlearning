from mock import MagicMock
from trainqlearning.experiments.episode import Episode
from trainqlearning.experiments.record import ExperimentRecord
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


class TestExperimentRecord:
    def setup(self):
        self.transition = MagicMock(spec=Transition)
        self.transition.reward = 0

    def test_record_should_store_transitions(self):
        record = ExperimentRecord()
        record.set_new_episode(0)
        record.save_transition(self.transition)
        assert len(record) == 1
        record.save_transition(self.transition)
        assert len(record) == 2

    def test_set_new_episode_should_add_new_row(self):
        record = ExperimentRecord()
        record.set_new_episode(0)
        record.save_transition(self.transition)
        record.set_new_episode(0)
        assert len(record.episodes) == 2

    def test_record_should_save_new_episode_to_new_set(self):
        record = ExperimentRecord()
        record.set_new_episode(0)
        record.set_new_episode(0)
        record.save_transition(self.transition)
        assert len(record.episodes[0]["transitions"]) == 0

    def test_record_method_get_last_should_return_last_transitions(self):
        record = ExperimentRecord()
        record.set_new_episode(0)
        for i in range(10):
            transition = MagicMock(spec=Transition)
            transition.reward = 0
            transition.name = "T" + str(i)
            record.save_transition(transition)
        assert [t.name for t in record.get_last_transitions(size=10)] == \
               ["T" + str(i) for i in range(10)]

    def test_record_method_get_last_should_return_n_last_transitions(self):
        record = ExperimentRecord()
        record.set_new_episode(0)
        for i in range(10):
            transition = MagicMock(spec=Transition)
            transition.reward = 0
            transition.name = "T" + str(i)
            record.save_transition(transition)
        assert [t.name for t in record.get_last_transitions(size=5)] == \
               ["T" + str(i) for i in range(5, 10)]

    def test_record_get_last_should_return_even_when_n_episodes(self):
        record = ExperimentRecord()
        record.set_new_episode(0)
        for i in range(10):
            transition = MagicMock(spec=Transition)
            transition.reward = 0
            transition.name = "T" + str(i)
            record.save_transition(transition)
            if i % 2 == 0:
                record.set_new_episode(0)
        assert [t.name for t in record.get_last_transitions(size=10)] == \
               ["T" + str(i) for i in range(10)]

    def test_record_method_get_some_should_return_n_transitions(self):
        record = ExperimentRecord()
        record.set_new_episode(0)
        for i in range(10):
            record.save_transition(self.transition)
        assert len(record.get_some_transitions(size=10)) == 10

    def test_record_method_get_some_should_return_n_last_transitions(self):
        record = ExperimentRecord()
        record.set_new_episode(0)
        for i in range(10):
            record.save_transition(self.transition)
        assert len(record.get_some_transitions(size=5)) == 5

    def test_record_get_some_should_return_even_when_n_episodes(self):
        record = ExperimentRecord()
        record.set_new_episode(0)
        for i in range(10):
            record.save_transition(self.transition)
            if i % 2 == 0:
                record.set_new_episode(0)
        assert len(record.get_some_transitions(size=10)) == 10
