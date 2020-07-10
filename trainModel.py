from service.TrainingService import TrainingService
from dotenv import load_dotenv
from rabbitMQ.TrainingProducer import TrainingProducer


if __name__ == '__main__':
    load_dotenv()
    with open("banner.txt", "r") as banner:
        print(banner.read())
        print("Training new model")

    training_service = TrainingService()
    new_classifier = training_service.generate_new_model()

    training_producer = TrainingProducer()
    training_producer.send_trained_model(new_classifier)
    training_producer.close()

