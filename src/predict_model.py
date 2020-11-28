# author: Fei Chang
# date: 2020-11-27

"""Fits a logistic regression classifier model on the pre-processed training data.
Saves the model as a joblib file.

Usage: src/predict_model.python --train=<train> --out_dir=<out_dir>

Options:
--train=<train>     Path (including filename) to training data (which needs to be saved as a csv file)
--out_dir=<out_dir> Path to directory where the serialized model should be written
"""

from docopt import docopt
import requests
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, cross_validate
from sklearn.linear_model import LogisticRegression
from joblib import dump, load

opt = docopt(__doc__)

def main(train, out_dir):
	try: 
		train_df = pd.read_csv(train)
	except FileNotFoundError:
		print("The input train data does not exist.\nPlease Check the raw data requested has been created.")
		return
	
	train_df = pd.read_csv(train)
	#Create X and y dataframe
	X_trian, y_train = 	train_df.drop(columns = ["target"]), train_df["target"]

	#Create the logistic regression model
	log_clf = LogisticRegression(class_weight = "balanced")

	scoring=["accuracy", "f1"]
	scores = cross_validate(log_clf, X_trian, y_train, scoring = scoring, return_train_score=True, cv = 5)
	scores_df = pd.DataFrame(scores)
	print("The mean validation accuracy score is %.3f" %scores["test_accuracy"].mean())
	print("The mean validation f1 score is %.3f" %scores["test_f1"].mean())
	
	try:
		dump(log_clf, out_dir+'/final_model.joblib')
		scores_df.to_csv(out_dir+"cross_validate_scores.csv")
	except:
		os.makedirs(out_dir)
		dump(log_clf, out_dir+'/final_model.joblib')
		scores_df.to_csv(out_dir+"cross_validate_scores.csv")

	

if __name__ == "__main__":
	main(opt["--train"], opt["--out_dir"])