# author: Fei Chang, Yanhua Chen
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
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
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
	X_train, y_train = train_df.drop(columns = ["target"]), train_df["target"]

	#Create the logistic regression model
	classifiers = {
   		"DummyClassifier": DummyClassifier(strategy='stratified'),
		"LogisticRegression": LogisticRegression(class_weight = "balanced", max_iter = 2000),
		"RandomForestClassifier": RandomForestClassifier(class_weight = "balanced"),
	}

	#Store results in dict
	results_df = {}

	#Score the models
	scoring=["accuracy", "f1"]
	for classifier_name, classifier in classifiers.items():
		scores = cross_validate(classifier, X_train, y_train, scoring = scoring, return_train_score=True, cv=10, n_jobs = -1)
		results_df[classifier_name] = pd.DataFrame(scores).mean()

	results_df = pd.DataFrame(results_df)

	#Fit the model with training data
	log_clf = LogisticRegression(class_weight = "balanced", max_iter = 2000)
	log_clf.fit(X_train, y_train)
	
	#Create feature importance table
	weights = log_clf.coef_.flatten()
	feat = train_df.columns.tolist()
	inds = np.argsort(log_clf.coef_.flatten())
	pos_words = [feat[index] for index in inds[-5:]]
	neg_words = [feat[index] for index in inds[:5]]
	pos_words_weights = [(weights[index]) for index in inds[-5:]]
	neg_words_weights = [(weights[index]) for index in inds[:5]]
	feat_imp_df = pd.DataFrame(
    	{
        	"positive feats": pos_words, "positive weights": pos_words_weights,
        	"negative feats": neg_words,"negative weights": neg_words_weights,
    	})


	#Save the results
	save_log = out_dir+'/logistic_model.joblib'


	try:
		dump(filename = save_log, value = log_clf)
		results_df.to_csv(out_dir+'/cross_validate_scores.csv')
		feat_imp_df.to_csv(out_dir+'/feature_importance.csv')
	except:
		os.remove(save_log)
		os.remove(save_rf)
		dump(filename = save_log, value = log_clf)
		results_df.to_csv(out_dir+'/cross_validate_scores.csv')
		feat_imp_df.to_csv(out_dir+'/feature_importance.csv')

	

if __name__ == "__main__":
	main(opt["--train"], opt["--out_dir"])
