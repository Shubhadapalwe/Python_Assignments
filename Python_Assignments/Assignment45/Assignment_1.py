# ----------------------------------------------------------
# Required libraries
# ----------------------------------------------------------
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# ----------------------------------------------------------
# This function calculates accuracy of the model
# ----------------------------------------------------------
def CheckAccuracy(X_test, Y_test, Y_pred):

    border = "-" * 60

    print(border)
    print("Step 5 : Calculate Accuracy")
    print(border)

    Accuracy = accuracy_score(Y_test, Y_pred) * 100

    print("Accuracy of model is :", round(Accuracy, 2), "%")

    print(border)


# ----------------------------------------------------------
# Main Machine Learning Function
# ----------------------------------------------------------
def MarvellousWinePredictor(DataPath):

    border = "-" * 60

# ----------------------------------------------------------
# Step 1 : Get Data
# ----------------------------------------------------------
    print(border)
    print("Step 1 : Get Data")
    print(border)

    df = pd.read_csv(DataPath)

    print("Dataset loaded successfully")
    print("Shape of dataset :", df.shape)

    print(border)
    print("First few records of dataset")
    print(df.head())
    print(border)


# ----------------------------------------------------------
# Step 2 : Clean, Prepare and Manipulate Data
# ----------------------------------------------------------
    print(border)
    print("Step 2 : Clean, Prepare and Manipulate Data")
    print(border)

    # Remove unwanted index column if present
    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"], inplace=True)
        print("Removed unwanted index column")

    # Remove empty rows
    df.dropna(inplace=True)

    print("Total rows :", df.shape[0])
    print("Total columns :", df.shape[1])

    print("Column names :", df.columns.tolist())

    print(border)


# ----------------------------------------------------------
# Step 3 : Train Data
# ----------------------------------------------------------
    print(border)
    print("Step 3 : Train Data")
    print(border)

    # Separate input features and output label
    X = df.drop(columns=["Class"])
    Y = df["Class"]

    print("Input shape :", X.shape)
    print("Output shape :", Y.shape)

    # Split dataset into half
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )

    print("Training data size :", X_train.shape)
    print("Testing data size :", X_test.shape)

    # Create KNN classifier
    Model = KNeighborsClassifier(n_neighbors=3)

    # Train the model
    Model.fit(X_train, Y_train)

    print("Model trained successfully")

    print(border)


# ----------------------------------------------------------
# Step 4 : Test Data
# ----------------------------------------------------------
    print(border)
    print("Step 4 : Test Data")
    print(border)

    Y_pred = Model.predict(X_test)

    Result = pd.DataFrame({
        "Expected Class": Y_test.values,
        "Predicted Class": Y_pred
    })

    print(Result)

    print(border)


# ----------------------------------------------------------
# Step 5 : Calculate Accuracy
# ----------------------------------------------------------
    CheckAccuracy(X_test, Y_test, Y_pred)


# ----------------------------------------------------------
# Main function
# ----------------------------------------------------------
def main():

    BaseDir = os.path.dirname(os.path.abspath(__file__))

    DataPath = os.path.join(BaseDir, "WinePredictor.csv")

    if not os.path.exists(DataPath):

        print("-" * 60)
        print("ERROR : CSV file not found")
        print("Expected path :", DataPath)
        print("Please place WinePredictor.csv in same folder")
        print("-" * 60)
        return

    MarvellousWinePredictor(DataPath)


# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------
if __name__ == "__main__":
    main()