from dotenv import load_dotenv
from rabbitMQ.StartPrediction import StartPrediction
from rabbitMQ.StartTraining import StartTraining
from threading import Thread


def start_application():
    load_dotenv()
    queues = [StartPrediction, StartTraining]

    for queue in queues:
        Thread(target=queue).start()


if __name__ == '__main__':
    with open("banner.txt", "r") as banner:
        print(banner.read())
    start_application()
    print("Application started, waiting for scenarii")
