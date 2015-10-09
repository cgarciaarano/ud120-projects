#!/usr/bin/python

"""
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors

    Sara has label 0
    Chris has label 1

"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

full_set = True
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


if not full_set:
    features_train = features_train[:len(features_train)/100]
    labels_train = labels_train[:len(labels_train)/100]


#for C in [10.0,100.,1000.,10000.]:
for C in [10000.]:
    clf = SVC(kernel='rbf', C = C)

    t0 = time()
    clf.fit(features_train, labels_train)
    print "training time:", round(time()-t0, 3), "s"

    t0 = time()
    prediction = clf.predict(features_test)
    print "prediction time:", round(time()-t0, 3), "s"
    '''
    t0 = time()
    test_score = clf.score(features_train, labels_train)
    print 'Test data score:{0} Time to process:{1}'.format(test_score, round(time()-t0, 3))
    '''
    t0 = time()
    '''
    # Iterative score
    correct_ctr = 0
    for i in range(len(prediction)):
            if prediction[i] == labels_test[i]:
                correct_ctr += 1
            else:
                print('Pred:{0} Truth:{1}'.format(prediction[i],labels_test[i]))

    print('Counter:{0} Totaal:{1}'.format(correct_ctr,len(prediction)))
    score = float(correct_ctr) / len(prediction)
    '''
    score = accuracy_score(labels_test, prediction)
    print 'Prediction score:{0} Time to process:{1}'.format(score, round(time()-t0, 3))

    for i in (10,26,50):
        print('Answer for {0} is {1}'.format(i,prediction[i]))

    total = 0
    for i in range(len(prediction)):
        if prediction[i] == 1:
            total += 1
    print('There are {0} Chris predictions'.format(total))    
