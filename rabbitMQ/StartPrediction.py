from service.PredictionService import PredictionService
from rabbitMQ.ScenarioConsumer import ScenarioConsumer
from pika.exceptions import AMQPError


def StartPrediction():
    try:
        prediction_service = PredictionService()
        scenario_consumer = ScenarioConsumer(prediction_service.make_a_prediction)
        scenario_consumer.start()
    except AMQPError:
        print("Prediction queue Error, restarting queue")
        scenario_consumer.close()
        StartPrediction()


if __name__ == '__main__':
    StartPrediction()

