from ml.XGBoostClassifier import XGBoostClassifier
import pickle
import datetime


class CreateClassifierParam:
    def __init__(self,
                 version,
                 training_accuracy,
                 created_at,
                 interesting_words,
                 good_prediction,
                 total_labeled_prediction,
                 total_prediction,
                 active_classifier,
                 model,
                 ):
        self.version = version
        self.trainingAccuracy = training_accuracy
        self.createdAd = created_at
        self.interestingWords = interesting_words
        self.goodPrediction = good_prediction
        self.totalLabeledPrediction = total_labeled_prediction
        self.totalPrediction = total_prediction
        self.activeClassifier = active_classifier
        self.model = model


def create_default_classifier_param(model: XGBoostClassifier):
    return CreateClassifierParam(
                 "version",
                 model.accuracy,
                 datetime.datetime.utcnow(),
                 model._scenario_formatter._interesting_words,
                 0,
                 0,
                 0,
                 False,
                 pickle.dumps(model)
    )
