# Makefile
# Fei Chang, Dec 2020


all : doc/income_census_report.md

# download raw data
data/raw/adult.csv : src/download_data.py 
	python src/download_data.py --url=https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data --out_file=data/raw/adult.csv

# pre-process data 
data/processed/training.csv data/processed/test.csv : data/raw/adult.csv src/preprocess.py 
	python src/preprocess.py --input=data/raw/adult.csv --out_dir=data/processed 

# create exploratory data analysis figure and write to file 
results/correlation_heatmap.png results/age.png results/work-hours.png: data/processed/training.csv src/eda_income_census.R
	Rscript src/eda_income_census.R --train=data/processed/training.csv --out_dir=results

# create eda report
src/eda.Rmd : data/raw/adult.csv results/correlation_heatmap.png results/age.png results/work-hours.png
	Rscript -e "rmarkdown::render('src/eda.Rmd')"

# fit data and tune model
results/randomforest_model.joblib results/logistic_model.joblib results/cross_validate_scores.csv : data/processed/training.csv src/predict_model.py
	python src/predict_model.py --train=data/processed/training.csv --out_dir=results

# test model
results/confusion_matrix.csv results/classification_report.csv : data/processed/test.csv results/logistic_model.joblib src/test_results.py
	python src/test_results.py --test=data/processed/test.csv --out_dir=results

# render final report
doc/income_census_report.md : doc/income_census_refs.bib results/cross_validate_scores.csv results/confusion_matrix.csv results/classification_report.csv results/age.png results/work-hours.png
	Rscript -e "rmarkdown::render('doc/income_census_report.Rmd', output_format = 'github_document')"


# clean everything up
clean :
	rm -rf data/raw/adult.csv
	rm -rf data/processed/training.csv
	rm -rf data/processed/test.csv
	rm -rf results/correlation_heatmap.png
	rm -rf results/age.png
	rm -rf results/work-hours.png 
	rm -rf src/eda.html
	rm -rf results/randomforest_model.joblib
	rm -rf results/logistic_model.joblib
	rm -rf results/cross_validate_scores.csv
	rm -rf results/confusion_matrix.csv
	rm -rf results/classification_report.csv
	rm -rf doc/income_census_report.html




