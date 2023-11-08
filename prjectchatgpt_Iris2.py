import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
data = pd.read_csv('iris_dataset.csv')  # Replace with the actual file path

# Split the dataset into features (X) and target labels (y)
X = data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = data['Species']

# Scale the features using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the scaled data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train a logistic regression model
logistic_regression_model = LogisticRegression(max_iter=1000)
logistic_regression_model.fit(X_train, y_train)

# Test the model using a random value
random_value = np.array([[5.1, 3.5, 1.4, 0.2]])  # Replace with your feature values
random_value_scaled = scaler.transform(random_value)

predicted_class = logistic_regression_model.predict(random_value_scaled)

print(f"Predicted class for the random value: {predicted_class[0]}")

# If you want more details, you can print a classification report and confusion matrix
y_pred = logistic_regression_model.predict(X_test)
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
