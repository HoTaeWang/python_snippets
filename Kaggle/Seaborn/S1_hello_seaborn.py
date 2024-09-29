# -*- coding: utf-8 -*-
"""hello_seaborn.ipynb
"""

# Setup the Notebook
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# %matplotlib inline

import seaborn as sns
print('Setup Complete')

# Load data
fifa_filepath = "./fifa.csv"
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)

# Examine data
print(fifa_data.head())
#print(fifa_data.describe())


# plot the data
# setup the width and height of the figure
plt.figure(figsize=(16, 6))

# Line chart showing how FIFA rankings evolved over time
sns.lineplot(data= fifa_data)

# Save the plot
plt.savefig('FifaRanking.png')

