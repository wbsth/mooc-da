#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics

def plant_classification():
    iris = load_iris()
    xtrain, xtest, ytrain, ytest = train_test_split(iris.data, iris.target, train_size=0.8, random_state=0)
    model = naive_bayes.GaussianNB()
    model.fit(xtrain, ytrain)
    y_predict = model.predict(xtest)
    score = metrics.accuracy_score(ytest, y_predict)
    return score

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
