from db import DB_URL, DB_PORT, DATABASE_NAME, DATASET_COLLECTION, _create_collection_instance
from model.TrainingScenario import TrainingScenario

# Todo Provide a function that fetch dataset on the database


def get_dataset() -> [TrainingScenario]:
    # scenario_collection = _create_collection_instance(DB_URL, DB_PORT, DATABASE_NAME, DATASET_COLLECTION)
    collection = _create_collection_instance(DB_URL, DB_PORT, "eggplant", DATASET_COLLECTION)
    data = collection.find({"usedInDataset": True})

    return [TrainingScenario.from_json(i) for i in data]


if __name__ == '__main__':
    a = get_dataset()
