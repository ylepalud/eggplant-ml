from rabbitMQ import RABBIT_MQ_HOST, RABBIT_MQ_PORT, RABBIT_MQ_SERVER, TRAINING_QUEUE
import json
import pika


class TrainingConsumer:

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
            queue=TRAINING_QUEUE,
            durable=True
        )

        self._channel.basic_consume(
            queue=TRAINING_QUEUE,
            on_message_callback=self.consume_callback,
            auto_ack=True
        )

    def consume_callback(self, ch, method, properties, body):
        json_data = json.loads(body.decode("utf-8"))
        self._trigger_function(json_data)

    def start(self):
        self._channel.start_consuming()

    def close(self):
        self._connection.close()
