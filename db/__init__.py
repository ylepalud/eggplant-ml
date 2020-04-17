from dotenv import load_dotenv
from pymongo import MongoClient
import os
load_dotenv()

DB_URL = os.getenv("DB_URL")
DB_PORT = int(os.getenv("DB_PORT"))
DATABASE_NAME = os.getenv("DATABASE_NAME")
CLASSIFIER_COLLECTION = os.getenv("CLASSIFIER_COLLECTION")
DATASET_COLLECTION = os.getenv("DATASET_COLLECTION")
TEST_COLLECTION = os.getenv("TEST_COLLECTION")


def _create_collection_instance(db_url: str, db_port: int, db_name: str, collection_name: str):
    client = MongoClient(db_url, db_port)
    db = client[db_name]
    return db[collection_name]
