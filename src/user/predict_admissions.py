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
        context = {
            'college_name': college_name,
            'prediction': 'yellow',
            'error': False,
            'processed': True,
            'profile_updated': True
        }
        
    return context


