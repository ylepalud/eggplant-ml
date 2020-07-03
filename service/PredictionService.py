from service.ClassifierService import ClassifierService
from model.PredictionScenario import PredictionScenario
from rabbitMQ.PredictionProducer import PredictionProducer
from db.NoDocument import NoDocument


class PredictionService:

    def __init__(self):
        self._classifierService = ClassifierService()
        self._predictionProducer = PredictionProducer()

    def make_a_prediction(self, classifier_id: str, scenario: PredictionScenario):
        print("Start prediction")
        try:
            classifier = self._classifierService.get_model()
        except NoDocument as e:
            print(e)
            return

        prediction = classifier.predict(scenario)
        prediction = [{"label": str(label[0]), "accuracy": str(label[1])} for label in prediction]
        prediction = {
            "prediction": prediction,
            "classifierId": classifier_id,
            "zucchiniId": scenario.zucchini_id,
            "scenarioId": scenario.id,
            "scenarioKey": scenario.scenario_key,
            "testRunId": scenario.test_run_id
        }
        self._predictionProducer.send_prediction(prediction)
        print("End prediction")
        return prediction


if __name__ == '__main__':
    prediction_service = PredictionService()
    from service.DatasetService import DatasetService
    dataset_service = DatasetService()
    dataset = dataset_service.get_dataset()

    print(prediction_service.make_a_prediction("5e99bb94e8e458b76926df19", dataset[0]))
