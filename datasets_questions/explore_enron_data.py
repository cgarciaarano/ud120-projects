#!/usr/bin/python

"""
    starter code for exploring the Enron dataset (emails + finances)
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

def find_guy(person):
    for key in enron_data.keys():
        if person in key:
            print('Person: {0}'.format(key))
            for feature in enron_data[key].keys():
                print('\t{0} : {1}'.format(feature, enron_data[key][feature]))


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

question = 12

if question == 1:
    print('Number of people: {0}'.format(len(enron_data.keys())))

if question == 2:
    for key in enron_data.keys():
        print('Number of features: {0}'.format(len(enron_data[key])))
        break

if question == 3:
    acc = 0
    for key in enron_data.keys():
        if enron_data[key]['poi']:
            acc += 1
    print('Number of POIs: {0}'.format(acc))

if question == 4:
 person = 'PRENTICE JAMES'
 find_guy(person)

if question == 5:
 person = 'COLWELL WESLEY'
 find_guy(person)

if question == 6:
 person = 'SKILLING JEFFREY'
 find_guy(person)

if question == 7:
 person = 'SKILLING JEFFREY'
 find_guy(person)
 person ='LAY KENNETH'
 find_guy(person)
 person = 'FASTOW'
 find_guy(person)

if question == 8:

    salary = [ x for x in enron_data.keys() if enron_data[x]['salary'] != 'NaN']
    print("N of people with salary: {0}".format(len(salary)))

    email = [ x for x in enron_data.keys() if enron_data[x]['email_address'] != 'NaN']
    print("N of people with email: {0}".format(len(email)))

if question == 9:
    total_payments = [ x for x in enron_data.keys() if enron_data[x]['total_payments'] == 'NaN']
    print("N of people without total_payments: {0}".format(len(total_payments)))    
    print("Percentage without total_payments: {0}".format(len(total_payments)/float(len(enron_data.keys()))*100))  

if question == 10:
    total_payments_poi = [ x for x in enron_data.keys() if enron_data[x]['total_payments'] == 'NaN' and enron_data[x]['poi'] ]
    n_pois = [ x for x in enron_data.keys() if  enron_data[x]['poi'] ]
    print("N of POIs without total_payments: {0}".format(len(total_payments_poi)))    
    print("Percentage POIs without total_payments: {0}".format(len(total_payments_poi)/float(len(n_pois))*100))  


if question == 11:    
    total_payments = [ x for x in enron_data.keys() if enron_data[x]['total_payments'] == 'NaN']
    print("N of people without total_payments: {0}".format(len(total_payments)+10))    
    print("Percentage without total_payments: {0}".format(len(total_payments)+10/float(len(enron_data.keys())+10)*100))  

if question == 12:    
    total_payments_poi = [ x for x in enron_data.keys() if enron_data[x]['total_payments'] == 'NaN' and enron_data[x]['poi'] ]
    n_pois = [ x for x in enron_data.keys() if  enron_data[x]['poi'] ]
    print("N of POIs: {0}".format(len(n_pois)+10))    
    print("N of POIs without total_payments_poi: {0}".format((len(total_payments_poi)+10)))  