from ml.ScenarioFormatter import ScenarioFormatter
from ml.InterestingWordListGenerator import interesting_word_list_generator
from ml.XGBoostClassifier import XGBoostClassifier
from model.TrainingScenario import TrainingScenario


def train_new_model(dataset: [TrainingScenario]) -> XGBoostClassifier:
    interesting_words = interesting_word_list_generator([(scenario.training_label, scenario.trace) for scenario in dataset])
    labels = list({scenario.training_label for scenario in dataset})
    scenario_formatter = ScenarioFormatter(interesting_words, labels)

    classifier = XGBoostClassifier(scenario_formatter)
    accuracy = classifier.train(dataset)
    return classifier
