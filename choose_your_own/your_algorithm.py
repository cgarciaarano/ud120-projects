#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
import traceback

features_train, labels_train, features_test, labels_test = makeTerrainData()




### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
#################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier

print('Number of train features: {0}'.format(len(features_train)))
print('Number of test features: {0}'.format(len(features_test)))

exercise = 4

if exercise == 1:
    clf = RandomForestClassifier(max_depth = None, n_estimators = 10, max_features = 'auto')
    clf.fit(features_train, labels_train)

    acc = clf.score(features_test, labels_test)

    print("Accuracy of RandomForest: {0}".format(acc))

# Beat accuracy 93.6%
elif exercise == 2:
    max_acc = 0
    for max_depth in range(1,15):
        for n_estimators in range(1,30):
            for max_features in range(1,2):

                clf = RandomForestClassifier(max_depth = max_depth, n_estimators = n_estimators, max_features = max_features, criterion = 'gini')
                clf.fit(features_train, labels_train)

                acc = clf.score(features_test, labels_test)
                if acc > max_acc:
                    max_acc = acc
                    print("Accuracy of RandomForest(max_depth={0}, n_estimators={1}, max_features={2}) : {3}".format(max_depth, n_estimators, max_features,acc))


    print("Max Accuracy: {0}".format(max_acc))

if exercise == 4:
    max_acc = 0
    for n_estimators in range(1,100):
        clf = AdaBoostClassifier(n_estimators = n_estimators)
        clf.fit(features_train, labels_train)

        acc = clf.score(features_test, labels_test)

        if acc > max_acc:
            max_acc = acc
            print("Accuracy of AdaBoostClassifier(n_estimators={0}) : {1}".format(n_estimators, acc))


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
    print('Some kind of error. {0}'.format(traceback.format_exc()))
