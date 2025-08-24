import pandas as pd
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv('dataset.csv')
print(df)
print("--------------Encoded Data------------------")
df_copy=df.copy()
le=LabelEncoder()
df_copy['Purchased_Encoder']=le.fit_transform(df_copy['Purchased'])
print(df_copy)








