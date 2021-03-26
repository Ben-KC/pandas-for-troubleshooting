# Using Pandas for Troubleshooting

## Background

Most Pandas demonstrations I've seen focus on using it for traditional data analysis tasks. In my work 
in industrial automation, I often use Pandas, but not necessarily in the traditional way. We have a number 
of systems that generate data in the form of logfiles. These logfiles are often either massive or exist in 
such large quantities that it can be difficult to go through them looking for trends or trying to identify 
issues. In this repo, I hope to create example Jupyter notebooks which emulate the ones I use at work in 
order to demonstrate how to use Python data tools for troubleshooting.  
  
Apologies in advance if things come across as fairly vague, I'm trying to emulate my work 
notebooks as closely as possible without disclosing information that might be considered sensitive.

## Usage

To use this repo, clone it to your local machine (you'll need at least Python 3.8). Run 
`pip install -r requirements.txt` from the base directory to install all the requirements, then run 
`jupyter lab` to open up a JupyterLab environment where you can interact with the notebooks.

## Current Notebooks
* [analysis.ipynb](analysis.ipynb): Troubleshooting a machine running a black-box model whose calculation time has spiked
