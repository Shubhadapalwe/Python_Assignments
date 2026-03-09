import math
import matplotlib.pyplot as plt


def MarvellousLinearRegression():
    border = "-" * 50

# ----------------------------------------------------------
# Step 1 : Load the dataset
# ----------------------------------------------------------
    print(border)
    print("Step 1 : Load the dataset")
    print(border)

    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    print("Values of X :", X)
    print("Values of Y :", Y)

# ----------------------------------------------------------
# Step 2 : Calculate Mean of X and Mean of Y
# ----------------------------------------------------------
    print(border)
    print("Step 2 : Calculate Mean of X and Mean of Y")
    print(border)

    mean_x = sum(X) / len(X)
    mean_y = sum(Y) / len(Y)

    print("Mean of X =", mean_x)
    print("Mean of Y =", mean_y)

# ----------------------------------------------------------
# Step 3 : Calculate slope (m)
# Formula:
# m = sum((Xi - Xmean) * (Yi - Ymean)) / sum((Xi - Xmean)^2)
# ----------------------------------------------------------
    print(border)
    print("Step 3 : Calculate slope (m)")
    print(border)

    numerator = 0
    denominator = 0

    for i in range(len(X)):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x) ** 2)

    m = numerator / denominator

    print("Numerator   =", numerator)
    print("Denominator =", denominator)
    print("Slope (m)   =", round(m, 2))

# ----------------------------------------------------------
# Step 4 : Calculate intercept (c)
# Formula:
# c = Ymean - m * Xmean
# ----------------------------------------------------------
    print(border)
    print("Step 4 : Calculate intercept (c)")
    print(border)

    c = mean_y - (m * mean_x)

    print("Intercept (c) =", round(c, 2))

# ----------------------------------------------------------
# Step 5 : Display Regression Equation
# Equation:
# Y = mX + c
# ----------------------------------------------------------
    print(border)
    print("Step 5 : Display Regression Equation")
    print(border)

    print(f"Regression Equation : Y = {round(m,2)}X + {round(c,2)}")

# ----------------------------------------------------------
# Step 6 : Predict Y for X = 6
# Formula:
# Y = mX + c
# ----------------------------------------------------------
    print(border)
    print("Step 6 : Predict Y for X = 6")
    print(border)

    x_new = 6
    y_pred_new = (m * x_new) + c

    print(f"Predicted Y for X = {x_new} : {round(y_pred_new,2)}")

# ----------------------------------------------------------
# Step 7 : Predict all Y values using regression equation
# ----------------------------------------------------------
    print(border)
    print("Step 7 : Predict all Y values")
    print(border)

    Y_pred = []

    for value in X:
        prediction = (m * value) + c
        Y_pred.append(prediction)

    for i in range(len(X)):
        print(f"X = {X[i]}  Actual Y = {Y[i]}  Predicted Y = {round(Y_pred[i],2)}")

# ----------------------------------------------------------
# Step 8 : Calculate Mean Squared Error (MSE)
# Formula:
# MSE = sum((Yi - Ypred)^2) / n
# ----------------------------------------------------------
    print(border)
    print("Step 8 : Calculate Mean Squared Error (MSE)")
    print(border)

    mse_sum = 0

    for i in range(len(Y)):
        error = Y[i] - Y_pred[i]
        squared_error = error ** 2
        mse_sum = mse_sum + squared_error
        print(f"Actual = {Y[i]}  Predicted = {round(Y_pred[i],2)}  Squared Error = {round(squared_error,2)}")

    mse = mse_sum / len(Y)

    print("Mean Squared Error (MSE) =", round(mse, 4))

# ----------------------------------------------------------
# Step 9 : Calculate R² Score manually
# Formula:
# R² = 1 - (SS_res / SS_tot)
# ----------------------------------------------------------
    print(border)
    print("Step 9 : Calculate R² Score")
    print(border)

    ss_res = 0
    ss_tot = 0

    for i in range(len(Y)):
        ss_res = ss_res + ((Y[i] - Y_pred[i]) ** 2)
        ss_tot = ss_tot + ((Y[i] - mean_y) ** 2)

    r2_score = 1 - (ss_res / ss_tot)

    print("SS_res =", round(ss_res, 4))
    print("SS_tot =", round(ss_tot, 4))
    print("R² Score =", round(r2_score, 4))


def MarvellousSalaryPrediction():
    border = "-" * 50

# ----------------------------------------------------------
# Step 1 : Load salary dataset
# ----------------------------------------------------------
    print(border)
    print("Step 1 : Load salary dataset")
    print(border)

    experience = [1, 2, 3, 4, 5]
    salary = [20000, 25000, 30000, 35000, 40000]

    print("Experience :", experience)
    print("Salary     :", salary)

# ----------------------------------------------------------
# Step 2 : Calculate mean values
# ----------------------------------------------------------
    print(border)
    print("Step 2 : Calculate mean values")
    print(border)

    mean_x = sum(experience) / len(experience)
    mean_y = sum(salary) / len(salary)

    print("Mean Experience =", mean_x)
    print("Mean Salary     =", mean_y)

# ----------------------------------------------------------
# Step 3 : Calculate slope and intercept
# ----------------------------------------------------------
    print(border)
    print("Step 3 : Calculate slope and intercept")
    print(border)

    numerator = 0
    denominator = 0

    for i in range(len(experience)):
        numerator = numerator + ((experience[i] - mean_x) * (salary[i] - mean_y))
        denominator = denominator + ((experience[i] - mean_x) ** 2)

    m = numerator / denominator
    c = mean_y - (m * mean_x)

    print("Slope (m)     =", round(m, 2))
    print("Intercept (c) =", round(c, 2))

# ----------------------------------------------------------
# Step 4 : Predict salary for 6 years experience
# ----------------------------------------------------------
    print(border)
    print("Step 4 : Predict salary for 6 years experience")
    print(border)

    years = 6
    predicted_salary = (m * years) + c

    print(f"Predicted Salary for {years} Years Experience : ₹{round(predicted_salary,2)}")

# ----------------------------------------------------------
# Step 5 : Plot regression line using matplotlib
# ----------------------------------------------------------
    print(border)
    print("Step 5 : Plot regression line")
    print(border)

    predicted_line = []

    for value in experience:
        predicted_line.append((m * value) + c)

    plt.figure(figsize=(8, 5))
    plt.scatter(experience, salary, label="Data Points")
    plt.plot(experience, predicted_line, label="Regression Line")
    plt.xlabel("Experience (Years)")
    plt.ylabel("Salary")
    plt.title("Experience vs Salary")
    plt.legend()
    plt.grid(True)
    plt.show()


def TheoryAnswers():
    border = "-" * 50

    print(border)
    print("Theory Answers")
    print(border)

# ----------------------------------------------------------
# Q4
# ----------------------------------------------------------
    print("4. Why is KNN called a lazy learner?")
    print("Answer : KNN is called a lazy learner because it does not learn much at training time.")
    print("It just stores the data and when new input comes, then it checks nearest neighbors.")
    print()

# ----------------------------------------------------------
# Q5
# ----------------------------------------------------------
    print("5. What happens if K is too small?")
    print("Answer : If K is too small, prediction may depend on very few points.")
    print("Because of this, noise or one wrong point can affect the result easily.")
    print("So model may become over sensitive.")
    print()

# ----------------------------------------------------------
# Q6
# ----------------------------------------------------------
    print("6. What happens if K is too large?")
    print("Answer : If K is too large, many points are considered in prediction.")
    print("Then nearby important points may get ignored and model may become less accurate.")
    print("Sometimes it can predict mostly majority class.")
    print()

# ----------------------------------------------------------
# Q7
# ----------------------------------------------------------
    print("7. Why does linear regression minimize squared error?")
    print("Answer : Linear regression uses squared error because bigger errors become more important after squaring.")
    print("So the best fit line tries to reduce large mistakes also.")
    print("It is also easier in mathematical calculation.")
    print()

# ----------------------------------------------------------
# Q8
# ----------------------------------------------------------
    print("8. What is the difference between MSE and R²?")
    print("Answer : MSE tells the average squared difference between actual value and predicted value.")
    print("Smaller MSE means better model.")
    print("R² tells how much data variation is explained by the model.")
    print("Higher R² means model fits better.")
    print()

# ----------------------------------------------------------
# Q9
# ----------------------------------------------------------
    print("9. Why R² cannot be greater than 1?")
    print("Answer : R² shows how well the model explains the data.")
    print("If value is 1, it means perfect fit.")
    print("So normally it should not go above 1 because more than full explanation is not possible.")
    print()

# ----------------------------------------------------------
# Q10
# ----------------------------------------------------------
    print("10. Can KNN be used for regression?")
    print("Answer : Yes, KNN can be used for regression also.")
    print("In classification it gives majority class, but in regression it gives average of nearest values.")
    print("So output becomes numeric instead of class label.")
    print()


# ----------------------------------------------------------
# Main Function
# ----------------------------------------------------------
def main():
    MarvellousLinearRegression()
    MarvellousSalaryPrediction()
    TheoryAnswers()


if __name__ == "__main__":
    main()