import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# ----------------------------------------------------------
# This function is used to calculate accuracy of KNN model
# by dividing the dataset into training data and testing data.
# We use different K values to check model performance.
# ----------------------------------------------------------
def CheckAccuracy(df, KValue):
    border = "-" * 50

    # Display heading for accuracy section
    print(border)
    print(f"Check Accuracy using K = {KValue}")
    print(border)

    # Create copy of dataframe so original dataset remains unchanged
    DataFrame = df.copy()

    # Create LabelEncoder objects for each text column
    WeatherEncoder = LabelEncoder()
    TemperatureEncoder = LabelEncoder()
    PlayEncoder = LabelEncoder()

    # Convert categorical string values into numeric values
    DataFrame["Whether"] = WeatherEncoder.fit_transform(DataFrame["Whether"])
    DataFrame["Temperature"] = TemperatureEncoder.fit_transform(DataFrame["Temperature"])
    DataFrame["Play"] = PlayEncoder.fit_transform(DataFrame["Play"])

    # Separate input features and output label
    X = DataFrame[["Whether", "Temperature"]]
    Y = DataFrame["Play"]

    # Split dataset into 50% training and 50% testing
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )

    # Create KNN model object with provided K value
    Model = KNeighborsClassifier(n_neighbors=KValue)

    # Train model using training data
    Model.fit(X_train, Y_train)

    # Predict output for testing data
    Y_Pred = Model.predict(X_test)

    # Calculate accuracy in percentage
    Accuracy = accuracy_score(Y_test, Y_Pred) * 100

    print("Accuracy is :", round(Accuracy, 2), "%")
    print()

    return Accuracy


# ----------------------------------------------------------
# This function loads the dataset, prepares the data,
# trains the model, accepts user input and predicts result.
# ----------------------------------------------------------
def MarvellousPlayPredictor(DataPath):
    border = "-" * 50

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

    # Remove serial number column if present in csv
    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"], inplace=True)
        print("Unnamed serial number column removed")

    # Remove empty rows if any
    df.dropna(inplace=True)

    print("Total records :", df.shape[0])
    print("Total columns :", df.shape[1])
    print("Column names  :", df.columns.tolist())

    print(border)
    print("Unique values in Whether     :", df["Whether"].unique())
    print("Unique values in Temperature :", df["Temperature"].unique())
    print("Unique values in Play        :", df["Play"].unique())

# ----------------------------------------------------------
# Step 3 : Convert categorical values into numeric values
# ----------------------------------------------------------
    print(border)
    print("Step 3 : Convert categorical data into numeric form")
    print(border)

    # Create encoders for all categorical columns
    WeatherEncoder = LabelEncoder()
    TemperatureEncoder = LabelEncoder()
    PlayEncoder = LabelEncoder()

    # Make a copy of original dataframe for encoded processing
    EncodedDataFrame = df.copy()

    # Encode text values into numeric constants
    EncodedDataFrame["Whether"] = WeatherEncoder.fit_transform(EncodedDataFrame["Whether"])
    EncodedDataFrame["Temperature"] = TemperatureEncoder.fit_transform(EncodedDataFrame["Temperature"])
    EncodedDataFrame["Play"] = PlayEncoder.fit_transform(EncodedDataFrame["Play"])

    print("Encoded dataset:")
    print(EncodedDataFrame.head())
    print(border)

    # Display mapping of categorical text to numbers
    print("Whether Mapping:")
    for Index, Value in enumerate(WeatherEncoder.classes_):
        print(Value, "->", Index)

    print("\nTemperature Mapping:")
    for Index, Value in enumerate(TemperatureEncoder.classes_):
        print(Value, "->", Index)

    print("\nPlay Mapping:")
    for Index, Value in enumerate(PlayEncoder.classes_):
        print(Value, "->", Index)

# ----------------------------------------------------------
# Step 4 : Train the model using whole dataset
# ----------------------------------------------------------
    print(border)
    print("Step 4 : Train the KNN model using whole dataset")
    print(border)

    # Separate input and output columns
    X = EncodedDataFrame[["Whether", "Temperature"]]
    Y = EncodedDataFrame["Play"]

    print("Input data shape  :", X.shape)
    print("Output data shape :", Y.shape)

    # As per instruction use K = 3
    KValue = 3

    # Create KNN model
    Model = KNeighborsClassifier(n_neighbors=KValue)

    # Train model on full dataset
    Model.fit(X, Y)

    print("KNN model trained successfully using K =", KValue)

# ----------------------------------------------------------
# Step 5 : Test model using user input
# ----------------------------------------------------------
    print(border)
    print("Step 5 : Test data by passing new input")
    print(border)

    print("Available Whether values     :", list(df["Whether"].unique()))
    print("Available Temperature values :", list(df["Temperature"].unique()))
    print(border)

    # Accept user values
    UserWeather = input("Enter weather : ")
    UserTemperature = input("Enter temperature : ")

    # Convert user input into neat format
    UserWeather = UserWeather.strip().capitalize()
    UserTemperature = UserTemperature.strip().capitalize()

    # Check if entered weather is valid
    if UserWeather not in WeatherEncoder.classes_:
        print("Invalid weather entered")
        return

    # Check if entered temperature is valid
    if UserTemperature not in TemperatureEncoder.classes_:
        print("Invalid temperature entered")
        return

    # Transform user text input into numeric values
    WeatherValue = WeatherEncoder.transform([UserWeather])[0]
    TemperatureValue = TemperatureEncoder.transform([UserTemperature])[0]

    # Prepare input in model-required 2D form
    PredictionInput = [[WeatherValue, TemperatureValue]]

    # Predict result
    Result = Model.predict(PredictionInput)

    # Convert numeric output back to original label
    FinalResult = PlayEncoder.inverse_transform(Result)

    print(border)
    print("Predicted output is :", FinalResult[0])
    print(border)

# ----------------------------------------------------------
# Step 6 : Check model accuracy for different K values
# ----------------------------------------------------------
    print(border)
    print("Step 6 : Calculate accuracy by changing K value")
    print(border)

    for K in [1, 3, 5]:
        CheckAccuracy(df, K)


# ----------------------------------------------------------
# Main function
# ----------------------------------------------------------
def main():
    # Get the absolute path of current python file folder
    BaseDir = os.path.dirname(os.path.abspath(__file__))

    # Build path for csv file located in same folder
    DataPath = os.path.join(BaseDir, "PlayPredictor.csv")

    # Check whether csv file exists before reading
    if not os.path.exists(DataPath):
        print("-" * 50)
        print("ERROR : CSV file not found")
        print("Expected file path :", DataPath)
        print("Please place PlayPredictor.csv in the same folder as this python file.")
        print("-" * 50)
        return

    # Call main predictor function
    MarvellousPlayPredictor(DataPath)


# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------
if __name__ == "__main__":
    main()