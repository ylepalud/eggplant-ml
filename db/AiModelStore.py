from db.NoDocument import NoDocument
from dto.CreateClassifierParam import create_default_classifier_param
from model.Classifier import Classifier
from db import DB_URL, DB_PORT, DATABASE_NAME, TEST_COLLECTION, _create_collection_instance
from bson.objectid import ObjectId

# Todo Store model object with the correct shape
# TODO https://medium.com/up-engineering/saving-ml-and-dl-models-in-mongodb-using-python-f0bbbae256f0


def store_object_in_mongo(model) -> Classifier:
    collection = _create_collection_instance(DB_URL, DB_PORT, DATABASE_NAME, TEST_COLLECTION)
    params = create_default_classifier_param(model)
    info = collection.insert_one(vars(params))
    return Classifier.from_create_param(info.inserted_id, params)


def load_object_from_mongo(_id) -> Classifier:
    collection = _create_collection_instance(DB_URL, DB_PORT, DATABASE_NAME, TEST_COLLECTION)
    data = collection.find_one({"_id": ObjectId(_id)})

    try:
        classifier = Classifier.from_json(data)
    except UnboundLocalError as e:
        raise NoDocument("No model with this id")
    return classifier
