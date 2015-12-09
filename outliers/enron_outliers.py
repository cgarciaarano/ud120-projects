#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]

data_dict.pop('TOTAL')

data = featureFormat(data_dict, features)


### Find outlier
import math
for fulano in data_dict.keys():
	if data_dict[fulano]['salary'] != 'NaN' and data_dict[fulano]['bonus'] != 'NaN':
		if data_dict[fulano]['salary'] > 8000000 and data_dict[fulano]['bonus'] > 2500000:
			print('{0}: Salary {1} Bonus: {2}'.format(fulano,data_dict[fulano]['salary'], data_dict[fulano]['bonus'] ))

### Find outliers
import math
for fulano in data_dict.keys():
	if data_dict[fulano]['salary'] != 'NaN' and data_dict[fulano]['bonus'] != 'NaN':
		if data_dict[fulano]['salary'] > 1000000 and data_dict[fulano]['bonus'] > 5000000:
			print('{0}: Salary {1} Bonus: {2}'.format(fulano,data_dict[fulano]['salary'], data_dict[fulano]['bonus'] ))

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.savefig("test.png")
matplotlib.pyplot.show()
