from service.ClassifierService import ClassifierService
from model.PredictionScenario import PredictionScenario
from rabbitMQ.PredictionProducer import PredictionProducer
from db.NoDocument import NoDocument


class PredictionService:

    def __init__(self):
        self._classifierService = ClassifierService()
        self._predictionProducer = PredictionProducer()

    def make_a_prediction(self, classifier_id: str, scenario: PredictionScenario):
        try:
            classifier = self._classifierService.get_model(classifier_id)
        except NoDocument as e:
            print(e)
            return

        prediction = classifier.model.predict(scenario)
        self._predictionProducer.send_prediction(prediction)
