# Income Status Predictor
Co-authors: Aishwarya Gopal, Fei Chang, Yanhua Chen

## About

Here we attempt to build a classification model using the Logistic Regression algorithm which uses a set of features like age, workclass, education etc to classify the income levels of an indivduals into one of the two categories: \>\$50k/year or \<=\$50k/year.

The Census Income Dataset is created by Ronny Kohavi and Barry Becker, and sourced from the UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. This is a classification dataset and we will complete a classification task to predict whether or not a person can earn more than $50k/yr for this project. We will use the binary attribute "income" as our target, which includes two values: ">50K" and "<=50K". There are 14 explanatory variables in the dataset, 6 are numeric features and 8 are categorical features. Each row contains one observation with the 14 explanatory variables(personal information) and the relative income status. There are 48842 observations in the dataset.

## Report

The final report can be found [here](##add link)

## Usage

To replicate the anlaysis, please clone this Github repository, install the dependencies listed below, and run the following commands in terminal from the root directory of the project

```
# download raw data
python src/download_data.py --url=https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data --out_file=data/raw/adult.csv

# run eda report
Rscript -e "rmarkdown::render('src/eda.Rmd')"

# pre-process data 
Python src/preprocess.py --input=data/raw/adult.csv --out_dir=data/processed 

# create exploratory data analysis figure and write to file 
Rscript src/eda_income_census.R --train=data/processed/training.csv --out_dir=results

# tune model
Python src/predict_model.py --train=data/processed/training.csv --out_dir=results

# test model
Python src/test_results.py --test=data/processed/test.csv --out_dir=results

# render final report
Rscript -e "rmarkdown::render('doc/income_census_report.Rmd', output_format = 'github_document')"
```

## Dependencies

x

## Citation
Ron Kohavi, "Scaling Up the Accuracy of Naive-Bayes Classifiers: a Decision-Tree Hybrid", Proceedings of the Second International Conference on Knowledge Discovery and Data Mining, 1996

Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.
