class PredictionScenario:
    def __init__(
                self,
                id: str,
                zucchini_id: str,
                trace: str,
                fail_step_key_word: str,
                ):
        self.id = id
        self.zucchini_id = zucchini_id
        self.trace = trace
        self.fail_step_key_word = fail_step_key_word

    @staticmethod
    def from_json(json: dict):
        return PredictionScenario(
            json["id"],
            json["zucchiniId"],
            json["trace"],
            json["failStepKeyWord"],
        )
