from rabbitMQ import RABBIT_MQ_HOST, RABBIT_MQ_PORT, RABBIT_MQ_SERVER, TRAINING_QUEUE, TRAINING_EXCHANGE, TRAIN_ROUTING_KEY
from ml.Classifier import Classifier
import pika
import json


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
        classifier_creation_params = dict()
        classifier_creation_params["version"] = model.id
        classifier_creation_params["trainingAccuracy"] = model.accuracy
        classifier_creation_params["interestingWords"] = list()
        self._channel.basic_publish(
            exchange=TRAINING_EXCHANGE,
            routing_key=TRAIN_ROUTING_KEY,
            body=json.dumps(classifier_creation_params)
        )

    def close(self):
        self._connection.close()
