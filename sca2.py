
from sklearn.preprocessing import StandardScaler , MinMaxScaler
import pandas as pd

scaler=MinMaxScaler()
df=pd.read_csv('second_dataset.csv')


# method for slecting all numeric column
# numeric_cols = df.select_dtypes(include=['int64','float64']).columns
# scaled_df = pd.DataFrame(scaler.fit_transform(df[numeric_cols]), columns=numeric_cols)
# print(scaled_df)

#only selecting those coulums having numeric value
standard_sca=scaler.fit_transform(df[['Age','Salary']])

print(pd.DataFrame(standard_sca,columns=['Age','Salary']))


