from __future__ import print_function

import pandas as pd
import math
from sklearn import neighbors, datasets
from numpy.random import permutation
import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.preprocessing import Normalizer
# from sklearn.model_selection import train_test_split

# import for getting paths
from project.project_data_paths import paths

# libraries for CNN
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv1D, MaxPooling1D
from keras import backend as K
from math import sqrt


# for getting images of unis
from .university_search import get_university_images

# libraries for KNN
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt
from scipy.interpolate.fitpack2 import UnivariateSpline



# gets dataframe from csv
def get_cnn_data():
    data_file_path = paths['cnn_recommender_processed_data']
    data = pd.read_csv(data_file_path, header=0)
    return data



# splits data into train and test sets
def get_train_test_cnn(data):
    # pick random indices to split..test-size = 20%
    np.random.seed(42)
    rand_indices = permutation(data.index)
    test_size = math.floor(len(data)/5)

    # separating train and test data
    test_data  = data.loc[rand_indices[1:test_size]]
    train_data = data.loc[rand_indices[test_size:]]

    # getting x_train and y_train
    y_train = train_data['University']
    x_train = train_data
    x_train = x_train.drop('University',1)

    # getting x_test and y_test
    y_test = test_data['University']
    x_test = test_data
    x_test = x_test.drop('University',1)

    return x_train, y_train, x_test, y_test



# has 80% accuracy...picks a uni from top 10 universities in terms of amount of data available using CNN
def get_cnn_recommendation(student_info):

    print('getting cnn rec')

    # returns uni as an array form [0,1,0....0]
    def get_university_label(college_name):
        index = all_unis.index(college_name)
        initial_list = [0]*len(all_unis)
        initial_list[index] = 1
        return np.array(initial_list)

    def get_uni(x):
        return all_unis[x]


    # getting dataset
    data = get_cnn_data()
    # list of all unis in dataset
    all_unis = data['University'].unique().tolist()


    # splitting into train and test set
    x_train, y_train, x_test, y_test = get_train_test_cnn(data)


    # converting uni names to arrays in training set
    y_train_labels = list()
    for name in y_train :
        uni_array = get_university_label(name)
        y_train_labels.append(uni_array)
    y_train_labels = np.array(y_train_labels)

    # converting uni names to arrays in testing set
    y_test_labels = list()
    for name in y_test :
        uni_array = get_university_label(name)
        y_test_labels.append(uni_array)
    y_test_labels = np.array(y_test_labels)

    # loading cnn model
    cnn_model = keras.models.load_model('data\models\cnn_model')
    print('CNN loaded')


    # getting mean and standard deviations
    training_mean = np.mean(x_train, axis=0)
    train_std_deviation = np.std(x_train, axis=0)
    testing_mean = np.mean(x_test, axis=0)
    test_std_deviation = np.std(x_test, axis=0)



    gpa_scale = 4
    number_mean = data['Number'].mean()

    # getting mean and std of entire dataset
    total_data_mean = (training_mean + testing_mean)/2
    train_variance = train_std_deviation**2
    test_variance = test_std_deviation**2
    total_variance = (train_variance + test_variance) / 2
    total_data_std_deviation = np.sqrt(total_variance)

    toefl = student_info.get('toefl_score')
    verbal = student_info.get('gre_verbal_score')
    quant = student_info.get('gre_quant_score')
    awa = student_info.get('gre_awa_score')
    gpa = student_info.get('undergrad_gpa')

    student_x = [number_mean, toefl, verbal, quant, float(awa), float(gpa), gpa_scale]
    normalized_student = (student_x - testing_mean) / test_std_deviation

    final_student_input = list()
    for item in normalized_student:
        final_student_input.append([item])

    final_student_input = np.array([final_student_input])

    # getting recommendation for current student
    recommendation_output = cnn_model.predict(final_student_input)
    final_recommendation = get_uni(np.argmax(recommendation_output))

    uni_image_link = get_university_images(final_recommendation)[0]
    cnn_recommendation = {
        'recommendation': final_recommendation,
        'image_link': uni_image_link
    }

    return cnn_recommendation



def get_best_recommendation_knn(data, student_major, student_array):

    # filling empty values with 0
    data.fillna(0, inplace = True)

    # extracting only the accepted students data and those with same intended major
    frame1 = data[(data['majors'] == student_major) & (data['results'] == 'Accepted')]
    frame2 = frame1
    frame3 = frame1
    frame4 = frame1
    frame5 = frame1
    frame6 = frame1
    frame7 = frame1
    frame8 = frame1
    frame9 = frame1
    frame10 = frame1
    frame11 = frame1
    frame12 = frame1

    all_frames = [frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10, frame11, frame12]

    # getting final data
    final_data = pd.concat(all_frames)

    # making x and y matrices
    # x is everything except uni name
    x = np.array(final_data.iloc[:, 5:10])
    x = preprocessing.scale(x)
    # y is the university names
    y = np.array(final_data['uniName'])


    # getting train and test sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 4)

    
    # making knn model with k = 15
    knn_model = KNeighborsClassifier(n_neighbors = 15)

    # getting accuracy of model
    cv_scores = cross_val_score(knn_model, x, y, cv = 5, scoring = 'accuracy')
    best_uni_prediction_accuracy = cv_scores.mean()
    print('cv best pred acc', best_uni_prediction_accuracy)

    # fitting model to training data
    knn_model.fit(x_train, y_train)

    # making prediction for test data
    test_predictions = knn_model.predict(x_test)

    # making prediction for the current student
    student_best_uni_prediction = knn_model.predict(student_array)
    print('pred for student', student_best_uni_prediction)

    for name in student_best_uni_prediction:
        recommended_uni = name

    uni_image_link = get_university_images(recommended_uni)[0]
    # uni_image_link = 'https://base.imgix.net/files/base/ebm/asumag/image/2019/04/asumag_8934_uicrendering_0.png?auto=format&fit=crop&h=432&w=768'

    recommendation = {
        'recommendation': recommended_uni,
        'image_link': uni_image_link
    }

    return recommendation




def get_student_admission_info(data, student_major, student_array):
    
    # filling empty values with 0
    data.fillna(0, inplace = True)

    # extracting only the accepted students data and those with same intended major
    frame1 = data[(data['majors'] == student_major) & (data['results'] == 'Accepted')]

    # making frames
    frame2 = frame1
    frame3 = frame1
    frame4 = frame1
    frame5 = frame1
    frame6 = frame1
    frame7 = frame1
    frame8 = frame1

    # joining all frames
    all_frames = [frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8]

    # getting final data
    final_data = pd.concat(all_frames)

    # making x and y matrices
    # x is everything except uni name
    x = np.array(final_data.iloc[:, 5:10])
    x = preprocessing.scale(x)
    # y is the university names
    y = np.array(final_data['uniName'])



    # getting train and test sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 4)

    # making knn model with k = 15
    knn_model = KNeighborsClassifier(n_neighbors = 15)

    # getting cv accuracy
    cv_scores = cross_val_score(knn_model, x, y, cv = 25, scoring = 'accuracy')
    cv_accuracy = cv_scores.mean()
    # print('cv acc', cv_accuracy)

    # training model
    knn_model.fit(x_train, y_train)

    # getting predictions on test data and evaluating
    test_predictions = knn_model.predict(x_test)
    test_accuracy = accuracy_score(y_test, test_predictions)
    # print('test acc', test_accuracy)


    # getting admission prediction for current student
    student_adm_prediction = knn_model.predict(student_array)


    # getting only relevant columns (name, major, result)
    z = np.array(final_data.iloc[:, 0:5])
    z_required = z[:, np.array([True, True, False, False, True])]

    # getting the nearest neighbours to student
    nearest_neighbors = knn_model.kneighbors(student_array)
    
    names_of_neighbor_unis = z_required[nearest_neighbors[1]]
    # print(names_of_neighbor_unis)

    # separating accepted and rejected unis
    accepted_unis = np.array([])
    rejected_unis = np.array([])

    for i in range(0,8):
        if 'Accepted' in names_of_neighbor_unis[0,i]:
            acceptance_count = names_of_neighbor_unis[0,i]
            accepted_unis = np.append(accepted_unis, acceptance_count)

        else:
            rejection_count = names_of_neighbor_unis[0,i]
            rejected_unis = np.append(rejected_unis, rejection_count)

    # print('**********************************************************************************')
    # print(accepted_unis)
    # print(rejected_unis)


    def get_unique(unis):

        # getting only uni names
        names_list = np.array([])

        unique_list = list() # will hold the unique uni names
        num_unis = len(unis)

        for i in range(0, num_unis, 3):
            count_unique = unis[i]
            names_list = np.append(names_list, count_unique)
        
        # print('names',names_list)

        # getting unique names
        for name in names_list:
            if name not in unique_list:
                unique_list.append(name)

        return unique_list 

    # getting unique names from accepted and rejected unis
    accepted_names = get_unique(accepted_unis)
    rejected_names = get_unique(rejected_unis)

    return accepted_names





def get_knn_recommendation(student_info):

    data_file_path = paths['university_admissions_data']
    column_names = ['uniName', 'majors', 'degrees', 'seasons', 'results', 'gpa', 'verbal_score', 'quant_score', 'awa_score', 'toefl_score']
    data = pd.read_csv(data_file_path, names = column_names, header = None)


    toefl = student_info.get('toefl_score')
    verbal = student_info.get('gre_verbal_score')
    quant = student_info.get('gre_quant_score')
    awa = float(student_info.get('gre_awa_score'))
    gpa = float(student_info.get('undergrad_gpa'))
    major = student_info.get('intended_field')


    # normalizing all values
    norm_gpa = (gpa - 0.25) / (4 - 0.25)
    norm_verbal = (verbal - 130.0) / (170.0 - 130.0)
    norm_quant = (quant - 131.0) / (170.0 - 131.0)
    norm_awa = (awa - 0.30) / (6.0 - 0.30)
    norm_toefl = (toefl - 57.0) / (120.0 - 57.0)


    # creating student numpy array with scores
    student_array = np.array([
        norm_gpa, norm_verbal, norm_quant, norm_awa, norm_toefl
    ])
    student_array = student_array.reshape(1, -1)

    # getting prediction of best recommended university
    best_recommendation = get_best_recommendation_knn(data, major, student_array)

    # getting unis where student is accepted or rejected
    accepted_unis_recommendations = get_student_admission_info(data, major, student_array)

    # print(accepted_unis_recommendations)


    print('---------------------------final recs (knn)-------------------------------')
    all_knn_recommendations = list()

    for uni in accepted_unis_recommendations:
        recommendation = dict()
        current_uni_image_link = get_university_images(uni)[0]
        recommendation['recommendation'] =  uni
        recommendation['image_link'] = current_uni_image_link
        # recommendation['image_link'] = 'https://base.imgix.net/files/base/ebm/asumag/image/2019/04/asumag_8934_uicrendering_0.png?auto=format&fit=crop&h=432&w=768'
        all_knn_recommendations.append(recommendation)

    print(all_knn_recommendations)
    print('--------------------------- final recs (knn) as dicts -------------------------------')
    # for rec in all_knn_recommendations:
    #     print(rec)

    return best_recommendation, all_knn_recommendations




def get_recommendations(student_info):

    top_recommendation_cnn = get_cnn_recommendation(student_info)
    # top_recommendation_cnn = {
    #     'recommendation': 'University of Texas Dallas',
    #     'image_link': 'https://media-exp1.licdn.com/dms/image/C4E1BAQESsYKpD2giAg/company-background_10000/0/1545159143732?e=2159024400&v=beta&t=5WALs4hWnJVwj4BcI87hm9V_A1IC00GJMWXjggi-Sd4'
    # }

    best_knn_recommendation, remaining_predictions = get_knn_recommendation(student_info)
    # knn_recommendation = {
    #     'recommendation': 'University of Texas Dallas',
    #     'image_link': 'https://media-exp1.licdn.com/dms/image/C4E1BAQESsYKpD2giAg/company-background_10000/0/1545159143732?e=2159024400&v=beta&t=5WALs4hWnJVwj4BcI87hm9V_A1IC00GJMWXjggi-Sd4'
    # }

    all_recommendations = {
        'cnn_recommendation': top_recommendation_cnn,
        'best_knn_recommendation': best_knn_recommendation,
        'remaining_recommendations': remaining_predictions
    }

    return all_recommendations
