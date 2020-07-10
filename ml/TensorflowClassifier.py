from ml.ScenarioFormatter import ScenarioFormatter
from model.TrainingScenario import TrainingScenario
from model.PredictionScenario import PredictionScenario
from ml.Classifier import Classifier
import numpy as np
import tensorflow as tf


class TensorflowClassifier(Classifier):

    def __init__(self, scenario_formatter: ScenarioFormatter):
        super().__init__(scenario_formatter)
        self._index_label_mapper = {index: label for index, label in enumerate(scenario_formatter.get_label())}
        self._label_index_mapper = {label: index for index, label in enumerate(scenario_formatter.get_label())}
        self._feature_size = 0

    def train(self, dataset: [TrainingScenario]) -> float:
        (train_labels, train_rows), (test_labels, test_rows) = super().prepare_data_for_training(dataset)
        train_labels = [self._label_index_mapper[label] for label in train_labels]
        test_labels = [self._label_index_mapper[label] for label in test_labels]

        model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(32, activation='sigmoid'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(32, activation='tanh'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(16, activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(6, activation='relu')
        ])

        loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

        model.compile(optimizer='adam',
                      loss=loss_fn,
                      metrics=['accuracy'])

        history = model.fit(np.array(train_rows), np.array(train_labels), epochs=125)

        model.evaluate(np.array(test_rows), np.array(test_labels), verbose=2)

        # Probability model
        self._trained_model = model

        accuracy = history.history['accuracy']
        self.accuracy = accuracy[-1]
        self._scenario_formatter.feature_size = len(test_rows[0])
        return accuracy

    def predict(self, scenario: PredictionScenario):
        feature_scenario = np.array([self._scenario_formatter.format_entry(
            scenario.trace,
            scenario.fail_step_key_word
        )])
        formatted_scenario = feature_scenario.reshape((1, self._scenario_formatter.feature_size))
        predictions = self._trained_model.predict(formatted_scenario)[0]

        return [(self._index_label_mapper[index_label], prediction) for index_label, prediction in enumerate(predictions)]
