from src.trainqlearning.experiments.episode import Episode
from src.trainqlearning.physics.strategy import ConstantBrakeStrategy
from src.trainqlearning.physics.controler import Controler


class TestEpisode:
    def test_train_speed_should_be_zero_at_the_end_of_the_episode(self):
        controler = Controler(100, ConstantBrakeStrategy(5))
        episode = Episode([], controler=controler)
        episode.run()
        assert episode.train.speed == 0
