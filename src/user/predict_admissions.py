from project.project_data_paths import paths

from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from fuzzywuzzy import process
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn import svm




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
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 4)

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
            'acceptance_chance': acceptance_chance
        }

        return knn_prediction





def get_predictions(college_name, student_info):

    college_name = get_corrected_uni_name(college_name)
    print(college_name)

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
        print('prediction using knn', knn_prediction['prediction'], knn_prediction['acceptance_chance'])

        context = {
            'college_name': college_name,
            'prediction': 'yellow',
            'error': False,
            'processed': True,
            'profile_updated': True
        }
        
    return context


