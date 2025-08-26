from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

df=pd.read_csv('next_dataset.csv')
X=df[['Weight', 'Texture']]
y=df['Fruit']

Knn=KNeighborsClassifier(n_neighbors=5)
Knn.fit(X,y)

wei=float(input("Enter weight in grams  "))
texture=float(input("Enter texture of surface 0 for smoth and 1 for rough  "))
pred=Knn.predict([[wei,texture]])[0]
print(f'Fruit is {pred} based on weight {wei} and texture {texture}');



 