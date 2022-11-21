# Phishing Classifier with ML

## Setup
Run the script bellow to prep the project and download the larger datasets

    $ python setup.py

## Order of execution
From top to bottom:
- enron-parser -> this Script process the "raw" legitimate email to a paletable version
- cleaning -> this script contain the step by step process of the data cleaning and preparation
- feature-exploration -> this script contains the step taken to extract the features from the cleaned and prepared datasets
- visualization -> this script visualize the datasets into several graph
- training -> this script compare several different estimator using different metric such as F1 score, accuracy, precise and recall.

## TODO
- Hyperparameter tuning
- visualization
