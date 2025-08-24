import pandas as pd 
import numpy as np
data={
    'Name':['Alice','Bob','Charlie','David','Eva'],
    'Age':[25,None,35,40,None],
    'City':['New York',np.nan,'Chicago','Houston','Miami']
}
df=pd.DataFrame(data)
print(df)
# print(df.isnull().mean()*100)
print("printing only complete data rows")
# df_drop=df.dropna()
# print(df_drop)
df['Age'].fillna(df['Age'].mean(), inplace=True)
print(df)
df['City'].fillna('Pampano Beach', inplace=True)
print(df)







