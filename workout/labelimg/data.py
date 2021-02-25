import os
import logging
from workout.labelimg.images import Images
from workout.labelimg.labels import Labels
from workout.labelimg.test import Test
from workout.labelimg.train import Train
from workout.utils import Source

logger = logging.getLogger(__name__)


class Data(Source):
    """ directory containing all labelimg data """
    name = 'data'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        kwargs.pop('source')
        Images.factory(source=self.path)
        Labels.factory(source=self.path)
        Train.factory(source=self.path)
        Test.factory(source=self.path, **kwargs)

    @property
    def images(self):
        return Images.instance

    @property
    def labels(self):
        return Labels.instance

    @property
    def train(self):
        return Train.instance

    @property
    def test(self):
        return Test.instance

    @property
    def labels_pbtxt(self):
        return os.path.join(self.path, 'labels.pbtxt')

    @property
    def train_records(self):
        return os.path.join(self.path, 'train.record')

    @property
    def test_records(self):
        return os.path.join(self.path, 'test.record')