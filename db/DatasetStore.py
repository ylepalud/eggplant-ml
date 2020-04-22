from db import DB_URL, DB_PORT, DATABASE_NAME, DATASET_COLLECTION, _create_collection_instance
from model.TrainingScenario import TrainingScenario


def get_dataset() -> [TrainingScenario]:
    collection = _create_collection_instance(DB_URL, DB_PORT, DATABASE_NAME, DATASET_COLLECTION)
    data = collection.find({"usedInDataset": True})

    return [TrainingScenario.from_json(i) for i in data]


if __name__ == '__main__':
    a = get_dataset()
