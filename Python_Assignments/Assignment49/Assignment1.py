# ----------------------------------------------------------
# Marvellous Infosystems : Machine Learning Assignment
# Diabetes Prediction using Multiple Models
# ----------------------------------------------------------

import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# ----------------------------------------------------------
# Function : Perform EDA
# ----------------------------------------------------------
def PerformEDA(df):

    print("-" * 60)
    print("Step 1 : Exploratory Data Analysis")
    print("-" * 60)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nDataset Info:")
    print(df.info())

    print("\nNull Values:")
    print(df.isnull().sum())

    print("\nBasic Statistics:")
    print(df.describe())


# ----------------------------------------------------------
# Function : Data Preprocessing
# ----------------------------------------------------------
def PreprocessData(df):

    print("\n" + "-" * 60)
    print("Step 2 : Data Preprocessing")
    print("-" * 60)

    # Replace 0 values with median (important for this dataset)
    columns = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

    for col in columns:
        df[col] = df[col].replace(0, df[col].median())

    print("Handled zero values using median replacement")

    # Split features and target
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    # Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print("Feature scaling applied using StandardScaler")

    return X_scaled, y


# ----------------------------------------------------------
# Function : Train Models
# ----------------------------------------------------------
def TrainModels(X_train, X_test, y_train, y_test):

    print("\n" + "-" * 60)
    print("Step 3 : Model Training")
    print("-" * 60)

    models = {
        "Logistic Regression": LogisticRegression(),
        "KNN": KNeighborsClassifier(n_neighbors=5),
        "Decision Tree": DecisionTreeClassifier()
    }

    results = {}

    for name, model in models.items():

        print(f"\nTraining {name}...")

        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)

        print(f"Accuracy of {name} : {acc:.4f}")

        print("Confusion Matrix:")
        print(confusion_matrix(y_test, y_pred))

        print("Classification Report:")
        print(classification_report(y_test, y_pred))

        results[name] = (model, acc)

    return results


# ----------------------------------------------------------
# Function : Predict New Data
# ----------------------------------------------------------
def PredictSample(model, scaler):

    print("\n" + "-" * 60)
    print("Step 5 : Prediction on Sample Data")
    print("-" * 60)

    # Example patient data
    sample = np.array([[2, 120, 70, 20, 85, 30.0, 0.5, 30]])

    sample_scaled = scaler.transform(sample)

    prediction = model.predict(sample_scaled)

    if prediction[0] == 1:
        print("Prediction : Patient is Diabetic")
    else:
        print("Prediction : Patient is NOT Diabetic")


# ----------------------------------------------------------
# Main Function
# ----------------------------------------------------------
def main():

    print("-" * 60)
    print("Marvellous Infosystems : Diabetes Prediction")
    print("-" * 60)

    # File path
    DataPath  = "/Users/suniljaware/Desktop/Python_Assignments/Assignment49/diabetes.csv"

    # Check file
    if not os.path.exists(DataPath):
        print("ERROR : CSV file not found")
        print("Place diabetes.csv in same folder")
        return

    # Load dataset
    df = pd.read_csv(DataPath)

    # Step 1 : EDA
    PerformEDA(df)

    # Step 2 : Preprocessing
    X, y = PreprocessData(df)

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Step 3 & 4 : Train + Evaluate
    results = TrainModels(X_train, X_test, y_train, y_test)

    # Select best model
    best_model_name = max(results, key=lambda x: results[x][1])
    best_model = results[best_model_name][0]

    print("\nBest Model :", best_model_name)

    # Refit scaler for prediction
    scaler = StandardScaler()
    scaler.fit(X)

    # Step 5 : Prediction
    PredictSample(best_model, scaler)


# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------
if __name__ == "__main__":
    main()