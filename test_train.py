from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import numpy as np
import pandas as pd

df=pd.read_csv('second_dataset.csv');
X=df[['Salary']]
y=df['Job_Role']
# X_train,X_test,y_train,y_test=train_test_split(X, y, test_size=0.3,random_state=42);
# print('Training');

# print(X_train)
# print('y training')
# print(y_train)
#in this way 70 percent of data is used for training and 30 percent for testing now I will use .fit annd . predict function to ask this model to make predictions
model=LinearRegression()
model.fit(X,y)

val=float(input("Please enter your salary in thousands"))
res= model.predict([val])[0]
print(f"Your job role is {res} with the salry of {val}")

#using linear regression model