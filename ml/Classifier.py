from ml.ScenarioFormatter import ScenarioFormatter
from model.TrainingScenario import TrainingScenario
from model.PredictionScenario import PredictionScenario
import random
import numpy as np


class Classifier:

    def __init__(self, scenario_formatter: ScenarioFormatter):
        self._scenario_formatter = scenario_formatter
        self._trained_model = None
        self.accuracy = 0

    def train(self, dataset: [TrainingScenario]) -> float:
        pass

    def predict(self, scenario: PredictionScenario):
        pass

    def prepare_data_for_training(self, dataset: [TrainingScenario]):
        row_data = []
        for trainingScenario in dataset:
            label = trainingScenario.training_label
            row = self._scenario_formatter.format_entry(
                trainingScenario.trace,
                trainingScenario.fail_step_key_word
            )
            row_data.append((label, row))

        random.shuffle(row_data)
        split_index = int(len(dataset) * 0.8)
        features = []
        labels = []
        for pair in row_data:
            label, feature = pair[0], pair[1]
            features.append(feature)
            labels.append(label)

        x_train = np.array(features[:split_index])
        x_test = np.array(features[split_index:])
        y_train = np.array(labels[:split_index])
        y_test = np.array(labels[split_index:])

        return (y_train, x_train), (y_test, x_test)
