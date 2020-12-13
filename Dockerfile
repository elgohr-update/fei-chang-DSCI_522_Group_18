# Docker file for the income status predictor project
# Yanhua Chen, Dec, 2020

# use rocker/tidyverse as the base imag
FROM rocker/tidyverse

USER root

RUN apt-get update --fix-missing 

# install R packages
RUN apt-get update -qq && install2.r --error \
    --deps TRUE \
    knitr \
    tidyverse \
    ggplot2 \
    reshape2 \
    docopt 
RUN Rscript -e "install.packages('kableExtra')"

# install python3
RUN apt-get install -y \
		python3-pip \
		python3-dev
    
# install anaconda & put it in the PATH
RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy && \
    /opt/conda/bin/conda update -n base -c defaults conda

# put anaconda python in path
ENV PATH="/opt/conda/bin:${PATH}"

# Updating Anaconda packages
RUN conda update -y -n base -c defaults conda

# install python packages
RUN conda install -y -c anaconda docopt \
    requests \
    pandas \
    numpy \
    scikit-learn \
    joblib
    
RUN conda update -y --all
    
