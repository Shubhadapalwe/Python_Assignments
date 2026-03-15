

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report


# ----------------------------------------------------------
# Q1 : Calculate Mean 
# ----------------------------------------------------------
def CalculateDatasetMean():

    border = "-" * 60
    print(border)
    print("Q1 : Calculate Mean of Dataset using NumPy")
    print(border)

    data = np.array([6, 7, 8, 9, 10, 11, 12])

    print("Dataset :", data)

    mean_value = np.mean(data)

    print("Mean of dataset is :", mean_value)
    print(border)


# ----------------------------------------------------------
# Q2 : Variance and Standard Deviation
# ----------------------------------------------------------
def CalculateVarianceAndStd():

    border = "-" * 60
    print(border)
    print("Q2 : Calculate Variance and Standard Deviation")
    print(border)

    data = np.array([6, 7, 8, 9, 10, 11, 12])

    print("Dataset :", data)

    variance = np.var(data)
    std_dev = np.std(data)

    print("Variance :", variance)
    print("Standard Deviation :", std_dev)

    print(border)


# ----------------------------------------------------------
# Q3 : Feature Scaling using StandardScaler
# ----------------------------------------------------------
def PerformFeatureScaling():

    border = "-" * 60
    print(border)
    print("Q3 : Feature Scaling using StandardScaler")
    print(border)

    data = np.array([
        [25, 20000],
        [30, 40000],
        [35, 80000]
    ])

    print("Original Dataset")
    print(data)

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(data)

    print("\nScaled Dataset")
    print(scaled_data)

    print(border)


# ----------------------------------------------------------
# Q4 : Euclidean Distance before and after scaling
# ----------------------------------------------------------
def CalculateEuclideanDistance():

    border = "-" * 60
    print(border)
    print("Q4 : Euclidean Distance Before and After Scaling")
    print(border)

    data = np.array([
        [25, 20000],
        [35, 80000]
    ])

    print("Original Points")
    print(data)

    # Distance before scaling
    dist_before = np.linalg.norm(data[0] - data[1])

    print("Distance before scaling :", dist_before)

    scaler = StandardScaler()
    scaled = scaler.fit_transform(data)

    dist_after = np.linalg.norm(scaled[0] - scaled[1])

    print("Distance after scaling :", dist_after)

    print(border)


# ----------------------------------------------------------
# Q5 : Concept of Classification Report
# ----------------------------------------------------------
def ExplainClassificationReport():

    border = "-" * 60
    print(border)
    print("Q5 : What is Classification Report?")
    print(border)

    print("A classification report is used to evaluate the performance")
    print("of classification models like Logistic Regression, KNN,")
    print("Decision Tree etc.")

    print("\nIt shows important metrics like:")
    print("Precision")
    print("Recall")
    print("F1 Score")
    print("Support")

    print("\nIt helps us understand how well the model")
    print("is predicting each class.")

    print(border)


# ----------------------------------------------------------
# Q6 : Meaning of evaluation metrics
# ----------------------------------------------------------
def ExplainClassificationMetrics():

    border = "-" * 60
    print(border)
    print("Q6 : Meaning of Precision, Recall, F1 Score, Support, Accuracy")
    print(border)

    print("Precision : How many predicted positives are correct.")
    print("Recall : How many actual positives are correctly predicted.")
    print("F1 Score : Harmonic mean of precision and recall.")
    print("Support : Number of actual occurrences of each class.")
    print("Accuracy : Overall correctness of the model.")

    print(border)


# ----------------------------------------------------------
# Q7 : Calculate TP, TN, FP, FN
# ----------------------------------------------------------
def CalculateConfusionValues():

    border = "-" * 60
    print(border)
    print("Q7 : Calculate TP, TN, FP, FN")
    print(border)

    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]

    TP = TN = FP = FN = 0

    for a, p in zip(actual, predicted):

        if a == 1 and p == 1:
            TP += 1

        elif a == 0 and p == 0:
            TN += 1

        elif a == 0 and p == 1:
            FP += 1

        elif a == 1 and p == 0:
            FN += 1

    print("True Positive :", TP)
    print("True Negative :", TN)
    print("False Positive :", FP)
    print("False Negative :", FN)

    print(border)


# ----------------------------------------------------------
# Q8 : Same calculation again (explicit question)
# ----------------------------------------------------------
def DisplayConfusionMatrixValues():

    border = "-" * 60
    print(border)
    print("Q8 : Display TP, TN, FP, FN")
    print(border)

    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]

    TP = TN = FP = FN = 0

    for a, p in zip(actual, predicted):

        if a == 1 and p == 1:
            TP += 1
        elif a == 0 and p == 0:
            TN += 1
        elif a == 0 and p == 1:
            FP += 1
        elif a == 1 and p == 0:
            FN += 1

    print("TP :", TP)
    print("TN :", TN)
    print("FP :", FP)
    print("FN :", FN)

    print(border)


# ----------------------------------------------------------
# Q9 : Generate Classification Report
# ----------------------------------------------------------
def GenerateClassificationReport():

    border = "-" * 60
    print(border)
    print("Q9 : Generate Classification Report")
    print(border)

    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]

    report = classification_report(actual, predicted)

    print(report)

    print(border)



def main():

    CalculateDatasetMean()
    CalculateVarianceAndStd()
    PerformFeatureScaling()
    CalculateEuclideanDistance()
    ExplainClassificationReport()
    ExplainClassificationMetrics()
    CalculateConfusionValues()
    DisplayConfusionMatrixValues()
    GenerateClassificationReport()



if __name__ == "__main__":
    main()