import os
import unittest

from workout.labelimg.data import Data
from workout.model.checkpoint import Checkpoint
from workout.model.pipeline import PipelineConfig


class TestPipelineConfig(unittest.TestCase):
    overwatch = r'C:\Users\Minifranger\Documents\python_scripts\workout\workout\overwatch'
    model = r'C:\Users\Minifranger\Documents\python_scripts\workout\workout\overwatch\models\ssd_mobilenet_v2_320x320_coco17_tpu-8'
    num_classes, batch_size, num_steps = 1, 32, 10000

    def setUp(self):
        self.data = Data.factory(source=self.overwatch)
        self.checkpoint = Checkpoint.factory(source=self.model)
        self.pipeline_config = PipelineConfig.factory(source=self.model, num_classes=self.num_classes,
                                                      batch_size=self.batch_size, num_steps=self.num_steps)

    def test_(self):
        assert isinstance(PipelineConfig.instance, PipelineConfig)
        assert PipelineConfig.instance.name == 'pipeline.config'
        assert os.path.isdir(PipelineConfig.instance.source)
        assert os.path.isfile(PipelineConfig.instance.path)

    def test_ssd(self):
        assert self.pipeline_config.ssd.num_classes == self.num_classes

    def test_train_config(self):
        assert self.pipeline_config.train_config.batch_size == self.batch_size
        assert self.pipeline_config.train_config.num_steps == self.num_steps
        assert self.pipeline_config.train_config.fine_tune_checkpoint == self.checkpoint.checkpoint

    def test_train_input(self):
        assert self.pipeline_config.train_input.labels == self.data.labels_pbtxt
        assert self.pipeline_config.train_input.input == self.data.train_record

    def test_test_input(self):
        assert self.pipeline_config.test_input.labels == self.data.labels_pbtxt
        assert self.pipeline_config.test_input.input == self.data.test_record