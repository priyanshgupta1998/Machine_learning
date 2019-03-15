# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values




# Encoding categorical data
#Encoding the indepedent variable (coulmn thata contains text/string data)
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()    #make a object
X[:, 3] = labelencoder.fit_transform(X[:, 3])   #fit in the dataset
onehotencoder = OneHotEncoder(categorical_features = [3])  #then encode the data
X = onehotencoder.fit_transform(X).toarray()  #devide into array


# Avoiding the Dummy Variable Trap 
X = X[:, 1:]    #remove the one dummy variable (anyone)


# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
#here we are taking 20% observation for testing purpose and 80% observations for training 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)



# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""



# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()  #create a object regressor (by calling the class LinearRegression()) 
#Now Do fit the multiple lenear regression to the training set
regressor.fit(X_train, y_train)  #aplying the fit method 


# Predicting the Test set results
y_pred = regressor.predict(X_test)  


#building the optimal model using Backward Elimination
#For this purpose we need to import one api
import statsmodels.formula.api as sm
#Now Add/create a first column of constant 'b0' according to formula 'y=b0 + b1*x1 + b2*x2 ......+bn*xn'
X=np.append(arr=np.ones((50,1)).astype(int),values=X,axis=1) #convert datatype into integer
#axis =1 is used for column
#Now step 1 is done 
#Now we are goiing to fit the model with all possoble predictors
X_opt = X[:,[0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog=X_opt).fit()
print(regressor_OLS.summary())
#Now step 2 is done.  Now here we can see the maximum value of 'p' is 99% in
# variable x2 ,So we have removeit  ,bcoz it is greater than SL. 
#step-3 is done . Now step-4 remove the predictor  'x2' and fit the model
X_opt = X[:,[0,1,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog=X_opt).fit()
print(regressor_OLS.summary())
#step-4 is done ,but again we have maximum p which is > S.L.
#remove that predictor where (P>SL)
X_opt = X[:,[0,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog=X_opt).fit()
print(regressor_OLS.summary())
#step-4 is done ,but again we have maximum p which is > S.L.
#remove that predictor where (P>SL)
X_opt = X[:,[0,3,5]]
regressor_OLS = sm.OLS(endog = y, exog=X_opt).fit()
print(regressor_OLS.summary())
#step-4 is done ,AND now our model is ready. but there is one predictor(no.5)
# we can observer which is slightly greater than 'SL'
#so ,we have to remove it.
X_opt = X[:,[0,3]]
regressor_OLS = sm.OLS(endog = y, exog=X_opt).fit()
print(regressor_OLS.summary())
#NOW ,we are getting powerfull model.


















