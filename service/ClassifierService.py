from ml.TensorflowClassifier import TensorflowClassifier
import tensorflow as tf
import pickle
import os


class ClassifierService:

    def __init__(self):
        self._base_path = "./storage/"
        self._model_path = "model"
        self._formatter_path = "formatter.pickle"
        self._model = None

    def get_model(self) -> TensorflowClassifier:
        if self._model is None:
            self._model = self.load_model()
        return self._model

    def post_new_model(self, model: TensorflowClassifier):
        if not os.path.exists(self._base_path):
            os.makedirs(self._base_path)
        with open(self._base_path + self._formatter_path, "wb+") as file:
            pickle.dump(model._scenario_formatter, file)
        model._trained_model.save(self._base_path + self._model_path)
        return model

    def load_model(self):
        print(os.getcwd())
        with open(self._base_path + self._formatter_path, 'rb') as file:
            loaded_formatter = pickle.load(file)
        tensorflow_classifier = TensorflowClassifier(loaded_formatter)
        tensorflow_classifier._trained_model = tf.keras.models.load_model(self._base_path + self._model_path)
        return tensorflow_classifier


if __name__ == '__main__':
    class CustomClass:
        def __init__(self, a):
            self.a = a

    classifier_service = ClassifierService()
    classifier_obj = classifier_service.post_new_model(CustomClass(2))
    obj = classifier_service.get_model(classifier_obj.id)
