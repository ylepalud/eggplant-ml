from service.PredictionService import PredictionService
from rabbitMQ.ScenarioConsumer import ScenarioConsumer


def main():
    prediction_service = PredictionService()
    scenario_consumer = ScenarioConsumer(prediction_service)
    scenario_consumer.start()
    scenario_consumer.close()


if __name__ == '__main__':
    main()

