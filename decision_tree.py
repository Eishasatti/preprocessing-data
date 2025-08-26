from sklearn.tree import DecisionTreeClassifier
import pandas as pd

df=pd.read_csv('next_dataset.csv')
X=df[['Weight', 'Texture']]
y=df['Fruit']
dtree=DecisionTreeClassifier()
dtree.fit(X,y)

wei=float(input("Enter weight in grams  "))
texture=float(input("Enter texture of surface 0 for smooth and 1 for rough  "))
pred=dtree.predict([[wei,texture]])[0]
print(f'Fruit is {pred} based on weight {wei} and texture {texture}');