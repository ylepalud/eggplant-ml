class PredictionScenario:
    def __init__(
                self,
                id: str,
                zucchini_id: str,
                trace: str,
                fail_step_key_word: str,
                scenario_key: str,
                test_run_id: str,
                ):
        self.id = id
        self.zucchini_id = zucchini_id
        self.trace = trace
        self.fail_step_key_word = fail_step_key_word
        self.scenario_key = scenario_key
        self.test_run_id = test_run_id

    @staticmethod
    def from_json(json: dict):
        return PredictionScenario(
            json["id"],
            json["zucchiniId"],
            json["trace"],
            json["failStepKeyWord"],
            json["scenarioKey"],
            json["testRunId"],
        )
