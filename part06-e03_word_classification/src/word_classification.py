#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer

alphabet = "abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)


# Returns a list of Finnish words
def load_finnish():
    finnish_url = "https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename = "src/kotus-sanalista_v1.xml"
    load_from_net = False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines = []
            for line in data:
                lines.append(line.decode('utf-8'))
        doc = "".join(lines)
    else:
        with open(filename, "rb") as data:
            doc = data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))


def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines = map(lambda s: s.rstrip(), data.readlines())
    return lines


def get_features(wordlist):
    vectorizer = CountVectorizer(token_pattern=r"(?u)\w|-", analyzer='char', vocabulary=alphabet_set)
    temp = vectorizer.transform(wordlist).toarray()
    final_array = np.hstack((temp[:, 1:], temp[:, 0].reshape(-1, 1)))
    return final_array


def contains_valid_chars(s):
    for i in s:
        if i not in alphabet:
            return False
    return True


def get_features_and_labels():
    finnish = load_finnish()
    finnish_lower = [word.lower() for word in finnish]
    finnish_ok = [word for word in finnish_lower if contains_valid_chars(word)]

    english = list(load_english())
    english_lower = [i.lower() for i in english if i[0].islower()]
    english_ok = [i for i in english_lower if contains_valid_chars(i)]

    finnish_feat = get_features(finnish_ok)
    finnish_targ = np.zeros((len(finnish_ok), 1))
    english_feat = get_features(english_ok)
    english_targ = np.ones((len(english_ok), 1))

    targ = np.concatenate((finnish_targ, english_targ))
    feat = np.concatenate((finnish_feat, english_feat))

    return feat, targ


def word_classification():
    feature_matrix, labels = get_features_and_labels()
    model = MultinomialNB()
    valgen = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    score = cross_val_score(model, feature_matrix, np.ravel(labels), cv=valgen)
    return score


def main():
    print("Accuracy scores are:", word_classification())


if __name__ == "__main__":
    main()
