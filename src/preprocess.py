# author: Fei Chang
# date: 2020-11-27

"""Cleans, splits and pre-processes (scales) the Census Income Dataset(from https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data).
Writes the training and test data to separate csv files.
Usage: src/preprocess.py --input_file=<input_file> --out_dir=<out_dir>

Options:
--input_file=<input_file>          Input raw data file in csv file.
--out_dir=<out_dir>                Path to directory where the processed data should be written
"""
  
from docopt import docopt
import requests
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import (
    train_test_split,
)
from sklearn.dummy import DummyClassifier
from sklearn.pipeline import FeatureUnion, Pipeline, make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import (
    OneHotEncoder,
    OrdinalEncoder,
    StandardScaler,
)
from sklearn.linear_model import LogisticRegression

opt = docopt(__doc__)

def main(input_file, out_dir):
  try: 
    raw_df = pd.read_csv(input_file)
  except FileNotFoundError:
    print("The input data file does not exist.\nPlease Check the raw data requested has been created.")
    return
  #Define colunm names
  col_names = ["age",
             "workclass",
             "fnlwgt",
             "education",
             "education_num",
             "marital_status",
             "occupation",
             "relationship",
             "race",
             "sex",
             "capital_gain",
             "capital_loss",
             "hours_per_week",
             "native_country",
             "income"]
  #Read raw data into dataframes
  raw_df = pd.read_csv(input_file)
  raw_df.columns = col_names
  
  #Split into test and train data
  train_df, test_df = train_test_split(raw_df, test_size=0.3, random_state=2020)

  #Basic cleaning by changing ? into nan values
  train_df_nan = train_df.replace("?", np.NaN)
  test_df_nan = test_df.replace("?", np.NaN)

  #Separate numeric features and categorical features
  numeric_features = [
    "age",
    "fnlwgt",
    "education_num",
    "capital_gain",
    "capital_loss",
    "hours_per_week",
  ]
  categorical_features = [
      "workclass",
      "marital_status",
      "occupation",
      "relationship",
      "race",
      "sex",
      "native_country",
  ]

  # Impute numeric missing values by the median
  imp = SimpleImputer(strategy="median")
  num_train = imp.fit_transform(train_df_nan[numeric_features])
  num_test = imp.transform(test_df_nan[numeric_features])

  # Impute categorical missing values by a constant string
  imp = SimpleImputer(strategy="constant", fill_value="missing")
  cat_train = imp.fit_transform(train_df_nan[categorical_features])
  cat_test = imp.transform(test_df_nan[categorical_features])

  # Scaling transformation for numeric features
  scaler = StandardScaler().fit(num_train)
  scaled_train = scaler.transform(num_train)
  scaled_test = scaler.transform(num_test)

  # One-hot transformation for categorical features
  ohe = OneHotEncoder(handle_unknown="ignore", sparse=False)
  ohe_train = ohe.fit_transform(cat_train)
  ohe_test = ohe.transform(cat_test)

  # Put the data after numeric and categorical transformations together
  processed_train = np.hstack((scaled_train, ohe_train))
  processed_test = np.hstack((scaled_test, ohe_test))

  # Define features created after transformation
  features = numeric_features
  features.extend(ohe.get_feature_names(categorical_features))

  # Convert processed train and test data with features into dataframe.
  processed_train_df = pd.DataFrame(
    data=processed_train,
    columns=features,
    index=train_df_nan.index,
    )

  processed_test_df = pd.DataFrame(
      data=processed_test,
      columns=features,
      index=test_df_nan.index,
    )

  #Define and add the target of prediction to the train and test data.
  processed_train_df["target"] =  train_df["income"].replace({' >50K': 1, ' <=50K': 0})
  processed_test_df["target"] =  test_df["income"].replace({' >50K': 1, ' <=50K': 0})

  training_file = out_dir+"/training.csv"
  test_file = out_dir+"/test.csv"
  try:
    processed_train_df.to_csv(training_file, index = False)
    processed_test_df.to_csv(test_file, index = False)
  except:
    os.makedirs(out_dir)
    processed_train_df.to_csv(training_file, index = False)
    processed_test_df.to_csv(test_file, index = False)


if __name__ == "__main__":
  main(opt["--input_file"], opt["--out_dir"])