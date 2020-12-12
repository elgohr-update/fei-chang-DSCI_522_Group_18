Predicting Income levels of an individual
================
Aishwarya Gopal, Fei Chang, Yanhua Chen
2020/11/29

  - [Summary](#summary)
  - [Introduction](#introduction)
  - [Methods](#methods)
      - [Data](#data)
      - [Analysis](#analysis)
  - [Results & Discussion](#results-discussion)
      - [Explanatory Data Analysis](#explanatory-data-analysis)
      - [Model Selection](#model-selection)
      - [Feature Importance](#feature-importance)
      - [Results](#results)
      - [Further Discussion](#further-discussion)
  - [References](#references)

# Summary

Here we attempt to build a classification model using the Logistic
Regression algorithm which uses a set of features like age, workclass,
education etc to classify the income levels of an indivdual into one of
the two categories: \>$50k/year or \<=$50k/year. The target class \>=50k
was encoded as 1 and the other class as 0. Our final Logistic Regression
model performed well on the test data set. We obtained an f1 score of
0.69 and an overall accuracy calculated to be 0.81. It correctly
predicted the income class of 7932 individuals. However it incorrectly
predicted 1837 examples.

# Introduction

“A large income is the best recipe for happiness I ever heard of” quotes
the famous English novelist Jane Austen. While it might not be the only
recipe, income dictates the standard of living and economic status of an
individual. So, we decided to study the income distribution of people
with different education levels, years of experience etc. The
observations in this data set are classified according to income levels,
into two categories(\>$50k/year or \<=$50k/year). This data set
comprises of numbers from many countries around the world but, about 90%
of the data has been collected from the USA. So, we are under the
assumption that, the median wage required to lead a life in the USA (at
the time this data was collected) i.e. $50k per year, was chosen as a
threshold for classification.

Taking into account, the importance and impact of income levels in
determining a nation’s growth, this study aims to present meaningful
insights regarding the same.

# Methods

## Data

The data set used in this project is of income census created by Ronny
Kohavi and Barry Becker. It was sourced from the UCI Machine Learning
Repository and can be found
[here](https://archive.ics.uci.edu/ml/machine-learning-databases/adult/),
specifically [this
file](https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data).
The data contains information such as age, workclass, education etc. The
target variable is income and it is divided into two categories (\<=50K
and \>50K). The ultimate aim is to train a classifier to predict the
income class.

## Analysis

The logistic regression algorithm was used to build a classification
model to predict whether an individual earns \>$50k/year or
\<=$50k/year. All the variables in original data set except for
education column was used. The education.num column is just a numerical
representation of the education level of an individual. f1 score was
chosen as the desired metric and a 10 fold cross-validation was
performed on the train set. The R and Python programming languages (R
Core Team 2019; Van Rossum and Drake 2009) and the following R and
Python packages were used to perform the analysis: docopt (de Jonge
2018), knitr (Xie 2014), tidyverse (Wickham et al. 2019), docopt
(Keleshev 2014), os (Van Rossum and Drake 2009), Pandas (McKinney 2010).
The code used to perform the analysis and create this report can be
found here: <https://github.com/UBC-MDS/DSCI_522_Group_18>.

# Results & Discussion

### Explanatory Data Analysis

To look at the realationship between some of the predictors and the
income class, we plotted the graphs of a few predictors according to the
class distribution.

<div class="figure">

<img src="../results/box_plots_numeric.png" alt="Figure 1. Boxplots of numeric variables categorized by target variable" width="100%" />

<p class="caption">

Figure 1. Boxplots of numeric variables categorized by target variable

</p>

</div>

The box plots of all scaled numeric features categorized by the target
variable is presented above. The target 0 is \<50k and the target 1 is
\>=50k.

From the above plot, it can be inferred that, in general as age
increases, i.e. experience level increases, there tends to be higher
income levels.

Individuals with income \>50k have longer average working hours per week
than individuals with \<50k. But there are some individuals who have
income \<50k, but have higher work hours.

Another important inference is that people with higher education levels
earn more on an average than people with lower education levels.

Other numerical variables such as capital\_loss and capital\_gain tend
to have very low median values but have a significantly high number of
outliers.

The next area of concern is collinearity. When two numeric input
variables are highly correlated, it is almost impossible to change the
value of one input variable without changing the other. Hence, the
coefficients become very sensitive to small changes in the model and the
coefficient estimates tend to swing wildly. To address this, we plotted
a correlation heatmap.

From the below correlation heatmap, we can observe that none of the
numeric variables seem to be highly correlated. Hence, we decided to
retain all the features except education (education and education.num
present the same information) for training the model.

<img src="../results/correlation_heatmap.png" width="1200" />

### Model Selection

We chose to build a simple classification model. To find the model that
best predicted whether an individual earns \>50k or \<=50k, we performed
10-fold cross validation using the Logistic regression algorithm and
Random Forest Classification. We observed that the Random Forest
Classification generates a higher training accuracy and f1 score,
however, its advantage in cross-validation scores is not obvious.
Meanwhile, the gap between train and cross-validation score is very
large in Random Forest Classification, which indicates the model is
overfitted. At this point, we decide to use Logistic Regression
algorithm to build the prediction model.

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">

<caption>

Table 1. Cross validate scores of model performance on train data.

</caption>

<thead>

<tr>

<th style="text-align:left;">

X

</th>

<th style="text-align:right;">

DummyClassifier

</th>

<th style="text-align:right;">

LogisticRegression

</th>

<th style="text-align:right;">

RandomForestClassifier

</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:left;">

fit\_time

</td>

<td style="text-align:right;">

0.025

</td>

<td style="text-align:right;">

2.944

</td>

<td style="text-align:right;">

7.354

</td>

</tr>

<tr>

<td style="text-align:left;">

score\_time

</td>

<td style="text-align:right;">

0.004

</td>

<td style="text-align:right;">

0.009

</td>

<td style="text-align:right;">

0.136

</td>

</tr>

<tr>

<td style="text-align:left;">

test\_accuracy

</td>

<td style="text-align:right;">

0.634

</td>

<td style="text-align:right;">

0.810

</td>

<td style="text-align:right;">

0.856

</td>

</tr>

<tr>

<td style="text-align:left;">

train\_accuracy

</td>

<td style="text-align:right;">

0.634

</td>

<td style="text-align:right;">

0.811

</td>

<td style="text-align:right;">

1.000

</td>

</tr>

<tr>

<td style="text-align:left;">

test\_f1

</td>

<td style="text-align:right;">

0.241

</td>

<td style="text-align:right;">

0.682

</td>

<td style="text-align:right;">

0.670

</td>

</tr>

<tr>

<td style="text-align:left;">

train\_f1

</td>

<td style="text-align:right;">

0.237

</td>

<td style="text-align:right;">

0.684

</td>

<td style="text-align:right;">

1.000

</td>

</tr>

</tbody>

</table>

### Feature Importance

Looking through the feature importance of our model, we found some
interesting information:

It seems that married people usually have higher probability to gain
more than 50k per year, especially for females (relationship\_Wife),
while people who are never married have higher probability to gain less
than 50k.

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">

<caption>

Table 2. feature importance of final model

</caption>

<thead>

<tr>

<th style="text-align:left;">

positive.feats

</th>

<th style="text-align:right;">

positive.weights

</th>

<th style="text-align:left;">

negative.feats

</th>

<th style="text-align:right;">

negative.weights

</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:left;">

native\_country\_ Japan

</td>

<td style="text-align:right;">

0.984

</td>

<td style="text-align:left;">

occupation\_ Priv-house-serv

</td>

<td style="text-align:right;">

\-1.801

</td>

</tr>

<tr>

<td style="text-align:left;">

relationship\_ Wife

</td>

<td style="text-align:right;">

1.322

</td>

<td style="text-align:left;">

native\_country\_ Peru

</td>

<td style="text-align:right;">

\-1.147

</td>

</tr>

<tr>

<td style="text-align:left;">

marital\_status\_ Married-civ-spouse

</td>

<td style="text-align:right;">

1.524

</td>

<td style="text-align:left;">

marital\_status\_ Never-married

</td>

<td style="text-align:right;">

\-1.078

</td>

</tr>

<tr>

<td style="text-align:left;">

marital\_status\_ Married-AF-spouse

</td>

<td style="text-align:right;">

1.668

</td>

<td style="text-align:left;">

native\_country\_ Dominican-Republic

</td>

<td style="text-align:right;">

\-1.037

</td>

</tr>

<tr>

<td style="text-align:left;">

capital\_gain

</td>

<td style="text-align:right;">

2.242

</td>

<td style="text-align:left;">

workclass\_ Without-pay

</td>

<td style="text-align:right;">

\-0.970

</td>

</tr>

</tbody>

</table>

### Results

Our prediction model performed quite well on test data, the confusion
matrix below indicates it only made 1837 mistakes, so the test accuracy
is 0.812. It predicted 364 examples as belonging to “\>=50K” group while
they actually belong to the “\<50K” group. These are termed as False
Positives(FP). The model predicted 1473 as “\<50K” group while the
actual prediction is “\>=50K”. These are termed as False Negatives(FN).
The examples correctly predicted as belonging to “\<50K” group are
termed as True Negatives(TN) and the examples correctly predicted as
belonging to “\>=50K” group are termed as True Positives(TP). However,
most of the mistake are from the “\>=50K” group.

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">

<caption>

Table 3. Confusion matrix of model performance on test data.

</caption>

<thead>

<tr>

<th style="empty-cells: hide;border-bottom:hidden;" colspan="1">

</th>

<th style="border-bottom:hidden;padding-bottom:0; padding-left:3px;padding-right:3px;text-align: center; " colspan="2">

<div style="border-bottom: 1px solid #ddd; padding-bottom: 5px; ">

Reference

</div>

</th>

</tr>

<tr>

<th style="text-align:left;">

</th>

<th style="text-align:right;">

\<50k

</th>

<th style="text-align:right;">

\>=50k

</th>

</tr>

</thead>

<tbody>

<tr grouplength="2">

<td colspan="3" style="border-bottom: 1px solid;">

<strong>Predicted</strong>

</td>

</tr>

<tr>

<td style="text-align:left; padding-left:  2em;" indentlevel="1">

\<50k

</td>

<td style="text-align:right;">

5929

</td>

<td style="text-align:right;">

1473

</td>

</tr>

<tr>

<td style="text-align:left; padding-left:  2em;" indentlevel="1">

\>=50k

</td>

<td style="text-align:right;">

364

</td>

<td style="text-align:right;">

2003

</td>

</tr>

</tbody>

</table>

This problem is also reflected by the classification report, that the
f1.score of “\>=50k” group is much lower than “\<50k” group. Precision
is calculated as TP/(TP+FP) while Recall is calculated as (TP/TP+FN). f1
score is the harmonic mean of Precision and Recall. This model is not
good enough to yet predict the income status of rich people.

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">

<caption>

Table 4. Classification report of model performance on test data.

</caption>

<thead>

<tr>

<th style="text-align:left;">

X

</th>

<th style="text-align:right;">

precision

</th>

<th style="text-align:right;">

recall

</th>

<th style="text-align:right;">

f1.score

</th>

<th style="text-align:right;">

support

</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:left;">

\<50k

</td>

<td style="text-align:right;">

0.942

</td>

<td style="text-align:right;">

0.801

</td>

<td style="text-align:right;">

0.866

</td>

<td style="text-align:right;">

7402

</td>

</tr>

<tr>

<td style="text-align:left;">

\>=50k

</td>

<td style="text-align:right;">

0.576

</td>

<td style="text-align:right;">

0.846

</td>

<td style="text-align:right;">

0.686

</td>

<td style="text-align:right;">

2367

</td>

</tr>

<tr>

<td style="text-align:left;">

macro avg

</td>

<td style="text-align:right;">

0.759

</td>

<td style="text-align:right;">

0.824

</td>

<td style="text-align:right;">

0.776

</td>

<td style="text-align:right;">

9769

</td>

</tr>

<tr>

<td style="text-align:left;">

weighted avg

</td>

<td style="text-align:right;">

0.853

</td>

<td style="text-align:right;">

0.812

</td>

<td style="text-align:right;">

0.822

</td>

<td style="text-align:right;">

9769

</td>

</tr>

</tbody>

</table>

### Further Discussion

To further improve this model in future, we have attempted tune
hyperparameters and also applied feature selection on it. However, both
approaches didn’t help to improve the model improvements. There are
several things we can suggest which beyond our capability . First,
exploring some method about feature engineering which might be helpful
to improve the model performance. Second, because the misclassification
is concentrated in \>50k group, having more data from that group will
improve the prediction accuracy.

# References

<div id="refs" class="references hanging-indent">

<div id="ref-docopt">

de Jonge, Edwin. 2018. *Docopt: Command-Line Interface Specification
Language*. <https://CRAN.R-project.org/package=docopt>.

</div>

<div id="ref-docoptpython">

Keleshev, Vladimir. 2014. *Docopt: Command-Line Interface Description
Language*. <https://github.com/docopt/docopt>.

</div>

<div id="ref-mckinney-proc-scipy-2010">

McKinney. 2010. “Data Structures for Statistical Computing in Python.”
In *Proceedings of the 9th Python in Science Conference*, edited by
Stéfan van der Walt and Jarrod Millman, 56–61.
[https://doi.org/ 10.25080/Majora-92bf1922-00a](https://doi.org/%2010.25080/Majora-92bf1922-00a%20).

</div>

<div id="ref-R">

R Core Team. 2019. *R: A Language and Environment for Statistical
Computing*. Vienna, Austria: R Foundation for Statistical Computing.
<https://www.R-project.org/>.

</div>

<div id="ref-Python">

Van Rossum, Guido, and Fred L. Drake. 2009. *Python 3 Reference Manual*.
Scotts Valley, CA: CreateSpace.

</div>

<div id="ref-tidyverse">

Wickham, Hadley, Mara Averick, Jennifer Bryan, Winston Chang, Lucy
D’Agostino McGowan, Romain François, Garrett Grolemund, et al. 2019.
“Welcome to the tidyverse.” *Journal of Open Source Software* 4 (43):
1686. <https://doi.org/10.21105/joss.01686>.

</div>

<div id="ref-knitr">

Xie, Yihui. 2014. “Knitr: A Comprehensive Tool for Reproducible Research
in R.” In *Implementing Reproducible Computational Research*, edited by
Victoria Stodden, Friedrich Leisch, and Roger D. Peng. Chapman;
Hall/CRC. <http://www.crcpress.com/product/isbn/9781466561595>.

</div>

</div>
