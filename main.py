from dotenv import load_dotenv
from rabbitMQ.StartPrediction import StartPrediction
from rabbitMQ.StartTraining import StartTraining
from threading import Thread
load_dotenv()


def start_application():
    queues = [StartPrediction, StartTraining]

    for queue in queues:
        Thread(target=queue).start()


if __name__ == '__main__':
    start_application()
