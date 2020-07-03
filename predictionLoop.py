from rabbitMQ.StartPrediction import StartPrediction
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    with open("banner.txt", "r") as banner:
        print(banner.read())
    StartPrediction()
    print("Application started, waiting for scenarii")
