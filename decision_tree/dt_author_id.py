#!/usr/bin/python

"""
    this is the code to accompany the Lesson 3 (decision tree) mini-project

    use an DT to identify emails from the Enron corpus by their authors

    Sara has label 0
    Chris has label 1

"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

from sklearn.tree import DecisionTreeClassifier
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()



exercise = 1

if exercise == 1:
    clf = DecisionTreeClassifier(min_samples_split=40)
    clf.fit(features_train, labels_train)
    acc = clf.score(features_test, labels_test)

    print('Accuracy with min_samples_split=40 = {0}'.format(acc))

if exercise == 2:

    print('Length of features = {0}'.format(len(features_train[0])))
