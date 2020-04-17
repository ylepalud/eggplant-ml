from dotenv import load_dotenv
import os
load_dotenv()

RABBIT_MQ_HOST = os.getenv("RABBIT_MQ_HOST")
RABBIT_MQ_PORT = int(os.getenv("RABBIT_MQ_PORT"))
RABBIT_MQ_SERVER = os.getenv("RABBIT_MQ_SERVER")
SCENARIO_QUEUE = os.getenv("SCENARIO_QUEUE")
PREDICTION_QUEUE = os.getenv("PREDICTION_QUEUE")
TRAINING_QUEUE = os.getenv("TRAINING_QUEUE")
