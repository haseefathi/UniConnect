from project.project_data_paths import paths

from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from fuzzywuzzy import process
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn import svm
import math as m




def get_corrected_uni_name(college_name):

    data_file_path = paths['university_admissions_data']

    column_names = ['uniNames', 'majors','degrees', 'seasons', 'decisions', 'gpa', 'verbal_scores', 'quant_scores', 'awa_scores','toefl_scores']

    data = pd.read_csv(data_file_path, names = column_names, header = None)

    if college_name is not None:
        unis = data.uniNames
        all_unis = list()
        for uni in unis:
            if uni not in all_unis:
                all_unis.append(uni)

        current_uni = process.extractOne(college_name, all_unis)

        if current_uni[1] < 80:
            college_name = None
        else:
            college_name = current_uni[0]

    return college_name




def get_acceptance_rate(college_name):

    data_file_path = paths['university_admissions_data']
    column_names = ['uniNames', 'majors','degrees', 'seasons', 'decisions', 'gpa', 'verbal_scores', 'quant_scores', 'awa_scores','toefl_scores']

    data = pd.read_csv(data_file_path, names = column_names, header = None)

    # extracting data for the university searched for by the user 
    uni_data = data[data['uniNames'] == college_name]
    decision_data = uni_data[(uni_data['decisions'] == 'Accepted')]

    if decision_data is not None:
        # getting decision stats 
        accepted_count = uni_data[uni_data['decisions'] == 'Accepted'].decisions.count()
        rejected_count = uni_data[uni_data['decisions'] == 'Rejected'].decisions.count()
        waitlisted_count = uni_data[uni_data['decisions'] == 'Wait Listed'].decisions.count()
        interview_count = uni_data[uni_data['decisions'] == 'Interview'].decisions.count()
        other_decisions_count = uni_data[uni_data['decisions'] == 'Other'].decisions.count()

        total_applications = accepted_count + rejected_count+ waitlisted_count + interview_count + other_decisions_count

        # acceptance_rate = float("%.2f" % float(accepted_count) / float(total_applications)) * 100

        acceptance_ratio = float((accepted_count/float(total_applications)))
        acceptance_rate = float("%.2f" % (acceptance_ratio*100))

        return acceptance_rate
    else:
        return None




def normalize_student_data(student_info):
    intended_field = student_info.get('intended_field')
    undergrad_gpa = float(student_info.get('undergrad_gpa'))
    gre_verbal_score = float(student_info.get('gre_verbal_score'))
    gre_quant_score = float(student_info.get('gre_quant_score'))
    gre_awa_score = float(student_info.get('gre_awa_score'))
    toefl_score = float(student_info.get('toefl_score'))


    gre_range = float(170.0 - 130.0)
    gpa_range = float(4.0 - 0.25)
    awa_range = float(6.0 - 0.30)
    toefl_range = float(120.0 - 57.0)

    # normalizing all the scores
    normalized_undergrad_gpa = float(undergrad_gpa - 0.25) / gpa_range
    normalized_gre_verbal_score = float(gre_verbal_score - 130.0) / gre_range
    normalized_gre_quant_score = float(gre_quant_score - 130.0) / gre_range
    normalized_gre_awa_score = float(gre_awa_score - 0.30) / awa_range
    normalized_toefl_score = float(toefl_score - 57.0) / toefl_range

    # creating the normalized student variable
    normalized_data = [normalized_undergrad_gpa, normalized_gre_verbal_score, normalized_gre_quant_score, normalized_gre_awa_score, normalized_toefl_score]

    normalized_student = np.array(normalized_data)
    normalized_student = normalized_student.reshape(1,-1)

    return normalized_student




def get_knn_predictions(college_name, student_info):
    data_file_path = paths['university_admissions_data']

    student_intended_major = student_info.get('intended_field')
    normalized_student = normalize_student_data(student_info)

    column_names = ['uniNames', 'majors','degrees', 'seasons', 'result', 'gpa', 'verbal_scores', 'quant_scores', 'awa_scores','toefl_scores']

    data = pd.read_csv(data_file_path, names = column_names, header = None )
    data.fillna(0, inplace = True)

    majors_data = data[(data['majors'] == student_intended_major) & (data['uniNames'] == college_name)]

    print(len(majors_data)) 
    majors_data_1 = majors_data
    majors_data_2 = majors_data
    majors_data_3 = majors_data
    majors_data_4 = majors_data
    majors_data_5 = majors_data

    frames = [majors_data, majors_data_1, majors_data_2, majors_data_3, majors_data_4, majors_data_5]

    majors_multiplied = pd.concat(frames)

    if len(majors_multiplied) > 25:

        # x - design matrix
        x = np.array(majors_multiplied.iloc[: ,5:10])
        # y - the target vector
        y = np.array(majors_multiplied['result'])
        z = np.array(majors_multiplied.iloc[:, 0:5])

        # getting only the uni, major and final result
        z1 = z[:, np.array([True, True, False, False, True])]

        # print("---printing everything----")
        # print("__________x__________")
        # print(x)
        # print("___________y__________")
        # print(y)
        # print("_________Z_______")
        # print(z)
        # print("__________z1_________")
        # print(z1)

        # splitting the data into training and test set
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 4)

        # creating knn model with k = 15
        knn_model = KNeighborsClassifier(n_neighbors = 15)

        # performing cross validation (CV)
        cv_scores = cross_val_score(knn_model, x, y, cv=25, scoring = 'accuracy')

        cv_accuracy = cv_scores.mean()
        accuracy_percent = float('%.2f' % (cv_accuracy * 100))
        # print('cv accuracy knn:' , accuracy_percent)

        # model fitting using training data
        knn_model.fit(x_train, y_train)

        # predicting admission chances for current student
        admission_prediction = knn_model.predict(normalized_student)
        # print('adm pred', admission_prediction)

        if admission_prediction == "Accepted":
            acceptance_chance = accuracy_percent
        else:
            acceptance_chance = 100 - accuracy_percent
        
        knn_prediction = {
            'prediction': admission_prediction,
            'acceptance_chance': acceptance_chance,
            'rejection_chance': 100 - acceptance_chance,
            'accuracy': accuracy_percent
        }

        return knn_prediction




def get_random_forest_prediction(college_name, student_info):
    data_file_path = paths['university_admissions_data']

    student_intended_major = student_info.get('intended_field')
    normalized_student = normalize_student_data(student_info)

    column_names = ['uniNames', 'majors','degrees', 'seasons', 'result', 'gpa', 'verbal_scores', 'quant_scores', 'awa_scores','toefl_scores']

    data = pd.read_csv(data_file_path, names = column_names, header = None )
    data.fillna(0, inplace = True)

    majors_data = data[(data['majors'] == student_intended_major) & (data['uniNames'] == college_name)]

    majors_data_1 = majors_data
    majors_data_2 = majors_data
    majors_data_3 = majors_data
    majors_data_4 = majors_data
    majors_data_5 = majors_data

    frames = [majors_data, majors_data_1, majors_data_2, majors_data_3, majors_data_4, majors_data_5]

    majors_multiplied = pd.concat(frames)


    # ----------------------------------------------------------
    majors_data['gpa'] = majors_data.gpa.astype(float)
    majors_data['verbal_scores'] = majors_data.verbal_scores.astype(float)
    majors_data['quant_scores'] = majors_data.quant_scores.astype(float)
    majors_data['awa_scores'] = majors_data.awa_scores.astype(float)
    majors_data['toefl_scores'] = majors_data.toefl_scores.astype(float)
    # ----------------------------------------------------------


    # making all scores of type float
    majors_multiplied['gpa'] = majors_multiplied.gpa.astype(float)
    majors_multiplied['verbal_scores'] = majors_multiplied.verbal_scores.astype(float)
    majors_multiplied['quant_scores'] = majors_multiplied.quant_scores.astype(float)
    majors_multiplied['awa_scores'] = majors_multiplied.awa_scores.astype(float)
    majors_multiplied['toefl_scores'] = majors_multiplied.toefl_scores.astype(float)

    dataframe = majors_multiplied.loc[:,'gpa':'toefl_scores']

    # creating x and y
    x = np.array(dataframe)
    y = np.array(majors_multiplied.loc[:,['result']])


    # creating x and y
    x1 = np.array(majors_data.loc[:,'gpa':'toefl_scores'])
    y1 = np.array(majors_data.loc[:,['result']])

    # splitting into train and test set
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 4)

    # creating random forest classifier
    rf_model = RandomForestClassifier(
        bootstrap = True, 
        class_weight = None, 
        criterion = 'gini', 
        max_depth = None, 
        max_features = 'auto', 
        max_leaf_nodes = None, 
        min_samples_leaf = 1, 
        min_samples_split = 2, 
        min_weight_fraction_leaf = 0.0, 
        n_estimators = 500, 
        n_jobs = 2, 
        oob_score = False
    )

    # training and fitting model
    rf_model.fit(x_train, y_train)

    # testing on test data
    test_prediction = rf_model.predict(x_test)

    test_decision_accuracy = rf_model.predict_proba(x_test)

    # getting prediction for current student
    admission_prediction = rf_model.predict(normalized_student)
    # print('rf pred', admission_prediction)
    

    # my calculation of accuracies
    acc = rf_model.score(x_test, y_test)
    print('my calculation of accuracy of rf on test set', acc)
    acc = rf_model.score(x_train, y_train)
    print('my calculation of accuracy of rf on train set', acc)


    # getting chance of acceptance
    accuracies = rf_model.predict_proba(normalized_student)

    accuracies_list = accuracies.tolist()
    # print('rf acc', accuracies_list)

    acceptance_probability = (accuracies_list[0])[0]
    acceptance_chance = float('%.2f' % (acceptance_probability * 100))
    # print('rf acceptance chance', acceptance_chance)

    rf_prediction = {
        'prediction': admission_prediction,
        'acceptance_chance': acceptance_chance, 
        'rejection_chance': 100 - acceptance_chance
    }

    return rf_prediction




def get_svm_prediction(college_name, student_info):
    data_file_path = paths['university_admissions_data']

    student_intended_major = student_info.get('intended_field')
    normalized_student = normalize_student_data(student_info)

    column_names = ['uniNames', 'majors','degrees', 'seasons', 'result', 'gpa', 'verbal_scores', 'quant_scores', 'awa_scores','toefl_scores']

    data = pd.read_csv(data_file_path, names = column_names, header = None )

    majors_data = data[(data['majors'] == student_intended_major)] 
    majors_data = majors_data[majors_data['uniNames'] == college_name]

    f1 = majors_data
    f2 = majors_data
    f3 = majors_data
    f4 = majors_data
    f5 = majors_data

    # creating dataframe
    frames = [majors_data, f1, f2, f3, f4, f5]
    dataframe = pd.concat(frames)

    # making all scores in dataframe as float
    dataframe['gpa'] = dataframe.gpa.astype(float)
    dataframe['verbal_scores'] = dataframe.verbal_scores.astype(float)
    dataframe['quant_scores'] = dataframe.quant_scores.astype(float)
    dataframe['awa_scores'] = dataframe.awa_scores.astype(float)
    dataframe['toefl_scores'] = dataframe.toefl_scores.astype(float)

    # creating x and y
    x = np.array(dataframe.loc[:, 'gpa':'toefl_scores'])
    y = np.array(dataframe.loc[:, ['result']])

    # print('-------x---------')
    # print(x)
    # print('-------y---------')
    # print(y)

    # splitting into train and test set
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 4)

    # create svm model
    svm_model = svm.SVC(kernel = 'linear', C = 0.001)

    # fitting the model
    svm_model.fit(x_train, y_train)

    # model evaluation on test data
    test_predictions = svm_model.predict(x_test)
    test_accuracy = svm_model.score(x_test, y_test)
    # print('svm accuracy on test set', test_accuracy)

    # predicting for current student
    admission_prediction = svm_model.predict(normalized_student)
    # print('svm pred', admission_prediction)

    if admission_prediction == 'Accepted':
        acceptance_chance = float('%.2f' % (test_accuracy * 100))
    else:
        acceptance_chance = 100 - float('%.2f' % (test_accuracy * 100))
    

    svm_prediction = {
        'prediction': admission_prediction, 
        'acceptance_chance': acceptance_chance, 
        'accuracy': test_accuracy * 100, 
        'rejection_chance': 100 - acceptance_chance
    }

    return svm_prediction




def get_final_prediction(knn_prediction, rf_prediction, svm_prediction):
    all_predictions = [knn_prediction, rf_prediction, svm_prediction]

    
    # calculating chance of acceptance and rejection
    final_acceptance_chance = 0
    final_rejection_chance = 0
    for pred in all_predictions:
        final_acceptance_chance += pred['acceptance_chance']
        final_rejection_chance += pred['rejection_chance']
    final_acceptance_chance /= 3
    final_rejection_chance /= 3

    print('final acceptance chance', final_acceptance_chance)
    print('final rejection chance', final_rejection_chance)

    if final_acceptance_chance > final_rejection_chance:
        final_prediction = 'Acceptance'
    else:
        final_prediction = 'Rejection'

    
    
    final_prediction_info = {
        'final_prediction': final_prediction, 
        'acceptance_chance': final_acceptance_chance, 
        'rejection_chance': final_rejection_chance
    }

    return final_prediction_info
    



def classify_college(acceptance_chance):
    if acceptance_chance >= 70:
        return ['Safe', 'green']
    elif acceptance_chance >= 35:
        return ['Moderate', 'orange']
    else:
        return ['Reach', 'red']


    
def get_predictions(college_name, student_info):

    college_name = get_corrected_uni_name(college_name)
    # print(college_name)

    if not student_info['profile_updated']:
        # student hasnt updated profile...so gotta get the acceptance rate of uni since cant personalize for student

        acceptance_rate = get_acceptance_rate(college_name)
        context = {
            'acceptance_rate': acceptance_rate,
            'error': False,
            'processed': True,
            'profile_updated': False,
            'college_name': college_name
        }

    else: 
        # student has updated profile...so gotta get the correct predictions using classifiers

        knn_prediction = get_knn_predictions(college_name, student_info)
        rf_prediction = get_random_forest_prediction(college_name, student_info)
        svm_prediction = get_svm_prediction(college_name, student_info)

        print('prediction using knn', knn_prediction['prediction'], knn_prediction['acceptance_chance'], knn_prediction['accuracy'])
        print('prediction using rf', rf_prediction['prediction'], rf_prediction['acceptance_chance'])
        print('prediction using svm', svm_prediction['prediction'], svm_prediction['acceptance_chance'], svm_prediction['accuracy'] )

        final_prediction = get_final_prediction(knn_prediction, rf_prediction, svm_prediction)
        school_type = classify_college(final_prediction.get('acceptance_chance'))
        print(school_type[1])

        context = {
            'college_name': college_name,
            'error': False,
            'processed': True,
            'profile_updated': True, 
            'final_prediction': final_prediction, 
            'knn_prediction': knn_prediction,
            'rf_prediction': rf_prediction, 
            'svm_prediction': svm_prediction, 
            'final_prediction_acceptance': final_prediction['acceptance_chance'],
            'knn_prediction_acceptance': knn_prediction['acceptance_chance'], 
            'rf_prediction_acceptance': rf_prediction['acceptance_chance'], 
            'svm_prediction_acceptance': svm_prediction['acceptance_chance'], 
            'school_type': school_type[0],
            'color': school_type[1]
        }
        
    return context
