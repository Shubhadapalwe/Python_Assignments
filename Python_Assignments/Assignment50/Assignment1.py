# ----------------------------------------------------------
# Marvellous Infosystems : ML Assignment
# Bank Term Deposit Subscription Prediction
# ----------------------------------------------------------

import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score


# ----------------------------------------------------------
# Step 1 : Load and Explore Data
# ----------------------------------------------------------
def LoadAndExploreDataset(DataPath):

    print("-" * 60)
    print("Step 1 : Load and Explore Dataset")
    print("-" * 60)

    if not os.path.exists(DataPath):
        print("ERROR : CSV file not found")
        return None

    df = pd.read_csv(DataPath, sep=';')   # Bank dataset uses ';'

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nDataset Info:")
    print(df.info())

    print("\nNull Values:")
    print(df.isnull().sum())

    print("\nBasic Statistics:")
    print(df.describe())

    print("\nTarget Distribution:")
    print(df['y'].value_counts())

    return df


# ----------------------------------------------------------
# Step 2 : Preprocessing
# ----------------------------------------------------------
def PreprocessDataset(df):

    print("\n" + "-" * 60)
    print("Step 2 : Data Preprocessing")
    print("-" * 60)

    # Handle 'unknown' values
    df.replace("unknown", np.nan, inplace=True)

    # Fill missing with mode
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].fillna(df[col].mode()[0])

    # Convert target column
    df['y'] = df['y'].map({'yes': 1, 'no': 0})

    # One-hot encoding
    df = pd.get_dummies(df, drop_first=True)

    # Split features and target
    X = df.drop("y", axis=1)
    y = df["y"]

    # Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print("Encoding + Scaling completed")

    return X_scaled, y


# ----------------------------------------------------------
# Step 3 : Split Data
# ----------------------------------------------------------
def SplitDataset(X, y):

    print("\n" + "-" * 60)
    print("Step 3 : Train-Test Split")
    print("-" * 60)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Training size :", X_train.shape)
    print("Testing size :", X_test.shape)

    return X_train, X_test, y_train, y_test


# ----------------------------------------------------------
# Step 4 : Train Models
# ----------------------------------------------------------
def TrainClassificationModels(X_train, X_test, y_train, y_test):

    print("\n" + "-" * 60)
    print("Step 4 : Model Training")
    print("-" * 60)

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "KNN": KNeighborsClassifier(n_neighbors=5),
        "Random Forest": RandomForestClassifier()
    }

    results = {}

    for name, model in models.items():

        print(f"\nTraining {name}...")

        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)

        print("Accuracy :", acc)

        print("Confusion Matrix:")
        print(confusion_matrix(y_test, y_pred))

        print("Classification Report:")
        print(classification_report(y_test, y_pred))

        # ROC AUC
        try:
            y_prob = model.predict_proba(X_test)[:, 1]
            roc = roc_auc_score(y_test, y_prob)
            print("ROC-AUC Score :", roc)
        except:
            print("ROC not available")

        results[name] = (model, acc)

    return results


# ----------------------------------------------------------
# Step 5 : Final Prediction
# ----------------------------------------------------------
def PredictFinalOutput(model, X_test):

    print("\n" + "-" * 60)
    print("Step 5 : Final Prediction")
    print("-" * 60)

    predictions = model.predict(X_test[:5])

    print("Sample Predictions (1 = Yes, 0 = No):")
    print(predictions)


# ----------------------------------------------------------
# Main Function
# ----------------------------------------------------------
def main():

    print("-" * 60)
    print("Bank Term Deposit Prediction")
    print("-" * 60)

    DataPath = "bank.csv"   # Keep file in same folder

    df = LoadAndExploreDataset(DataPath)

    if df is None:
        return

    X, y = PreprocessDataset(df)

    X_train, X_test, y_train, y_test = SplitDataset(X, y)

    results = TrainClassificationModels(X_train, X_test, y_train, y_test)

    # Best model selection
    best_model_name = max(results, key=lambda x: results[x][1])
    best_model = results[best_model_name][0]

    print("\nBest Model :", best_model_name)

    PredictFinalOutput(best_model, X_test)


# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------
if __name__ == "__main__":
    main()
    