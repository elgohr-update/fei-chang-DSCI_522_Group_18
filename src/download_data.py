# author: Group 18
# date: 2020-11-26

"""Downloads raw data from the web to a local filepath as a csv file format.
Usage: src/down_data.py --url=<url> --out_file=<out_file>

Options:
--url=<url>              URL from where to download the data (must be in standard csv format)
--out_file=<out_file>    Path (including filename) of where to locally write the file
"""
  
from docopt import docopt
import requests
import os
import pandas as pd

opt = docopt(__doc__)

def main(url, out_file):
    ## check url valildation
    request = requests.get(url)
    if request.status_code != 200:
        print("The provided url does not exist, please enter the correct url.")
        return
    
    ## read data
    data = pd.read_csv(url, header=None, sep=",")
    
    ## save data to out_file as .csv
    try:
        data.to_csv(out_file, index = False)
    ## if the directory doesn't exit, create one
    except:
        os.makedirs(os.path.dirname(out_file))
        data.to_csv(out_file, index = False)


if __name__ == "__main__":
    main(opt["--url"], opt["--out_file"])