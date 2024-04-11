# Multiple Linear Regression



### Objectives

* Use scikit-learn to implement Multiple Linear Regression
* Create a model, train it, test it and use the model



### Table of contents

1) Understanding the DATA

2) Reading the Data in

3) Multiple Regression Model

4) Prediction

5) Practice



### Importing Needed Packages

```
import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
```

### Reading DATA

```
df = pd.read_csv("FuelConsumption.csv")

# Take a look at the dataset
df.head()
```

#### Extract some interesting features for Multiple Linear Regression

```
cdf = df[['Columm_1', 'Columm_2', 'Columm_3','Columm_1']]
cdf.head(9)
```

####  Plot Y values (Emission Value in this case) with respect to Engine Size

```python
plt.scatter(cdf.ENGINE_SIZE, cdf.CO2EMISSIONS, color='blue')
plt.xlabel("Engine Size")
plt.ylabel("Emission")
plt.show()

```

### Creating train and test dataset

* Let's split our dataset into train and test sets. Around 80% of the entire dataset will be used for training and 20% for testing. We create a mask to select random rows using the np.random.rand()

  ```python
  msk = np.random.rand(len(df)) < 0.8
  train = cdf[msk]
  test = cdf[~msk]
  ```

  

### Multiple Regression Model

```python
from sklearn import linear_model
regr = linear_model.LinearRegression()
x = np.asanyarray(train[['ENGINE_SIZE', 'CYLINDERS', 'FUELCOMSUMPTION_COMB']])
y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit(x, y)
# The coefficients
print('Coefficients: ', regr.coef_)
```



### Prediction

```python
y_hat = regr.predict(test[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB']])
x = np.asanyarray(test[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB']])
y = np.asanyarray(test[['CO2EMISSIONS']])
print("Mean Squared Error (MSE) : %.2f" % np.mean((y_hat-y) ** 2))

# Explained variance Score : 1 is perfect prediction
print()
```



