from dotenv import load_dotenv
from pymongo import MongoClient
import os
load_dotenv()

DB_URL = os.getenv("DB_URL")
DB_PORT = int(os.getenv("DB_PORT"))
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_NAME = "eggplant"
CLASSIFIER_COLLECTION = "classifier"
DATASET_COLLECTION = "dataset"
TEST_COLLECTION = "test_collection"


def _create_collection_instance(db_url: str, db_port: int, db_name: str, collection_name: str):
    if DB_USERNAME is None or DB_PASSWORD is None:
        client = MongoClient(db_url, db_port)
    else:
        client = MongoClient(db_url, db_port, username=DB_USERNAME, password=DB_PASSWORD)
    db = client[db_name]
    return db[collection_name]
