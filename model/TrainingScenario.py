class TrainingScenario:
    def __init__(self,
                 id: str,
                 zucchini_id: str,
                 trace: str,
                 training_label: str,
                 correction_action: str,
                 scenario_key: str,
                 fail_step_key_word: str,
                 used_in_dataset: bool
                 ):
        self.id = id
        self.zucchini_id = zucchini_id
        self.trace = trace
        self.training_label = training_label
        self.correction_action = correction_action
        self.scenario_key = scenario_key
        self.fail_step_key_word = fail_step_key_word
        self.used_in_dataset = used_in_dataset

    @staticmethod
    def from_json(json: dict):
        return TrainingScenario(
            json["_id"],
            json["zucchiniId"],
            json["trace"],
            json["trainingLabel"],
            json["correctionAction"],
            json["scenarioKey"],
            json["failStepKeyWord"],
            json["usedInDataset"],
        )
