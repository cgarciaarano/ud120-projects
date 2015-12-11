#!/usr/bin/python 

""" 
    skeleton code for k-means clustering mini-project

"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than 4 clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

exercise = 5
if exercise in (1,2):
    ### the input features we want to use 
    ### can be any key in the person-level dictionary (salary, director_fees, etc.) 
    feature_1 = "salary"
    feature_2 = "exercised_stock_options"
    feature_3 = "total_payments"
    poi  = "poi"
    features_list = [poi, feature_1, feature_2, feature_3]
    data = featureFormat(data_dict, features_list )
    poi, finance_features = targetFeatureSplit( data )


    ### in the "clustering with 3 features" part of the mini-project,
    ### you'll want to change this line to 
    ### for f1, f2, _ in finance_features:
    ### (as it's currently written, line below assumes 2 features)
    for f1, f2, _ in finance_features:
        plt.scatter( f1, f2 )
        
    plt.savefig('plot.png')    
    plt.show()



    from sklearn.cluster import KMeans
    # features_list = [poi, feature_1, feature_2, feature_3]
    # data2 = featureFormat(data_dict, features_list )
    # poi, finance_features = targetFeatureSplit( data2 )
    clf = KMeans(n_clusters=2)
    pred = clf.fit_predict( finance_features )
    Draw(pred, finance_features, poi, name="clusters_before_scaling.pdf", f1_name=feature_1, f2_name=feature_2)


    ### cluster here; create predictions of the cluster labels
    ### for the data and store them to a list called pred

    try:
        Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
    except NameError:
        print "no predictions object named pred found, no clusters to plot"


if exercise in (3,):
    min_eso = 5000
    max_eso = 0
    for fulano in data_dict.keys():
        if data_dict[fulano]['exercised_stock_options'] != 'NaN':
            max_eso = data_dict[fulano]['exercised_stock_options'] if (data_dict[fulano]['exercised_stock_options'] > max_eso) else max_eso
            min_eso = data_dict[fulano]['exercised_stock_options'] if (data_dict[fulano]['exercised_stock_options'] < min_eso) else min_eso
    print('Max: {0} Min:{1}'.format(max_eso, min_eso))

if exercise in (4,):
    min_s = 5000
    max_s = 0
    for fulano in data_dict.keys():
        if data_dict[fulano]['salary'] != 'NaN':
            max_s = data_dict[fulano]['salary'] if (data_dict[fulano]['salary'] > max_s) else max_s
            min_s = data_dict[fulano]['salary'] if (data_dict[fulano]['salary'] < min_s) else min_s
    print('Max: {0} Min:{1}'.format(max_s, min_s))

if exercise in (5,):
    ### the input features we want to use 
    ### can be any key in the person-level dictionary (salary, director_fees, etc.) 
    feature_1 = "salary"
    feature_2 = "exercised_stock_options"
    feature_3 = "total_payments"
    poi  = "poi"
    features_list = [poi, feature_1, feature_2]
    data = featureFormat(data_dict, features_list )
    poi, finance_features = targetFeatureSplit( data )


    ### in the "clustering with 3 features" part of the mini-project,
    ### you'll want to change this line to 
    ### for f1, f2, _ in finance_features:
    ### (as it's currently written, line below assumes 2 features)
    for f1, f2 in finance_features:
        plt.scatter( f1, f2 )
        
    plt.savefig('plot.png')    
    plt.show()



    from sklearn.cluster import KMeans
    clf = KMeans(n_clusters=2)
    pred = clf.fit_predict( finance_features )
    Draw(pred, finance_features, poi, name="clusters_before_scaling.pdf", f1_name=feature_1, f2_name=feature_2)


    ### cluster here; create predictions of the cluster labels
    ### for the data and store them to a list called pred

    try:
        Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
    except NameError:
        print "no predictions object named pred found, no clusters to plot"
