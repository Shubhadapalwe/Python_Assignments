# ============================================
# Student Performance ML - Decision Tree Model
# ============================================

import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# --------------------------------------------------
# Step 1: Load Dataset
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "student_performance_ml.csv")

df = pd.read_csv("student_performance_ml.csv")

print("\nDataset Loaded Successfully")
print("Shape:", df.shape)
print(df.head())

# --------------------------------------------------
# Step 2: Data Preparation
# --------------------------------------------------

X = df[["StudyHours", "Attendance", "PreviousScore",
        "AssignmentsCompleted", "SleepHours"]]

y = df["FinalResult"]

# --------------------------------------------------
# Step 3: Train-Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("\nTraining size:", X_train.shape)
print("Testing size:", X_test.shape)

# --------------------------------------------------
# Step 4: Train Decision Tree Model
# --------------------------------------------------

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

print("\nModel Trained Successfully")

# --------------------------------------------------
# Step 5: Prediction
# --------------------------------------------------

y_pred = model.predict(X_test)

print("\nPredicted values:", y_pred)
print("Actual values   :", y_test.values)

# --------------------------------------------------
# Step 6: Accuracy Calculation
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# --------------------------------------------------
# Step 7: Confusion Matrix
# --------------------------------------------------

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.title("Confusion Matrix")
plt.show()

print("\nExplanation:")
print("TP = Correctly predicted Pass")
print("TN = Correctly predicted Fail")
print("FP = Predicted Pass but actually Fail")
print("FN = Predicted Fail but actually Pass")

# --------------------------------------------------
# Step 8: Training vs Testing Accuracy (Overfitting Check)
# --------------------------------------------------

train_accuracy = accuracy_score(y_train, model.predict(X_train))
test_accuracy = accuracy_score(y_test, y_pred)

print(f"\nTraining Accuracy: {train_accuracy * 100:.2f}%")
print(f"Testing Accuracy : {test_accuracy * 100:.2f}%")

if train_accuracy > test_accuracy + 0.1:
    print("Model may be Overfitting")
elif train_accuracy < test_accuracy - 0.1:
    print("Model may be Underfitting")
else:
    print("Model seems balanced")

# --------------------------------------------------
# Step 9: Compare Different max_depth
# --------------------------------------------------

print("\nComparing different max_depth values")

for depth in [1, 3, None]:
    temp_model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    temp_model.fit(X_train, y_train)
    temp_pred = temp_model.predict(X_test)
    temp_acc = accuracy_score(y_test, temp_pred)
    print(f"max_depth={depth} → Testing Accuracy: {temp_acc * 100:.2f}%")

# --------------------------------------------------
# Step 10: Predict for New Student
# --------------------------------------------------

new_student = pd.DataFrame({
    "StudyHours": [6],
    "Attendance": [85],
    "PreviousScore": [66],
    "AssignmentsCompleted": [7],
    "SleepHours": [7]
})

prediction = model.predict(new_student)

print("\nPrediction for New Student:")
print("Input:", new_student.iloc[0].to_dict())

if prediction[0] == 1:
    print("Result: PASS")
else:
    print("Result: FAIL")

print("\nProgram Completed Successfully")