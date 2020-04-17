import db.DatasetStore as datasetCollection
from model.TrainingScenario import TrainingScenario


class DatasetService:

    def get_dataset(self) -> [TrainingScenario]:
        return datasetCollection.get_dataset()
