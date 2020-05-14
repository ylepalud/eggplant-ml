from service.TrainingService import TrainingService
from rabbitMQ.TrainingConsumer import TrainingConsumer
from pika.exceptions import AMQPError


def StartTraining():
    try:
        training_service = TrainingService()
        training_consumer = TrainingConsumer(training_service.generate_new_model)
        training_consumer.start()
    except AMQPError:
        print("Training queue Error, restarting queue")
        training_consumer.close()
        StartTraining()


if __name__ == '__main__':
    StartTraining()
