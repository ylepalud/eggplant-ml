from ml.cleanTrace import clean_trace
import numpy as np


class ScenarioFormatter:
    fail_step_key_word = [
        "Soit",
        "Et",
        "Quand",
        "Alors"
    ]

    track_http_status = ["200", "301", "302", "304", "400", "401", "403", "404", "500", "503", "504"]
    
    def __init__(self, interesting_words: [str], labels: [str]):
        self._labels = labels
        self._interesting_words = interesting_words

        self._sequence_one_hot_encoded = [
            *self.fail_step_key_word,
            *self.track_http_status,
            *self._interesting_words
        ]

        self._index_to_label_mapper = dict()
        for index, value in enumerate(self._sequence_one_hot_encoded):
            self._index_to_label_mapper[index] = value

    def _track_http_status_to_number(self, trace: [str]) -> [int]:
        http_status = {http_status: 0 for http_status in self.track_http_status}
        for word in trace:
            for tracked_status in self.track_http_status:
                if word == tracked_status:
                    http_status[word] = 1
        return http_status.values()

    def _fail_step_key_word_to_number(self, keyword: str) -> [int]:
        keyword_format = []
        for bdd_keyword in self.fail_step_key_word:
            if bdd_keyword == keyword:
                keyword_format.append(1)
            else:
                keyword_format.append(0)
        return keyword_format

    def _interesting_words_to_number(self, trace: [str]) -> [int]:
        interesting_words = {word: 0 for word in self._interesting_words}
        for word in trace:
            if word in interesting_words.keys():
                interesting_words[word] = 1
        return interesting_words.values()

    def format_entry(self, trace: str, fail_step_keyword: str) -> [int]:
        trace = clean_trace(trace)
        one_hot_encoded = [
            *self._track_http_status_to_number(trace),
            *self._fail_step_key_word_to_number(fail_step_keyword),
            *self._interesting_words_to_number(trace),
        ]
        data_frame = np.array(one_hot_encoded)
        return data_frame

    def get_label(self):
        return self._labels


if __name__ == '__main__':
    data = {'correction_action': 'UNKNOWN',
     'fail_step_key_word': 'Alors',
     'id': '8223cbcc-7a3d-11ea-9fa4-9b5985c0b7c7',
     'scenario_key': 'd3b6357b8907b890dd300f8227e5dca39e665798',
     'trace': 'java.lang.AssertionError: Différence entre le code retour attendu '
              '[200] et le code retour obtenu [400].. Expression: (resp.status == '
              '200)\n'
              '\tat '
              'step_definitions.searchFromItineraries.then.SearchSolutionsFromItinerariesAssertions$_run_closure1.doCall(SearchSolutionsFromItinerariesAssertions.groovy:38)\n'
              "\tat ✽.Alors des solutions sont remontées classées dans l'ordre des "
              'itinéraires passés en entrée du '
              'service(features/search_solutions_from_itineraries/search-solutions-from-itineraries.feature:86)\n',
     'training_label': 'NOT_APPLICABLE',
     'used_in_dataset': True,
     'zucchini_id': '890a7a08-b76a-4b3f-a13d-44958bb34c48'}
    scenario_formatter = ScenarioFormatter(['Alors', 'des', 'solutions'], ['NOT_APPLICABLE', 'UNKNOWN'])
    print(scenario_formatter.format_entry(data['trace'], data['fail_step_key_word']))
