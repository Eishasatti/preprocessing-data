import pandas as pd
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv('second_dataset.csv')
print(df)

df_copy=df.copy()
le=LabelEncoder()
df_copy['job_encoder']=le.fit_transform(df_copy['Job_Role'])
df_encoded=pd.get_dummies(df_copy,columns=['Job_Role'])
print(df_encoded)







