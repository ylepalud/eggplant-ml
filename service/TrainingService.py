from service.DatasetService import DatasetService
from service.ClassifierService import ClassifierService
from ml.TrainModel import train_new_model
from model.Classifier import Classifier


class TrainingService:

    def __init__(self):
        self._datasetService = DatasetService()
        self._classifierService = ClassifierService()

    def generate_new_model(self) -> Classifier:
        dataset = self._datasetService.get_dataset()
        model = train_new_model(dataset)
        return self._classifierService.post_new_model(model)


if __name__ == '__main__':
    trainingService = TrainingService()
    value = trainingService.generate_new_model()

    """
    from db.NoDocument import NoDocument
    try:
        value = trainingService._classifierService.get_model("5e99bb94e8e458b76926df19")
    except NoDocument as e:
        print(e)
    """
