from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Load data
df = pd.read_csv('second_dataset.csv')

X = df[['Salary']]            # Feature
y = df['Job_Role']            # Target (string labels)

# Encode job roles into numbers
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.3, random_state=42
)

# Train a classifier
model = LogisticRegression()
model.fit(X_train, y_train)

# Take input
val = float(input("Please enter your salary in thousands: "))
res = model.predict([[val]])[0]

# Convert prediction back to original string label
job_role = encoder.inverse_transform([res])[0]

print(f"Your job role is {job_role} with the salary of {val}")
