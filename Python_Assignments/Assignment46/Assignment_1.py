
from sklearn.linear_model import LinearRegression


# ----------------------------------------------------------
# Train regression model using Study Hours and Marks
# ----------------------------------------------------------
def TrainStudyHoursModel():

    border = "-" * 60

    print(border)
    print("Training Linear Regression Model : StudyHours vs Marks")
    print(border)

    # Input feature
    StudyHours = [[1], [2], [3], [4], [5]]

    # Output labels
    Marks = [50, 55, 60, 65, 70]

    print("Study Hours :", StudyHours)
    print("Marks       :", Marks)

    # Create Linear Regression model
    Model = LinearRegression()

    # Train the model
    Model.fit(StudyHours, Marks)

    print(border)
    print("Model trained successfully")
    print(border)

    # Display model parameters
    print("Coefficient :", Model.coef_[0])
    print("Intercept   :", Model.intercept_)

    print(border)

    return Model


# ----------------------------------------------------------
# Predict marks for given study hours
# ----------------------------------------------------------
def PredictMarksForStudyHours(Model):

    border = "-" * 60

    print(border)
    print("Predicting Marks for 6 Study Hours")
    print(border)

    PredictedMarks = Model.predict([[6]])

    print("Predicted Marks :", PredictedMarks[0])

    print(border)


# ----------------------------------------------------------
# Train regression model using two input features
# StudyHours and SleepHours
# ----------------------------------------------------------
def TrainMultiFeatureRegressionModel():

    border = "-" * 60

    print(border)
    print("Training Regression Model using StudyHours and SleepHours")
    print(border)

    # Input features
    # [StudyHours , SleepHours]
    InputFeatures = [
        [1, 7],
        [2, 6],
        [3, 7],
        [4, 6],
        [5, 8]
    ]

    # Output feature
    Marks = [50, 55, 60, 65, 70]

    print("Input Features :")
    for value in InputFeatures:
        print(value)

    print("Output Marks :", Marks)

    # Create model
    Model = LinearRegression()

    # Train model
    Model.fit(InputFeatures, Marks)

    print(border)
    print("Model trained successfully")
    print(border)

    # Print coefficients
    print("Coefficient for StudyHours :", Model.coef_[0])
    print("Coefficient for SleepHours :", Model.coef_[1])

    # Print intercept
    print("Intercept :", Model.intercept_)

    print(border)


# ----------------------------------------------------------
# Print explanation of regression coefficients
# ----------------------------------------------------------
def ExplainRegressionCoefficients():

    border = "-" * 60

    print(border)
    print("Importance of Coefficients in Regression")
    print(border)

    print("Coefficients show how much each input feature affects the output.")
    print("If coefficient is positive, output increases with input.")
    print("If coefficient is negative, output decreases.")
    print("Using coefficients we can understand which feature has")
    print("more impact on the prediction.")

    print(border)



def main():

    Model = TrainStudyHoursModel()

    PredictMarksForStudyHours(Model)

    TrainMultiFeatureRegressionModel()

    ExplainRegressionCoefficients()



if __name__ == "__main__":
    main()