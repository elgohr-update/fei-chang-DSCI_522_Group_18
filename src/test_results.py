# author: Fei Chang, Yanhua Chen
# date: 2020-11-28

"""Assesses model's accuracy on a test data set.

Usage: src/test_results.python --test=<test> --out_dir=<out_dir>

Options:
--test=<test>     Path (including filename) to test data (which needs to be saved as a csv file)
--out_dir=<out_dir> Path to directory where the serialized model should be written
"""
from docopt import docopt
import requests
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, cross_validate
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score)
from joblib import dump, load

opt = docopt(__doc__)

def main(test, out_dir):
        try: 
	        test_df = pd.read_csv(test)
        except FileNotFoundError:
                print("The input test data does not exist.\nPlease Check the raw data requested has been created.")
                return

	#Load and wrangle test data
        test_df = pd.read_csv(test)
        X_test, y_test = test_df.drop(columns = ["target"]), test_df["target"]

	#Load model and predict
        model = load(filename='results/logistic_model.joblib') 
        pred = model.predict(X_test)

        #Create confusion matrix
        cm = pd.DataFrame(confusion_matrix(y_test, pred))
        
        #Create classification report
        cr = pd.DataFrame(classification_report(y_test, pred, output_dict=True)).transpose()

        #Save results
        try:
                cm.to_csv(out_dir+'/confusion_matrix.csv')
                cr.to_csv(out_dir+'/classification_report.csv')
        except:
                os.makedirs(out_dir)
                cm.to_csv(out_dir+'/confusion_matrix.csv')
                cr.to_csv(out_dir+'/classification_report.csv')


if __name__ == "__main__":
	main(opt["--test"], opt["--out_dir"])
