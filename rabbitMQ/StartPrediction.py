from service.PredictionService import PredictionService
from rabbitMQ.ScenarioConsumer import ScenarioConsumer


def StartPrediction():
    prediction_service = PredictionService()
    scenario_consumer = ScenarioConsumer(prediction_service.make_a_prediction)
    scenario_consumer.start()
    scenario_consumer.close()


if __name__ == '__main__':
    StartPrediction()

