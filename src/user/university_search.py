from project.project_data_paths import paths
import pandas as pd
from fuzzywuzzy import process
from matplotlib.pyplot import figure
from matplotlib.legend import Legend
from bokeh.embed import components


def university_search(college_name):

    data_file_path = paths['university_admissions_data']

    column_names = ['uniNames', 'majors','degrees', 'seasons', 'decisions', 'gpa', 'verbal_scores', 'quant_scores', 'awa_scores','toefl_scores']

    data = pd.read_csv(data_file_path, names = column_names, header = None)

    if college_name is not None:
        unis = data.uniNames

        all_unis = list()

        for uni in unis:
            if uni not in all_unis:
                all_unis.append(uni)

        print(len(all_unis))

        current_uni = process.extractOne(college_name, all_unis)

        if current_uni[1] < 80:
            college_name = None
        else:
            college_name = current_uni[0]

    # extracting data for the university searched for by the user 
    uni_data = data[data['uniNames'] == college_name]
    decision_data = uni_data[(uni_data['decisions'] == 'Accepted')]

    if decision_data is not None:
        decision_data['greScores'] = (decision_data[['verbal_scores','quant_scores']].sum(axis = 1))

        # calculating the average, max, min gre score of those who were accepted 
        average_gre = float("%.2f" % (decision_data['greScores'].dropna()).mean())
        min_gre = (decision_data['greScores'].dropna()).min()
        max_gre = (decision_data['greScores'].dropna()).max()

        # calculating stats for verbal gre
        avg_verbal = (decision_data['verbal_scores'].dropna()).mean()
        min_verbal = (decision_data['verbal_scores'].dropna()).min()
        max_verbal = (decision_data['verbal_scores'].dropna()).max()

        # calculating stats for quant gre scores 
        avg_quant = (decision_data['quant_scores'].dropna()).mean()
        min_quant = (decision_data['quant_scores'].dropna()).min()
        max_quant = (decision_data['quant_scores'].dropna()).max()

        # calculating stats for undergrad gpa
        average_gpa = (decision_data['gpa'].dropna()).mean()
        min_gpa = (decision_data['gpa'].dropna()).min()
        max_gpa = (decision_data['gpa'].dropna()).max()

        # calculating stats for toefl scores 
        average_toefl = float("%.2f" % (decision_data['toefl_scores'].dropna()).mean())
        min_toefl = (decision_data['toefl_scores'].dropna()).min()
        max_toefl = (decision_data['toefl_scores'].dropna()).max()

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


        # getting all the majors offered in uni
        majors = uni_data.majors

        all_majors = list()
        for major in majors: 
            if major not in all_majors:
                all_majors.append(major)

        majors_count = len(all_majors)


        context = {
            'college_name': college_name,
            
            # gre info
            'average_gre': average_gre,
            'min_gre': min_gre,
            'max_gre': max_gre,

            # gre verbal info
            'average_verbal': avg_verbal,
            'min_verbal': min_verbal,
            'max_verbal': max_verbal,

            # gre quant info
            'average_quant': avg_quant,
            'min_quant': min_quant,
            'max_quant': max_quant,

            # gpa info
            'average_gpa': average_gpa,
            'min_gpa': min_gpa,
            'max_gpa': max_gpa,

            # toefl info
            'average_toefl': average_toefl,
            'min_toefl': min_toefl,
            'max_toefl': max_toefl,

            # decision stats info
            'acceptance_rate': acceptance_rate,

            # majors offered info
            'majors_count': majors_count,

            # if any errors in finding uni
            'error': False
        }
    
    else:
        context = {
            'error': True
        }

    return context