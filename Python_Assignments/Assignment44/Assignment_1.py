import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# ----------------------------------------------------------
# This function is used to load the dataset, clean it,
# prepare the data, train Linear Regression model,
# test the model and display expected and predicted values.
# ----------------------------------------------------------
def MarvellousAdvertisingPredictor(DataPath):
    border = "-" * 60

# ----------------------------------------------------------
# Step 1 : Load the dataset
# ----------------------------------------------------------
    print(border)
    print("Step 1 : Load the dataset")
    print(border)

    df = pd.read_csv(DataPath)

    print("Dataset loaded successfully")
    print("Shape of dataset :", df.shape)

    print(border)
    print("Some entries from dataset")
    print(df.head())
    print(border)

# ----------------------------------------------------------
# Step 2 : Clean, Prepare and Manipulate data
# ----------------------------------------------------------
    print(border)
    print("Step 2 : Clean, Prepare and Manipulate data")
    print(border)

    # Remove serial number column if present
    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"], inplace=True)
        print("Unwanted serial number column removed")

    # Remove empty rows if any
    df.dropna(inplace=True)

    print("Total records :", df.shape[0])
    print("Total columns :", df.shape[1])
    print("Column names  :", df.columns.tolist())
    print(border)

# ----------------------------------------------------------
# Step 3 : Train the data using Linear Regression
# ----------------------------------------------------------
    print(border)
    print("Step 3 : Train the model")
    print(border)

    # Separate input features and output label
    X = df[["TV", "radio", "newspaper"]]
    Y = df["sales"]

    print("Shape of X :", X.shape)
    print("Shape of Y :", Y.shape)

    # Split the dataset into half parts
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )

    print("Training data size :", X_train.shape)
    print("Testing data size  :", X_test.shape)

    # Create Linear Regression object
    Model = LinearRegression()

    # Train the model
    Model.fit(X_train, Y_train)

    print("Model trained successfully")
    print(border)
    print("Model coefficients are :")
    print("TV coefficient        :", Model.coef_[0])
    print("Radio coefficient     :", Model.coef_[1])
    print("Newspaper coefficient :", Model.coef_[2])
    print("Intercept             :", Model.intercept_)
    print(border)

# ----------------------------------------------------------
# Step 4 : Test the trained model
# ----------------------------------------------------------
    print(border)
    print("Step 4 : Test the model")
    print(border)

    Y_Pred = Model.predict(X_test)

# ----------------------------------------------------------
# Step 5 : Display expected values and predicted values
# ----------------------------------------------------------
    print(border)
    print("Step 5 : Display expected and predicted values")
    print(border)

    Result = pd.DataFrame({
        "Expected Sales": Y_test.values,
        "Predicted Sales": Y_Pred
    })

    print(Result)

    print(border)
    print("Prediction completed successfully")
    print(border)


# ----------------------------------------------------------
# Main function
# ----------------------------------------------------------
def main():
    # Get current python file folder path
    BaseDir = os.path.dirname(os.path.abspath(__file__))

    # Build path for csv file
    DataPath = os.path.join(BaseDir, "Advertising.csv")

    # Check if file exists
    if not os.path.exists(DataPath):
        print("-" * 60)
        print("ERROR : CSV file not found")
        print("Expected file path :", DataPath)
        print("Please place Advertising.csv in the same folder as this python file.")
        print("-" * 60)
        return

    # Call main predictor function
    MarvellousAdvertisingPredictor(DataPath)


# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------
if __name__ == "__main__":
    main()