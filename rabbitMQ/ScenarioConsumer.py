from rabbitMQ import RABBIT_MQ_HOST, RABBIT_MQ_PORT, RABBIT_MQ_SERVER, EGGPLANT_SUBMIT_PREDICTION_QUEUE, EGGPLANT_SUBMIT_PREDICTION_EXCHANGE, PREDICTION_ROUTING_KEY
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
            queue=EGGPLANT_SUBMIT_PREDICTION_QUEUE,
            durable=True
        )

        self._channel.exchange_declare(
            exchange=EGGPLANT_SUBMIT_PREDICTION_EXCHANGE,
            exchange_type="topic",
            durable=True
        )

        self._channel.queue_bind(
            exchange=EGGPLANT_SUBMIT_PREDICTION_EXCHANGE,
            queue=EGGPLANT_SUBMIT_PREDICTION_QUEUE,
            routing_key=PREDICTION_ROUTING_KEY
        )

        self._channel.basic_consume(
            queue=EGGPLANT_SUBMIT_PREDICTION_QUEUE,
            on_message_callback=self.consume_callback,
            auto_ack=True
        )

    def consume_callback(self, ch, method, properties, body):
        try:
            json_data = json.loads(body.decode("utf-8"))
        except json.decoder.JSONDecodeError as e:
            print("Invalid Json input")
            return
        self._trigger_function(
            PredictionScenario.from_json(json_data)
        )

    def start(self):
        self._channel.start_consuming()

    def close(self):
        self._connection.close()


if __name__ == '__main__':
    scenarioConsumer = ScenarioConsumer()
    scenarioConsumer.start()
    scenarioConsumer.close()
