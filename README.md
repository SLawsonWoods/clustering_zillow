# clustering_zillow 
Sarah Lawson Woods September 2021


_________________________________________________________________________________________________________
**Table of Contents**

1.)  Project Summary
2.)  Project Objective
3.)  Business Goals
4.)  Audience
5.)  Project Deliverables


6.)  Project Context
7.)  Data Dictionary**
8.)  Initial Hypothesis**
9.)  Executive Summary - Conclusions & Next Steps**


10.)  Pipeline Stages Breakdown
10a.) Project Plan
10b.) Data Acquisition
10c.) Data Preparation
10d.) Data Exploration
10e.) Modeling and Evaluation

11.)  Reproduce

________________________________________________________________________________________________________
**Project Summary**
Zillow's Zestimate is an estimate of value of a home using a formula they created. Zestimates have an accuracy of about 80%.  What drives errors between the zestimates and the actual sale price of the home?In this project working with a Zillow dataset I explore features of a home that are drivers for logerror, and create models to predict logerror. I want to establish if using clustering to explore my data will help me find these drivers and increase my model performance. 

_________________________________________________________________________________________________________
**Project Objectives**
Document code, process (data acquistion, preparation, exploratory data analysis including clusterng and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report. Create modules (acquire.py, prepare.py) that make your process repeateable. Construct 4 models to predict logerror using clustering techniqures if they prove to indicate useful features. Deliver a 4 minute presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above; your presentation should be appropriate for your audience the Zillow data science team.  Set aside one minute at the end of the presentation to answer questions about your code, process, findings and key takeaways, and models.

_________________________________________________________________________________________________________
**Business Goals**
Find drivers for logerror which is the difference between the actual sale price of a home and the zestimate. Answer the question, drives logerror? Construct 4 ML model that accurately predicts churn for each customer.
Document the process well enough to be presented or read like a report.

_________________________________________________________________________________________________________
**Audience**
The Zillow Data Science Team.

___________________________________________________________________________________________
**Project Deliverables**

A Jupyter Notebook Report
A README.md
A .py file for aquiring and one for preparing the data
A notebook presentation

_________________________________________________________________________________________________________
**Project Context**
The zillow dataset I am using comes from the Codeup database.

_________________________________________________________________________________________________________
**Data Dictionary

senior_citizen: Indicates if customer is a senior citizen                        (int)
tenure: Months customer has subscribed to service                                (int)
monthly_charges:  Dollar cost per month                                          (float)
total_charges:  Dollar cost accumulated during tenure                            (float)
internet_extras: Indicates if customer pays for internet add-ons                 (int)
streaming_entertainmen: Indicates if customer has streaming movies or tv         (int)
family:  Indicates if customer has dependents or partner                         (int)
gender_Male: Indicates if customer identifies as male                            (int)
phone_service_Yes: Indicates if customer has at least 1 phone line               (int)
paperless_billing_Yes: Indicates if customer uses paperless billing              (int)
churn_Yes: Indicates if customer has left the company                            (int)
contract_type_Month-to-month: Indicates if customer pays on a monthly basis      (int)
contract_type_One_year: Indicates if customer pays annually                      (int)
contract_type_Two_year: Indicates if customer pays bi-annually                   (int)
internet_service_type_DSL: Indicates if customer has DSL internet                (int)
internet_service_type_Fiber_optic: Indicates if customer has fiber optic internet(int)
internet_service_type_None: Indicates if customer does not have internet         (int)
payment_type_Bank_transfer: Indicates if customer pays using a bank account      (int)
payment_type_Credit_card: Indicates if customer pays using a credit card         (int)
payment_type_Electronic_check: Indicates if customer pays using e-check          (int)
payment_type_Mailed_check: Indicates if customer pays using paper check          (int)

_________________________________________________________________________________________________________
**Initial Hypotheses

Hypothesis 1: Let's see if there is a relationship between payment type and churn.
$H_0$: There is no relationship between payment type and churn, they are independent. 
$H_a$: There is a relationship between payment type and churn, they are dependent on each other. 
Outcome: I rejected the Null Hypothesis; there is a relationship between payment type and churn.

Hypothesis 2: Let's see if there is a relationship between being a senior citizen and churn.
alpha = .05
$H_0$: There is no relationship between being a senior citizen or not and churn, they are independent. 
$H_a$: There is a relationship between beinga a senior citizen or not and churn, they are dependent on each other.
Outcome: I rejected the Null Hypothesis; there is a relationship between being a senior citizen and churn.

_________________________________________________________________________________________________________
**Executive Summary - Conclusions & Next Steps**

I found that all of the classification models I created, LogisticRegression, DecisionTree, RandomForest, and KNeighbors predicted the species of Iris equally well using the features sepal_width, sepal_length, petal_length, petal_width.
I chose my DecisionTree model as my best model with a 90% accuracy rate for predicting my target value, species. This model outperformed my baseline score of 33% accuracy, so it has value.
Some initial exploration and statistical testing revealed that engineering some new features like petal area or sepal area might help my models predict with even more accuracy, and with more time, I would like to test this hypothesis.

_________________________________________________________________________________________________________
**Pipeline Stages Breakdown**

Plan
- Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- Acquire data from the Codeup Database and create a function to automate this process. Save the function   in an acquire.py file to import into the Final Report Notebook.
- Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function   to automate the process, store the function in a prepare.py module, and prepare data in Final Report     Notebook by importing and using the function.
- Explore the dataset after preparation using visualizations, and clustering to identify potential 
  drivers of logerror.
- Establish a baseline accuracy and document well.
- Clearly define three hypotheses, set an alpha, run the statistical tests needed, reject or fail to       reject the Null Hypothesis, and document findings and takeaways.
- Train four different ML models incorporate drivers found while clustering as possible.
- Evaluate models on train and validate datasets.
- Choose the model with that performs the best and evaluate that single model on the test dataset.
- Document conclusions, takeaways, and next steps in the Final Report Notebook.
 
Plan -> Acquire
Store functions that are needed to acquire data from the customers, contract_type, internet_service_types and payment_types tables from the telco database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
The final function will return a pandas DataFrame.
Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
Plot distributions of individual variables.

Plan -> Acquire -> Prepare
Store functions needed to prepare the telco data; make sure the module contains the necessary imports to run the code. The final function should do the following: - Split the data into train/validate/test. - Handle any missing values. - Handle erroneous data and/or outliers that need addressing. - Encode variables as needed. - Create any new features, if made for this project.
Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.

Plan -> Acquire -> Prepare -> Explore
Answer key questions, my hypotheses, and figure out the features that can be used in a classification model to best predict the target variable, churn.
Run at least 2 statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings.
Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). The goal is to identify features that are related to churn (the target), identify any data integrity issues, and understand 'how the data works'. If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.

Plan -> Acquire -> Prepare -> Explore -> Model
Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
Train (fit, transform, evaluate) multiple models.
Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe. Remove variables that seem to give no insight.

Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.

Plan -> Acquire -> Prepare -> Explore -> Model -> Deliver
Introduce myself and my project goals at the very beginning of my notebook walkthrough.
Summarize my findings at the beginning like I would for an Executive Summary.
Walk Codeup Data Science Team through the analysis I did to answer my questions and that lead to my findings. (Visualize relationships and Document takeaways.)
Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.

_________________________________________________________________________________________________________
**Reproduce My Project**

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook.

 Read this README.md
 Download the aquire.py, prepare.py, and final_report.ipynb files into your working directory
 Add your own env file to your directory. (user, password, host)
 Run the telco_final_report.ipynb notebook.
 
_________________________________________________________________________________________________________

