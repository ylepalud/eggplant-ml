from dotenv import load_dotenv
import os
load_dotenv()

RABBIT_MQ_HOST = os.getenv("RABBIT_MQ_HOST")
RABBIT_MQ_PORT = int(os.getenv("RABBIT_MQ_PORT"))
RABBIT_MQ_SERVER = os.getenv("RABBIT_MQ_SERVER")

EGGPLANT_SUBMIT_TRAINING_QUEUE = "eggplant-submit-training"
EGGPLANT_SUBMIT_TRAINING_EXCHANGE = "eggplant-submit-training"
EGGPLANT_SUBMIT_PREDICTION_QUEUE = "eggplant-submit-prediction"
EGGPLANT_SUBMIT_PREDICTION_EXCHANGE = "eggplant-submit-prediction"
PREDICTION_QUEUE = "eggplant-prediction"
PREDICTION_EXCHANGE = "eggplant-prediction"
TRAINING_QUEUE = "eggplant-training"
TRAINING_EXCHANGE = "eggplant-training"

PREDICTION_ROUTING_KEY = "prediction"
TRAIN_ROUTING_KEY = "train"
