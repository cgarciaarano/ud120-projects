#!/usr/bin/python

"""
    this is the code to accompany the Lesson 1 (Naive Bayes) mini-project

    use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1

"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

print 'Training data length:{0}'.format(len(features_train))
print 'Test data length:{0}'.format(len(features_test))

print 'Test data:{0}'.format(features_test[0:3])


clf = GaussianNB()

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
prediction = clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"

t0 = time()
test_score = clf.score(features_train, labels_train)
print 'Test data score:{0} Time to process:{1}'.format(test_score, round(time()-t0, 3))

t0 = time()
score = accuracy_score(prediction, labels_test)
print 'Prediction score:{0} Time to process:{1}'.format(score, round(time()-t0, 3))

#########################################################
### your code goes here ###


#########################################################
