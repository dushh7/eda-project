import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/dataset.csv")

# Show first rows
print(df.head())

# Basic info
print(df.info())

# Missing values
print(df.isnull().sum())

# Drop duplicates
df = df.drop_duplicates()

# Summary stats
print(df.describe())