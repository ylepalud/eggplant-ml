from ml.ScenarioFormatter import ScenarioFormatter
from model.TrainingScenario import TrainingScenario
from model.PredictionScenario import PredictionScenario
import numpy as np
import xgboost as xgb
import random


class XGBoostClassifier:

    def __init__(self, scenario_formatter: ScenarioFormatter):
        self._scenario_formatter = scenario_formatter
        self._trained_model = None
        self.accuracy = None
        
    def train(self, dataset: [TrainingScenario]) -> float:
        (train_labels, train_rows), (test_labels, test_rows) = self._prepare_data_for_training(dataset)
        self._trained_model = xgb.XGBClassifier(
            learning_rate=0.8,
            n_estimators=140,
            max_depth=9,
            min_child_weight=1,
            gamma=0.3,
            subsample=0.8,
            colsample_bytree=0.9,
            scale_pos_weight=1,
            objective='multi:softprob',
            reg_lambda=1,
            reg_alpha=0
        ).fit(
            train_rows,
            train_labels,
            eval_metric='auc'
        )
        test_predictions = self._trained_model.predict(test_rows)
        good_prediction = sum(
            [1 for pred, true_label in zip(test_predictions, test_labels) if pred == true_label])

        accuracy = round(good_prediction / len(test_predictions.tolist()), 5) * 100
        self.accuracy = round(accuracy, 3)
        return self.accuracy
        
    def _prepare_data_for_training(self, dataset: [TrainingScenario]):
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

    def predict(self, scenario: PredictionScenario):
        formatted_scenario = np.array([self._scenario_formatter.format_entry(
            scenario.trace,
            scenario.fail_step_key_word
        )])
        prediction = self._trained_model.predict_proba(formatted_scenario)[0]
        return [(label, prediction) for label, prediction in zip(self._scenario_formatter.get_label(), prediction)]
