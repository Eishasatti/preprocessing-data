import pandas as pd
from sklearn.linear_model import LinearRegression
X=[[1], [2], [3], [4], [5]]
y=[40, 50 ,60, 75, 85]
model=LinearRegression()

model.fit(X,y)

val=float(input("Please enter your study hrs"))
res= model.predict([[val]])[0]
print(f"Your expected marks are {res} with the study hours of  {val}")
