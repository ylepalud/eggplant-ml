from service.DatasetService import DatasetService
from service.ClassifierService import ClassifierService
from ml.TrainModel import train_xgb_model, train_neural_net_model

from model.Classifier import Classifier


class TrainingService:

    def __init__(self):
        self._datasetService = DatasetService()
        self._classifierService = ClassifierService()

    def generate_new_model(self) -> Classifier:
        dataset = self._datasetService.get_dataset()
        model = train_neural_net_model(dataset)
        return self._classifierService.post_new_model(model)


if __name__ == '__main__':
    trainingService = TrainingService()
    value = trainingService.generate_new_model()
