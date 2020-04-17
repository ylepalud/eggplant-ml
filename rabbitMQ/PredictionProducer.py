from rabbitMQ import RABBIT_MQ_HOST, RABBIT_MQ_PORT, RABBIT_MQ_SERVER, PREDICTION_QUEUE
import pika
import json


class PredictionProducer:

    def __init__(self):
        self._connection = pika.BlockingConnection(
            pika.connection.ConnectionParameters(
                host=RABBIT_MQ_HOST,
                port=RABBIT_MQ_PORT,
                locale=RABBIT_MQ_SERVER,
            )
        )
        self._channel = self._connection.channel()
        self._channel.queue_declare(
            queue=PREDICTION_QUEUE,
            durable=True
        )

    def send_prediction(self, prediction):
        self._channel.basic_publish(
            exchange='',
            routing_key=PREDICTION_QUEUE,
            body=json.dumps(prediction)
        )

    def close(self):
        self._connection.close()
