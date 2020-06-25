from ml.ScenarioFormatter import ScenarioFormatter
from model.TrainingScenario import TrainingScenario
from model.PredictionScenario import PredictionScenario
import numpy as np
from xgboost import XGBClassifier
import random
from sklearn.model_selection import RandomizedSearchCV


class XGBoostClassifier:

    def __init__(self, scenario_formatter: ScenarioFormatter):
        self._scenario_formatter = scenario_formatter
        self._trained_model = None
        self.accuracy = 0
        
    def train(self, dataset: [TrainingScenario]) -> float:
        (train_labels, train_rows), (test_labels, test_rows) = self._prepare_data_for_training(dataset)

        self._trained_model = XGBClassifier(
            learning_rate=0.02,
            n_estimators=600,
            objective='multi:softprob',
            silent=True,
            eval_set=[(test_rows, test_labels)],
            early_stopping_rounds=5,
        )

        params = {
            'min_child_weight': [1, 5, 10],
            'gamma': [0.5, 1, 1.5, 2, 5],
            'subsample': [0.6, 0.8, 1.0],
            'colsample_bytree': [0.6, 0.8, 1.0],
            'max_depth': [3, 4, 5]
        }

        randomized_search_cv = RandomizedSearchCV(
            self._trained_model,
            param_distributions=params,
            random_state=42,
            n_iter=10,
            cv=3,
            verbose=1,
            n_jobs=4,
            return_train_score=True
        )
        train_accuracy = randomized_search_cv.fit(train_rows, train_labels)
        self._trained_model = randomized_search_cv
        self.accuracy = train_accuracy.best_score_
        return train_accuracy.best_score_

    def _calculate_accuracy(self, dataset: [TrainingScenario]):
        good_prediction = 0
        total_entry = len(dataset)
        for training_scenario in dataset:
            prediction = max(self.predict(training_scenario), key=lambda e: e[0])[0]
            if training_scenario.training_label == prediction:
                good_prediction += 1
        return round(good_prediction/total_entry, 4)

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
