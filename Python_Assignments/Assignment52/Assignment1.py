# ----------------------------------------------------------
# Marvellous Infosystems : Machine Learning Assignment
# Fake News Detection using Voting Classifier
# ----------------------------------------------------------

import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# ----------------------------------------------------------
# Function to load both csv files and combine them
# ----------------------------------------------------------
def LoadAndPrepareDataset(FakePath, TruePath):

    border = "-" * 60

    print(border)
    print("Step 1 : Load Both CSV Files")
    print(border)

    fake_df = pd.read_csv(FakePath)
    true_df = pd.read_csv(TruePath)

    print("Fake dataset shape :", fake_df.shape)
    print("True dataset shape :", true_df.shape)

    print(border)
    print("Step 2 : Add Label Column")
    print(border)

    # 0 = Fake, 1 = Real
    fake_df["label"] = 0
    true_df["label"] = 1

    print("Label added successfully")

    print(border)
    print("Step 3 : Combine Both Datasets")
    print(border)

    df = pd.concat([fake_df, true_df], ignore_index=True)

    print("Combined dataset shape :", df.shape)

    print(border)
    print("Step 4 : Keep Only Relevant Columns")
    print(border)

    # Use title + text together for better classification
    df = df[["title", "text", "label"]]

    # Remove null values
    df.dropna(inplace=True)

    # Combine title and text into one feature
    df["content"] = df["title"] + " " + df["text"]

    print("Final dataset shape :", df.shape)
    print(df.head())

    return df


# ----------------------------------------------------------
# Function to convert text into numeric features
# ----------------------------------------------------------
def ExtractFeatures(df):

    border = "-" * 60

    print(border)
    print("Part 2 : Feature Extraction using TF-IDF")
    print(border)

    X = df["content"]
    Y = df["label"]

    Vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)

    X_tfidf = Vectorizer.fit_transform(X)

    print("TF-IDF feature extraction completed")
    print("Feature matrix shape :", X_tfidf.shape)

    return X_tfidf, Y


# ----------------------------------------------------------
# Function to train all models
# ----------------------------------------------------------
def TrainAllModels(X_train, X_test, Y_train, Y_test):

    border = "-" * 60

    print(border)
    print("Part 3 : Model Training")
    print(border)

    # Individual models
    LogisticModel = LogisticRegression(max_iter=1000)
    DecisionTreeModel = DecisionTreeClassifier(random_state=42)

    # Hard Voting
    HardVotingModel = VotingClassifier(
        estimators=[
            ("lr", LogisticModel),
            ("dt", DecisionTreeModel)
        ],
        voting="hard"
    )

    # Soft Voting
    SoftVotingModel = VotingClassifier(
        estimators=[
            ("lr", LogisticRegression(max_iter=1000)),
            ("dt", DecisionTreeClassifier(random_state=42))
        ],
        voting="soft"
    )

    Models = {
        "Logistic Regression": LogisticModel,
        "Decision Tree": DecisionTreeModel,
        "Hard Voting Classifier": HardVotingModel,
        "Soft Voting Classifier": SoftVotingModel
    }

    Results = {}

    for Name, Model in Models.items():

        print(border)
        print(f"Training : {Name}")
        print(border)

        Model.fit(X_train, Y_train)

        Y_Pred = Model.predict(X_test)

        Accuracy = accuracy_score(Y_test, Y_Pred)

        print("Accuracy :", round(Accuracy * 100, 2), "%")

        print("Confusion Matrix :")
        print(confusion_matrix(Y_test, Y_Pred))

        print("Classification Report :")
        print(classification_report(Y_test, Y_Pred))

        Results[Name] = Accuracy

    return Results


# ----------------------------------------------------------
# Function to display final comparison
# ----------------------------------------------------------
def CompareModelResults(Results):

    border = "-" * 60

    print(border)
    print("Part 4 : Final Accuracy Comparison")
    print(border)

    for Name, Accuracy in Results.items():
        print(f"{Name} : {round(Accuracy * 100, 2)} %")

    print(border)

    BestModel = max(Results, key=Results.get)

    print("Best Performing Model :", BestModel)
    print(border)


# ----------------------------------------------------------
# Main function
# ----------------------------------------------------------
def main():

    border = "-" * 60

    print(border)
    print("Marvellous Infosystems : Fake News Detection Project")
    print(border)

    BaseDir = os.path.dirname(os.path.abspath(__file__))

    FakePath = os.path.join(BaseDir, "fake.csv")
    TruePath = os.path.join(BaseDir, "true.csv")

    if not os.path.exists(FakePath):
        print("ERROR : fake.csv file not found")
        return

    if not os.path.exists(TruePath):
        print("ERROR : true.csv file not found")
        return

    # Load and prepare dataset
    df = LoadAndPrepareDataset(FakePath, TruePath)

    # Feature extraction
    X, Y = ExtractFeatures(df)

    # Train-test split
    print(border)
    print("Train-Test Split")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Training data shape :", X_train.shape)
    print("Testing data shape  :", X_test.shape)

    # Train all models
    Results = TrainAllModels(X_train, X_test, Y_train, Y_test)

    # Final comparison
    CompareModelResults(Results)


# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------
if __name__ == "__main__":
    main()