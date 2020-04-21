from service.TrainingService import TrainingService
from rabbitMQ.TrainingConsumer import TrainingConsumer


def StartTraining():
    training_service = TrainingService()
    training_consumer = TrainingConsumer(training_service.generate_new_model)
    training_consumer.start()
    training_consumer.close()


if __name__ == '__main__':
    StartTraining()
