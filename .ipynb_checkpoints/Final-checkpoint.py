# import libraries
import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

# read in dataset
camera = pd.read_csv("camera_dataset.csv")

# transform into  pandas dataframe
camera_df = pd.DataFrame(camera)

# check for null values and drop them as these only occur in 2 rows
camera_df.isnull().sum()
camera_new = camera_df.dropna(axis=0, how='any')

# print(camera_new.isnull().sum())
# print(camera_new.shape)
# print(camera_df.shape)
# print(camera_df.head())
print(camera_new.columns)
