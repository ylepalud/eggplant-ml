from pymongo import MongoClient
import db.AiModelStore as db
from dotenv import load_dotenv
load_dotenv()


class TestClass:
    def __init__(self, number, greeting):
        self._a_number = number
        self._greeting = greeting

    def add(self, number):
        return self._a_number + number

    def greeting(self, name):
        return self._greeting + name


def reset():
    client = MongoClient("localhost", 27017)
    db = client["test"]
    collection = db.test_collection
    collection.drop()


if __name__ == "__main__":
    reset()
    obj = TestClass(2, "Hello")
    obj2 = TestClass(5, "salut")

    inserted_id = db.store_object_in_mongo(obj)
    inserted_id2 = db.store_object_in_mongo(obj2)
    loaded_obj = db.load_object_from_mongo(inserted_id.id)
    loaded_obj2 = db.load_object_from_mongo(inserted_id2.id)

    try:
        loaded_obj3 = db.load_object_from_mongo("willfail")
    except db.NoDocument as e:
        print(e)
