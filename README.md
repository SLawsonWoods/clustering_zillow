# clustering_zillow 
Sarah Lawson Woods September 2021
_________________________________________________________________________________________________________
**Table of Contents**

1.)  Project Summary
2.)  Project Objective & Goals
3.)  Audience
4.)  Project Deliverables


5.)  Project Context

6.)  Data Dictionary
7.)  Initial Hypothesis
8.)  Executive Summary - Conclusions & Next Steps**
9.)  Pipeline Stages Breakdown


10.)  Project Plan https://trello.com/b/FbVWBxd8/clustering-with-zillow
10a.) Data Acquisition
10b.) Data Preparation
10c.) Data Exploration
10d.) Modeling and Evaluation

11.)  Reproduce

________________________________________________________________________________________________________
**Project Summary**
Zillow's Zestimate is an estimate of value of a home using a formula they created. Zestimates have an accuracy of about 80%.  What drives errors between the zestimates and the actual sale price of the home?In this project working with a Zillow dataset I explore features of a home that are drivers for logerror, and create models to predict logerror. I want to establish if using clustering to explore my data will help me find these drivers and increase my model performance. 

_________________________________________________________________________________________________________
**Project Objectives & Goals**
Document code, process (data acquistion, preparation, exploratory data analysis including clusterng and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report. Create modules (acquire.py, prepare.py) that make your process repeateable. Construct 4 models to predict logerror using clustering techniqures if they prove to indicate useful features. Deliver a 4 minute presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above; your presentation should be appropriate for your audience the Zillow data science team.  Set aside one minute at the end of the presentation to answer questions about your code, process, findings and key takeaways, and models.

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
**Data Dictionary**

    Column Name                                                              Description

'airconditioningtypeid'                                Type of cooling system present in the home (if any)
'architecturalstyletypeid'	                           Architectural style of the home (i.e. ranch, colonial, split-level, etc)
'basementsqft'                                         Finished living area below or partially below ground level
'bathroomcnt'                                          Number of bathrooms in home including fractional bathrooms
'bedroomcnt'                                           Number of bedrooms in home
'buildingqualitytypeid'                                Overall assessment of condition building from best/lowest- worst/highest
'buildingclasstypeid'                                  The building framing type (steel frame, wood frame, concrete/brick)
'calculatedbathnbr'                                    Number of bathrooms in home including fractional bathroom
'decktypeid'                                           Type of deck (if any) present on parcel
'threequarterbathnbr'                                  Number of 3/4 bathrooms in house (shower + sink + toilet)
'finishedfloor1squarefeet'                             Size of the finished living area on the first (entry) floor of the home
'calculatedfinishedsquarefeet'                         Calculated total finished living area of the home
'finishedsquarefeet6'                                  Base unfinished and finished area
'finishedsquarefeet12'                                 Finished living area
'finishedsquarefeet13'                                 Perimeter living area
'finishedsquarefeet15'                                 Total area
'finishedsquarefeet50'                                 Size of the finished living area on the first (entry) floor of the home
'fips'                                                 Federal Information Processing Standard code - see                                                                              https://en.wikipedia.org/wiki/FIPS_county_code for more details
'fireplacecnt'                                         Number of fireplaces in a home (if any)
'fireplaceflag'                                        Is a fireplace present in this home
'fullbathcnt'                                          Number of full bathrooms (sink, shower + bathtub, and toilet) in home
'garagecarcnt'                                         Total number of garages on the lot including an attached garage
'garagetotalsqft'                                      Total number of square feet of all garages on lot
'hashottuborspa'                                       Does the home have a hot tub or spa
'heatingorsystemtypeid'                                Type of home heating system
'latitude'                                             Latitude of the middle of the parcel multiplied by 10e6
'longitude'                                            Longitude of the middle of the parcel multiplied by 10e6
'lotsizesquarefeet'                                    Area of the lot in square feet
'numberofstories'                                      Number of stories or levels the home has
'parcelid'                                             Unique identifier for parcels (lots)
'poolcnt'                                              Number of pools on the lot (if any)
'poolsizesum'                                          Total square footage of all pools on property
'pooltypeid10'                                         Spa or Hot Tub
'pooltypeid2'                                          Pool with Spa/Hot Tub
'pooltypeid7'                                          Pool without hot tub
'propertycountylandusecode'                            County land use code i.e. it's zoning at the county level
'propertylandusetypeid'                                Type of land use the property is zoned for
'propertyzoningdesc'                                   Description of the allowed land uses (zoning) for that property
'rawcensustractandblock'                               Census tract and block ID combined and blockgroup assignment by extension
'censustractandblock'                                  Census tract and block ID combined - also contains blockgroup assignment                                                        by extension
'regionidcounty'                                       County in which the property is located
'regionidcity'                                         City in which the property is located (if any)
'regionidzip'                                          Zip code in which the property is located
'regionidneighborhood'                                 Neighborhood in which the property is located
'roomcnt'                                              Total number of rooms in the principal residence
'storytypeid'                                          Type of floors in a multi-story house (i.e. basement and main level,                                                            split-level, attic, etc.). See tab for details.
'typeconstructiontypeid'                               What type of construction material was used to construct the home
'unitcnt'                                              Number of units the structure is built into (i.e. 2 = duplex, 3 =                                                                triplex, etc...)
'yardbuildingsqft17'                                   Patio in yard
'yardbuildingsqft26'                                   Storage shed/building in yard
'yearbuilt'                                            The Year the principal residence was built
'taxvaluedollarcnt'                                    The total tax assessed value of the parcel
'structuretaxvaluedollarcnt'                           The assessed value of the built structure on the parcel
'landtaxvaluedollarcnt'                                The assessed value of the land area of the parcel
'taxamount'                                            The total property tax assessed for that assessment year
'assessmentyear'                                       The year of the property tax assessment
'taxdelinquencyflag'                                   Property taxes for this parcel are past due as of 2015
'taxdelinquencyyear'                                   Year for which the unpaid propert taxes were due
_________________________________________________________________________________________________________
**Initial Hypotheses**

My initial ideas were that area of the home and acreage that the home sits on would be important features to explore and model with if they proved to have a strong correlation with logerror.

_________________________________________________________________________________________________________
**Executive Summary - Conclusions & Next Steps**

Goals: The purpose of this project is create a regression model with using Kmeans clusters (if proven valuable) to predicts the drivers of logerror of Zillow homes in three counties of California (Los Angeles County, Orange County, and Ventrua County).

Target: logerror which is the difference in the predicted zestimate and the actual home sale price

Findings: The three clusters I created were not insightful enough to use in modeling.  My four models all performed poorly and were beaten by the baseline.  My best model was the 3rd degree polynomial and was beaten by the baseline model by a small amount.

Results: Best predictors discovered were bedroom count, number of bedrooms and I found no significant clusters to use as features in modeling

Conclusion and Next Steps: Some initial exploration and statistical testing revealed that some features that had better correlation with logerror were bedroom and bathroom and with more time, I would like to test these features in clustering.


_________________________________________________________________________________________________________
**Pipeline Stages Breakdown**

Plan
- Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- Acquire data from the Codeup Database and create a function to automate this process. Save the function   in an acquire.py file to import into the Final Report Notebook.
- Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function   to automate the process, store the function in a prepare.py module, and prepare data in Final Report     Notebook by importing and using the function.
- Explore the dataset after preparation using visualizations, and clustering to identify potential 
  drivers of logerror.
- Establish a baseline accuracy and document well.
- Clearly define three hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- Train four different ML models incorporate drivers found while clustering as possible.
- Evaluate models on train and validate datasets.
- Choose the model with that performs the best and evaluate that single model on the test dataset.
- Document conclusions, takeaways, and next steps in the Final Report Notebook.
 
Plan -> Acquire
Store functions that are needed to acquire data selecting single family units, with transaction dates in the specified months and year, from the Zillow database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code. The final function will return a pandas DataFrame. Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
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
 Run the final_notebook.ipynb
 
_________________________________________________________________________________________________________

