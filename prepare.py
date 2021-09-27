import pandas as pd
import numpy as np
import seaborn as sns
import os
import matplotlib.pyplot as plt
from scipy import stats
import math
import sklearn.preprocessing
from sklearn.model_selection import train_test_split
import env
import wrangle_functions
np.random.seed(123)

def prep_function(df):
    df = prep_work1(df)
    df = drop_cols_null(df)
    df = prep_work2(df)
    # create a df with no outliers 
    df_no_outs =outlier_function(df,df.columns, 1.5)
    return df_no_outs, df

def prep_work1(df):
    """ This function, drops nulls, renames the columns to something more clear to understand, corrects datatypes, get's rid of 
    unneeded decimals, reassigns proper dataypes, and drops duplicates."""
    # create list of single unit propertylandusedesc
    single_prop_types = ['Single Family Residential', 'Condominium', 'Mobile Home',
                     'Manufactured, Modular, Prefabricated Homes', 'Townhouse']
    # filter for most-likely single unit properties
    df = df[df.propertylandusedesc.isin(single_prop_types)]
    df = df[(df.bedroomcnt > 0) & (df.bedroomcnt <= 10)]
    df = df[(df.bathroomcnt > 0) & (df.bathroomcnt <= 10)]
    # dropping columns with more than 25% missing values
    return df
    
def drop_cols_null(df, max_missing_rows_pct=0.25):
    '''
    Takes in a DataFrame and a maximum percent for missing values and
    returns the passed DataFrame after removing any colums missing the
    defined max percent or more worth of rows
    '''
    # set threshold for axis=1 and drop cols
    thresh_col = math.ceil(df.shape[0] * (1 - max_missing_rows_pct))
    df = df.dropna(axis=1, thresh=thresh_col)
    return df

def prep_work2(df):
    # make that a permanent part of the df
    df = drop_cols_null(df)
    #drop unneeded columns
    df =df.drop(columns= ['propertylandusetypeid', 'id', 
       'calculatedbathnbr','rawcensustractandblock',
       'latitude', 'longitude',
        'propertycountylandusecode','regionidcounty','finishedsquarefeet12',
       'regionidzip', 'yearbuilt','id','censustractandblock','last_trans_date',
       'transactiondate', 'id','roomcnt','fullbathcnt','assessmentyear'])
    # here I am dropping the duplicate parcelid column
    df = df.iloc[:,~df.columns.duplicated()]
    #rename columns we might keep for better understanding
    df = df.rename(columns={'bathroomcnt':'bathrooms','bedroomcnt': 'bedrooms','calculatedfinishedsquarefeet':
         'area','fips':'zipcode','lotsizesquarefeet': 'lot_area','taxvaluedollarcnt':'tax_value'})
    df = wrangle_functions.handle_missing_values(df)
    # replace nulls with median values for lot_area
    df.lot_area.fillna(7313, inplace = True)
    # drop columns with nulls for yearbuilt, taxvalue and taxamount
    df.dropna()
    # correcting dtype
    df.zipcode.astype(object)
    # I looked up the the average home size is 2,300 sqft so I will make that the cutoff 
    # between a large and small home
    # here I want to divide the homes and insert into a column those that are more than 2,300 sqft
    df['large_home'] =(df['area']> 2300).astype(int)
    #drop propertylanusetypeid, parcelid, propertylandusedesc, landtaxvaluedollarcnt,structuretaxvaluedollarcnt
    df.drop(columns = ['parcelid', 'propertylandusedesc', 'landtaxvaluedollarcnt', 'structuretaxvaluedollarcnt'])
    # Columns to look for extreme outliers, tax_value and area
    df = df[df.tax_value < 5_000_000]
    df = df[df.area < 8000]
    return df
    
    
def outlier_function(df, cols, k):
    cols = ['bathrooms', 'bedrooms',
       'area','lot_area','tax_value',
       'taxamount']
    #function to detect and handle oulier using IQR rule
    for col in df[cols]:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        upper_bound =  q3 + k * iqr
        lower_bound =  q1 - k * iqr
        df = df[(df[col] < upper_bound) & (df[col] > lower_bound)]
    return df
    
    

def train_validate_test(df, target):
    '''
    this function takes in a dataframe and splits it into 3 samples, 
    a test, which is 20% of the entire dataframe, 
    a validate, which is 24% of the entire dataframe,
    and a train, which is 56% of the entire dataframe. 
    It then splits each of the 3 samples into a dataframe with independent variables
    and a series with the dependent, or target variable. 
    The function returns train, validate, test sets and also another 3 dataframes and 3 series:
    X_train (df) & y_train (series), X_validate & y_validate, X_test & y_test. 
    '''
    target = 'logerror'
    # split df into test (20%) and train_validate (80%)
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)

    # split train_validate off into train (70% of 80% = 56%) and validate (30% of 80% = 24%)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)

        
    # split train into X (dataframe, drop target) & y (series, keep target only)
    X_train = train.drop(columns=[target])
    y_train = train[target]
    
    # split validate into X (dataframe, drop target) & y (series, keep target only)
    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]
    
    # split test into X (dataframe, drop target) & y (series, keep target only)
    X_test = test.drop(columns=[target])
    y_test = test[target]
    
    return train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test






# def scale_dataset(train, validate, test):
#     #applying the robust scaler
#     scaler = sklearn.preprocessing.RobustScaler()
#     # Note that we only call .fit with the training data,
#     # but we use .transform to apply the scaling to all the data splits.
#     scaler.fit(x_train)

#     x_train_scaled = scaler.transform(x_train)
#     x_validate_scaled = scaler.transform(x_validate)
#     x_test_scaled = scaler.transform(x_test)
#     return x_train_scaled, x_validate_scaled, x_test_scaled

# plt.figure(figsize=(13, 6))
# plt.subplot(121)
# plt.hist(x_train, bins=25, ec='black')
# plt.title('Original')
# plt.subplot(122)
# plt.hist(x_train_scaled, bins=25, ec='black')
# plt.title('Scaled')