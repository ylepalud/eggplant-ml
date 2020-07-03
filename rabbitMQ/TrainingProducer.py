from rabbitMQ import RABBIT_MQ_HOST, RABBIT_MQ_PORT, RABBIT_MQ_SERVER, TRAINING_QUEUE, TRAINING_EXCHANGE
from model.Classifier import Classifier
import pika


class TrainingProducer:

    def __init__(self):
        self._connection = pika.BlockingConnection(
            pika.connection.ConnectionParameters(
                host=RABBIT_MQ_HOST,
                port=RABBIT_MQ_PORT,
                locale=RABBIT_MQ_SERVER
            )
        )
        self._channel = self._connection.channel()

        self._channel.exchange_declare(
            exchange=TRAINING_EXCHANGE,
            exchange_type="topic",
            durable=True
        )

        self._channel.queue_declare(
            queue=TRAINING_QUEUE,
            durable=True
        )

    def send_trained_model(self, model: Classifier):
        # TODO find a way to publish files
        self._channel.basic_publish(
            exchange=TRAINING_EXCHANGE,
            routing_key=TRAINING_QUEUE,
            body=""
        )

    def close(self):
        self._connection.close()
