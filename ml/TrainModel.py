from ml.ScenarioFormatter import ScenarioFormatter
from ml.InterestingWordListGenerator import interesting_word_list_generator
from ml.XGBoostClassifier import XGBoostClassifier
from model.TrainingScenario import TrainingScenario
from ml.TensorflowClassifier import TensorflowClassifier
from collections import Counter
import string


def train_xgb_model(dataset: [TrainingScenario]) -> XGBoostClassifier:
    interesting_words = interesting_word_list_generator([(scenario.training_label, scenario.trace) for scenario in dataset])
    labels = list({scenario.training_label for scenario in dataset})
    scenario_formatter = ScenarioFormatter(interesting_words, labels)

    classifier = XGBoostClassifier(scenario_formatter)
    return classifier


def train_neural_net_model(dataset: [TrainingScenario]) -> TensorflowClassifier:
    def clean_trace(trace):
        punctuation_and_whitespaces = string.punctuation + string.whitespace
        translator = str.maketrans(punctuation_and_whitespaces, ' ' * len(punctuation_and_whitespaces))
        trace = trace.translate(translator)
        return [word.lower() for word in trace.split()]

    trace = [sc.trace for sc in dataset]
    trace = [clean_trace(tr) for tr in trace]
    words = []

    for tr in trace:
        for word in tr:
            words.append(word)

    selected_words = [(word, frequency) for word, frequency in Counter(words).items()]

    features = [word[0] for word in selected_words]
    features = [f for f in features if f.isalpha()]
    features = [f for f in features if len(f) > 1]

    labels = list({scenario.training_label for scenario in dataset})

    scenario_formatter = ScenarioFormatter(features, labels)
    classifier = TensorflowClassifier(scenario_formatter)
    classifier.train(dataset)
    return classifier
