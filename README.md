# Income Status Predictor
Co-authors: Aishwarya Gopal, Fei Chang, Yanhua Chen

## About

Here we ...

The Census Income Dataset is created by Ronny Kohavi and Barry Becker, and sourced from the UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. This is a classification dataset and we will complete a classification task to predict whether or not a person can earn more than $50k/yr for this project. We will use the binary attribute "income" as our target, which includes two values: ">50K" and "<=50K". There are 14 explanatory variables in the dataset, 6 are numeric features and 8 are categorical features. Each row contains one observation with the 14 explanatory variables(personal information) and the relative income status. There are 48842 observations in the dataset.

## Report

The final report can be found [here](##add link)

## Usage

To replicate the anlaysis, please clone this Github repository, install the dependencies listed below, and run the following commands in terminal from the root directory of the project

```
# download raw data
python src/download_data.py --url=https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data --out_file=data/raw/adult.csv
```

## Dependencies

x

## Citation
Ron Kohavi, "Scaling Up the Accuracy of Naive-Bayes Classifiers: a Decision-Tree Hybrid", Proceedings of the Second International Conference on Knowledge Discovery and Data Mining, 1996

Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.
