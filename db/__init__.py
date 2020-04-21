from dotenv import load_dotenv
from pymongo import MongoClient
import os
load_dotenv()

DB_URL = os.getenv("DB_URL")
DB_PORT = int(os.getenv("DB_PORT"))

DATABASE_NAME = "test"
CLASSIFIER_COLLECTION = "classifier"
DATASET_COLLECTION = "dataset"
TEST_COLLECTION = "test_collection"


def _create_collection_instance(db_url: str, db_port: int, db_name: str, collection_name: str):
    client = MongoClient(db_url, db_port)
    db = client[db_name]
    return db[collection_name]
