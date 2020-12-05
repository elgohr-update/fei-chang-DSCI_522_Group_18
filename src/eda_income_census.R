
"Creates eda plots for the pre-processed training data from the Income census data
Saves the plots as a pdf and png file.
Usage: src/eda_income_census.r --train=<train> --out_dir=<out_dir>
  
Options:
--train=<train>     Path (including filename) to training data (which needs to be saved as a csv file)
--out_dir=<out_dir> Path to directory where the plots should be saved
" -> doc

library(tidyverse)
library(docopt)
library(knitr)
library(ggplot2)
library(cowplot)
library(reshape2)
theme_set(theme_minimal())

opt <- docopt(doc)

main <- function(train, out_dir) {
  x_train <- read_csv(train)
  x_train$target = as.factor(x_train$target)
  
  # visualize correlation heatmap between numerical features
  numeric_features <- c( "age",
                         "fnlwgt",
                         "education_num",
                         "capital_gain",
                         "capital_loss",
                         "hours_per_week")
  numeric_features 
  numeric_data <- x_train[, numeric_features]
  cormat <- round(cor(numeric_data),2)
  melted_cormat <- melt(cormat)
  
  plot0<- ggplot(data = melted_cormat, aes(x=Var1, y=Var2, fill=value)) +
    geom_tile() +
    ggtitle("Correlation Heatmap for Numeric Features ") +
    xlab("Numeric Features") +
    ylab("Numeric Features")

  ggsave(file = paste0(out_dir, "/correlation_heatmap.png"),
         plot = plot0,
         width = 5,
         height = 5)
  
  # visualize age distribution for income levels
  plot1 <- ggplot(x_train, aes(x = target, y = age)) +
    geom_boxplot() +
    ggtitle("Age distribution for different income levels") +
    xlab("Income Levels") +
    ylab("Age")
  
  ggsave(file = paste0(out_dir, "/age.png"),
         plot = plot1,
         width = 5,
         height = 5)

  plot2 <- ggplot(x_train, aes(x = target, y = hours_per_week)) +
    geom_boxplot() +
    ggtitle("Work Hours distribution for different income levels") +
    xlab("Income Levels") +
    ylab("Work Hours per week")

  ggsave(file = paste0(out_dir, "/work-hours.png"),
         plot = plot2,
         width = 5,
         height = 5)
  
}

main(opt[["--train"]], opt[["--out_dir"]])