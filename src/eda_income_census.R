
"Creates eda plots for the pre-processed training data from the Income census data
Saves the plots as a pdf and png file.
Usage: src/eda_income_census.r --train=<train> --out_dir=<out_dir>
  
Options:
--train=<train>     Path (including filename) to training data (which needs to be saved as a csv file)
--out_dir=<out_dir> Path to directory where the plots should be saved
" -> doc

library(feather)
library(tidyverse)
library(docopt)
theme_set(theme_minimal())

opt <- docopt(doc)

main <- function(train, out_dir) {
  
  # visualize age distribution for income levels
  plot1 <- boxplot (age ~ income, data = train, 
           main = "Age distribution for different income levels",
           xlab = "Income Levels", ylab = "Age", col = "salmon")
  ggsave(paste0(out_dir, "/age_and_income.png"), 
         plot1,
         width = 8, 
         height = 10)
  
  plot2 <- boxplot (`hours.per.week` ~ income, data = census_data, 
                    main = "Work Hours distribution for different income levels",
                    xlab = "Income Levels", ylab = "Age", col = "salmon")
  ggsave(paste0(out_dir, "/work-hours_and_income.png"), 
         plot2,
         width = 8, 
         height = 10)
}

main(opt[["--train"]], opt[["--out_dir"]])