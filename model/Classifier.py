from dto.CreateClassifierParam import CreateClassifierParam
import pickle


class Classifier:
    def __init__(self,
                 id,
                 version,
                 training_accuracy,
                 created_at,
                 interesting_words,
                 good_prediction,
                 total_labeled_prediction,
                 total_prediction,
                 active_classifier,
                 model
                 ):
        self.id = id
        self.version = version
        self.training_accuracy = training_accuracy
        self.created_at = created_at
        self.interesting_words = interesting_words
        self.good_prediction = good_prediction
        self.total_labeled_prediction = total_labeled_prediction
        self.total_prediction = total_prediction
        self.active_classifier = active_classifier
        self.model = pickle.loads(model)

    @staticmethod
    def from_json(json: dict):
        return Classifier(
            json["_id"],
            json["version"],
            json["trainingAccuracy"],
            json["createdAd"],
            json["interestingWords"],
            json["goodPrediction"],
            json["totalLabeledPrediction"],
            json["totalPrediction"],
            json["activeClassifier"],
            json["model"]
        )

    @staticmethod
    def from_create_param(id: str, params: CreateClassifierParam):
        return Classifier(
            id,
            params.version,
            params.trainingAccuracy,
            params.createdAd,
            params.interestingWords,
            params.goodPrediction,
            params.totalLabeledPrediction,
            params.totalPrediction,
            params.activeClassifier,
            params.model
        )
