from rabbitMQ import RABBIT_MQ_HOST, RABBIT_MQ_PORT, RABBIT_MQ_SERVER, EGGPLANT_SUBMIT_TRAINING_QUEUE, EGGPLANT_SUBMIT_TRAINING_EXCHANGE, TRAIN_ROUTING_KEY
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
            queue=EGGPLANT_SUBMIT_TRAINING_QUEUE,
            durable=True
        )

        self._channel.exchange_declare(
            exchange=EGGPLANT_SUBMIT_TRAINING_EXCHANGE,
            exchange_type="topic",
            durable=True
        )

        self._channel.queue_bind(
            exchange=EGGPLANT_SUBMIT_TRAINING_EXCHANGE,
            queue=EGGPLANT_SUBMIT_TRAINING_QUEUE,
            routing_key=TRAIN_ROUTING_KEY
        )

        self._channel.basic_consume(
            queue=EGGPLANT_SUBMIT_TRAINING_QUEUE,
            on_message_callback=self.consume_callback,
            auto_ack=True
        )

    def consume_callback(self, ch, method, properties, body):
        print("Start training new classifier")
        try:
            json_data = json.loads(body.decode("utf-8"))
        except json.decoder.JSONDecodeError as e:
            print("Invalid Json input")
            return
        # self._trigger_function(json_data)
        self._trigger_function()
        print("End training new classifier")

    def start(self):
        self._channel.start_consuming()

    def close(self):
        self._connection.close()
