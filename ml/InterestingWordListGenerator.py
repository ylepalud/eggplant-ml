from collections import Counter
from ml.cleanTrace import clean_trace


def interesting_word_list_generator(rows: [(str, str)]) -> [str]:
    """
    Génération d'une liste de mots présent dans type d'erreur autre que UNKNOWN
    :param rows: (label, trace) Traces d'erreurs de scenarios en échecs avec le type d'erreur
    :return: liste de mots important
    """
    # Aggrégation des traces au type d'erreur
    label_trace = dict()
    for row in rows:
        label, trace = row[0], row[1]
        if label not in label_trace.keys():
            label_trace[label] = []
        label_trace[label] += clean_trace(trace)
        label_trace[label] = [w for w in label_trace[label] if w.isalpha()]
        label_trace[label] = [w for w in label_trace[label] if len(w) > 1]

    # Répartition des mots en fonction des types d'erreurs
    label_counter = dict()
    for label, words_in_trace in label_trace.items():
        label_counter[label] = Counter(words_in_trace)

    label_most_common_word = dict()
    for label, counter in label_counter.items():
        label_most_common_word[label] = [i[0] for i in counter.most_common(1000)]

    # filter dans le top most_counter_number les mots qui ne sont que dans cette trace
    label_intersting_words = dict()
    for label_most_commun, counter in label_counter.items():
        label_intersting_words[label_most_commun] = []

        # On récupére tous les mots qui ne sont pas du label courant
        all_words_except_current_label = []
        for label_filter, words in label_trace.items():
            if label_filter != label_most_commun:
                all_words_except_current_label += words

        # On filtre
        top_x_words = label_most_common_word[label_most_commun]
        label_intersting_words[label_most_commun] = [interesting_word for interesting_word in top_x_words if
                                                     interesting_word not in all_words_except_current_label]

    result = []
    for label, word in label_intersting_words.items():
        result = [*result, *[w for w in word]]
        # result = [*result, *[w for w in word if label != 'UNKNOWN']]
    return result


if __name__ == '__main__':
    a = [("UNKNOW", "java.lang.exception"), ("PARTNER", "java.lang.exception Partner ko"), ("PARTNER", "java.lang.exception Partner ko"), ("TOTO", "titi a mangé tata")]

    print(interesting_word_list_generator(a))
