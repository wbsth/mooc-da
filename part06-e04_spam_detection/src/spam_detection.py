#!/usr/bin/env python3

from gzip import open
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

def prepare_array(filename, fraction):
    with open(filename) as myfile:
        file = myfile.readlines()
        length = int(len(file) * fraction)
        normal = file[:length]
        normal = np.asarray(normal)
        return normal

def spam_detection(random_state=0, fraction=1.0):
    ham = prepare_array('src/ham.txt.gz', fraction)
    ham_label = np.zeros((len(ham), 1))
    spam = prepare_array('src/spam.txt.gz', fraction)
    spam_label = np.ones((len(spam), 1))

    label = np.concatenate((ham_label, spam_label))
    joined_list = np.concatenate((ham, spam))

    vectorizer = CountVectorizer()
    feature_matrix = vectorizer.fit_transform(joined_list)

    matrix_train, matrix_test, label_train, label_test = train_test_split(feature_matrix, label, train_size=0.75, random_state=random_state)

    label_train = np.ravel(label_train)

    model = MultinomialNB()
    model.fit(matrix_train, label_train)
    prediction = model.predict(matrix_test)

    correct = accuracy_score(label_test, prediction, normalize=False)
    test_sample_size = len(label_test)
    misclassified = test_sample_size - correct
    score = correct / test_sample_size

    return score, test_sample_size, misclassified

def main():
    spam_detection()
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
