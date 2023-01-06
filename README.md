# Phishing Classifier with ML

This is an attempt to create an AI model that can classify whether an email is a phishing attempt or not, by comparing different model estimator to find which one perform better then the rest. model perfomance is measured through evaluation metric such as accuracy, precision, recall, and F1 Score

## Setup
Run the script bellow to prep the project and download the larger datasets

    $ python setup.py

## Order of execution
Before running the script listed bellow, run the setup script at least once.

From top to bottom:
- enron-parser -> this Script process the "raw" legitimate email to a paletable version
- cleaning -> this script contain the step by step process of the data cleaning and preparation
- feature-exploration -> this script contains the step taken to extract the features from the cleaned and prepared datasets
- visualization -> this script visualize the datasets into several graph
- training -> this script compare several different estimator using different metric such as F1 score, accuracy, precise and recall.

## Reference
- https://github.com/diegoocampoh/MachineLearningPhishing