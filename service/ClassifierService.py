import db.AiModelStore as classifierCollection
from model.Classifier import Classifier


class ClassifierService:
    def __init__(self):
        self._cache = dict()

    def get_model(self, model_id) -> Classifier:
        if model_id in self._cache.keys():
            return self._cache[model_id]
        classifier = classifierCollection.load_object_from_mongo(model_id)
        self._cache[model_id] = classifier
        return classifier

    def post_new_model(self, model: Classifier):
        classifier = classifierCollection.store_object_in_mongo(model)
        self._cache[classifier.id] = classifier
        return classifier


if __name__ == '__main__':
    class CustomClass:
        def __init__(self, a):
            self.a = a

    classifier_service = ClassifierService()
    classifier_obj = classifier_service.post_new_model(CustomClass(2))
    obj = classifier_service.get_model(classifier_obj.id)
