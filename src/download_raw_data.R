## author: Group18
## date: 2020-11-21

##This script is to download the raw dataset for the project

## This script has no options, the dataset will automatically save in the `src` folder

##Usage: Rscript download_raw_data.R 

main <- function(){
  file_path<-getwd()
  url<-paste0("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data")
  destfile<-paste0(file_path,"/src/adult.csv")
  download.file(url,destfile,method="auto",quiet = FALSE, mode="w",cacheOK=TRUE)
}

main()


