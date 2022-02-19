# UniConnect
### A Social Networking Platform for Prospective Graduate Students. See it <a href = "http://uniconnect2021.herokuapp.com/">here!</a><br>

## Description
This is a platform which allows upcoming students to find others all around the world and communicate with them through real-time messaging. Users will be allowed to register and create an account on the platform and create profiles and make connections with others. Additionally, there will also be other services on the web application such as a university admissions predictor and a university recommender system which can be used by students to help in decision making. Students will also be able to view statistics of different universities available on the database and see how they compare to others who were admitted to the university. <br>

#### Packages used:
Django, TensorFlow, Keras, NumPy, pandas, scikit-learn, websockets, asyncio, Google Custom Search API

## Analysis of Machine Learning Models used:
Data scraped off the internet from: Edulix, Reddit, RateMyProfessor, Unigo using Selenium and BS4 web scrapers.
#### Admissions Predictor Model Accuracies
| Model         | Accuracy |
|---------------|----------|
| kNN           | 82.64%   |
| SVM           | 72.53%   |
| Random Forest | 84.2%    |

#### University Recommender System
The recommender system has a good accuracy of ~81% on test data. (Models based on kNN and neural networks)

#### Sentiment Analysis Model
The model has an accuracy of 82%, which is good enough. (Model based on Naive Bayes) 

## Screenshots

### Profile
#### Home Page
![home](https://github.com/haseefathi/UniConnect/blob/master/screenshots/home.png)

#### Login and SignUp pages

| Login | SignUp |
|-------|--------|
|   ![login](https://github.com/haseefathi/UniConnect/blob/master/screenshots/login.png)    |     ![signup](https://github.com/haseefathi/UniConnect/blob/master/screenshots/signup.png)
   |

#### Account Home page with navbar
 ![user home](https://github.com/haseefathi/UniConnect/blob/master/screenshots/accthome.png)     
![navbar](https://github.com/haseefathi/UniConnect/blob/master/screenshots/navbar.png)

### Universities:
![unis](https://github.com/haseefathi/UniConnect/blob/master/screenshots/universities.png)

#### University Statistics:
![stats](https://github.com/haseefathi/UniConnect/blob/master/screenshots/stats.png)

#### Admission Predictions:
![preds](https://github.com/haseefathi/UniConnect/blob/master/screenshots/pred.png)

#### Recommendations:
![recs](https://github.com/haseefathi/UniConnect/blob/master/screenshots/recs.png)

### Social Media Component:

#### Find Connections:
![conns](https://github.com/haseefathi/UniConnect/blob/master/screenshots/findconns.png)

#### Friends:
![friends](https://github.com/haseefathi/UniConnect/blob/master/screenshots/friends.png)

#### Messaging:
![messages](https://github.com/haseefathi/UniConnect/blob/master/screenshots/messages.png)





