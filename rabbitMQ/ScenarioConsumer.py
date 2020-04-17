from rabbitMQ import RABBIT_MQ_HOST, RABBIT_MQ_PORT, RABBIT_MQ_SERVER, SCENARIO_QUEUE
import json
from model.PredictionScenario import PredictionScenario
import pika


class ScenarioConsumer:

    def __init__(self, trigger_function):
        self._trigger_function = trigger_function
        self._connection = pika.BlockingConnection(
            pika.connection.ConnectionParameters(
                host=RABBIT_MQ_HOST,
                port=RABBIT_MQ_PORT,
                locale=RABBIT_MQ_SERVER
            )
        )

        self._channel = self._connection.channel()
        self._channel.queue_declare(
            queue=SCENARIO_QUEUE,
            durable=True
        )

        self._channel.basic_consume(
            queue=SCENARIO_QUEUE,
            on_message_callback=self.consume_callback,
            auto_ack=True
        )

    def consume_callback(self, ch, method, properties, body):
        json_data = json.loads(body.decode("utf-8"))
        prediction_scenario = PredictionScenario.from_json(json_data)
        print("New prediction to submit")
        print(prediction_scenario)
        print()
        self._trigger_function(prediction_scenario)

    def start(self):
        self._channel.start_consuming()

    def close(self):
        self._connection.close()


if __name__ == '__main__':
    scenarioConsumer = ScenarioConsumer()
    scenarioConsumer.start()
    scenarioConsumer.close()
