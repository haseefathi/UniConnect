from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import confusion_matrix

import numpy as np
import itertools
import matplotlib.pyplot as plt
import pandas as pd

def get_all_data():
    root = "data/sentiment_analysis_data/"

    with open(root + "imdb_labelled.txt", "r") as text_file:
        data = text_file.read().split('\n')
         
    with open(root + "amazon_cells_labelled.txt", "r") as text_file:
        data += text_file.read().split('\n')

    with open(root + "yelp_labelled.txt", "r") as text_file:
        data += text_file.read().split('\n')

    return data


def preprocessing_data(data):
    processing_data = []
    for single_data in data:
        if len(single_data.split("\t")) == 2 and single_data.split("\t")[1] != "":
            processing_data.append(single_data.split("\t"))

    return processing_data


def split_data(data):
    total = len(data)
    training_ratio = 0.75
    training_data = []
    evaluation_data = []

    for indice in range(0, total):
        if indice < total * training_ratio:
            training_data.append(data[indice])
        else:
            evaluation_data.append(data[indice])

    return training_data, evaluation_data


def preprocessing_step():
    data = get_all_data()
    processing_data = preprocessing_data(data)

    print('preprocessed data')
    return split_data(processing_data)



def training_step(data, vectorizer):
    training_text = [data[0] for data in data]
    training_result = [data[1] for data in data]

    training_text = vectorizer.fit_transform(training_text)

    print('returning the fitted model')
    return BernoulliNB().fit(training_text, training_result)



def get_sentiment_analysis(college_name):   
    training_data, evaluation_data = preprocessing_step()
    vectorizer = CountVectorizer(binary = 'true')
    classifier = training_step(training_data, vectorizer)

    if college_name in ['New York University', 'Columbia University', 'Stanford University', 'Harvard University']:
        uni_reviews = pd.read_csv('data\\reviews.csv', header = 0, encoding = 'cp1252')
        data = uni_reviews.loc[uni_reviews['University'] == college_name]
        all_reviews = data['Review'].tolist()

        count_positive = 0
        count_all = len(all_reviews)
        for review in all_reviews:
            result = classifier.predict(vectorizer.transform([review]))
            if result[0] == '1': count_positive += 1

        pos_percent = (count_positive / count_all) * 100
        print('Percentage of positive reviews:', pos_percent)

        return pos_percent

    else:
        return None

    
print(get_sentiment_analysis('Harvard University'))


