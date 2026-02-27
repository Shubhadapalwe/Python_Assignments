# =========================================================
# Advanced Decision Tree Analysis - Student Performance ML
# =========================================================

import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix


# --------------------------------------------------
# 1️ Load Dataset
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "student_performance_ml.csv")

df = pd.read_csv("student_performance_ml.csv")

print("\nDataset Loaded Successfully")
print("Shape:", df.shape)


# --------------------------------------------------
# 2️ Prepare Features & Target
# --------------------------------------------------

features = ["StudyHours", "Attendance", "PreviousScore",
            "AssignmentsCompleted", "SleepHours"]

X = df[features]
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"\nInitial Model Accuracy: {accuracy*100:.2f}%")


# --------------------------------------------------
# 3️ Feature Importance
# --------------------------------------------------

print("\nFeature Importances:")
importances = model.feature_importances_

for name, score in zip(features, importances):
    print(f"{name} : {score:.4f}")

most_important = features[importances.argmax()]
least_important = features[importances.argmin()]

print("\nMost Important Feature:", most_important)
print("Least Important Feature:", least_important)


# --------------------------------------------------
# 4️ Remove SleepHours & Retrain
# --------------------------------------------------

print("\nRemoving SleepHours and retraining...")

features_without_sleep = ["StudyHours", "Attendance",
                          "PreviousScore", "AssignmentsCompleted"]

X2 = df[features_without_sleep]

X2_train, X2_test, y2_train, y2_test = train_test_split(
    X2, y, test_size=0.3, random_state=42
)

model2 = DecisionTreeClassifier(random_state=42)
model2.fit(X2_train, y2_train)

new_accuracy = accuracy_score(y2_test, model2.predict(X2_test))

print(f"New Accuracy without SleepHours: {new_accuracy*100:.2f}%")

if new_accuracy >= accuracy:
    print("Removing SleepHours did NOT reduce performance significantly.")
else:
    print("SleepHours contributes to model performance.")


# --------------------------------------------------
# 5️ Train using only StudyHours & Attendance
# --------------------------------------------------

print("\nTraining using only StudyHours and Attendance")

X_small = df[["StudyHours", "Attendance"]]

Xs_train, Xs_test, ys_train, ys_test = train_test_split(
    X_small, y, test_size=0.3, random_state=42
)

model_small = DecisionTreeClassifier(random_state=42)
model_small.fit(Xs_train, ys_train)

small_accuracy = accuracy_score(ys_test, model_small.predict(Xs_test))

print(f"Accuracy with only 2 features: {small_accuracy*100:.2f}%")


# --------------------------------------------------
# 6️ Predict for 5 New Students
# --------------------------------------------------

print("\nPredicting for 5 New Students")

new_students = pd.DataFrame({
    "StudyHours": [2, 6, 4, 8, 5],
    "Attendance": [60, 85, 75, 95, 80],
    "PreviousScore": [40, 70, 55, 78, 60],
    "AssignmentsCompleted": [2, 7, 5, 9, 6],
    "SleepHours": [5, 7, 6, 8, 7]
})

predictions = model.predict(new_students)

new_students["PredictedResult"] = predictions
print(new_students)


# --------------------------------------------------
# 7️ Manual Accuracy Calculation
# --------------------------------------------------

print("\nManual Accuracy Calculation")

correct = (y_test.values == y_pred).sum()
manual_accuracy = correct / len(y_test)

print("Manual Accuracy:", manual_accuracy*100)
print("Sklearn Accuracy:", accuracy*100)


# --------------------------------------------------
# 8️ Misclassified Students
# --------------------------------------------------

print("\nMisclassified Students")

misclassified = X_test[y_test != y_pred]
print(misclassified)
print("Number of Misclassified:", len(misclassified))


# --------------------------------------------------
# Compare Different random_state
# --------------------------------------------------

print("\nComparing Different random_state values")

for rs in [0, 10, 42]:
    temp_model = DecisionTreeClassifier(random_state=rs)
    temp_model.fit(X_train, y_train)
    temp_acc = accuracy_score(y_test, temp_model.predict(X_test))
    print(f"random_state={rs} → Accuracy: {temp_acc*100:.2f}%")


# --------------------------------------------------
#  Decision Tree Visualization
# --------------------------------------------------

plt.figure(figsize=(12, 8))
plot_tree(model,
          feature_names=features,
          class_names=["Fail", "Pass"],
          filled=True)
plt.title("Decision Tree Visualization")
plt.show()


# --------------------------------------------------
#  Add PerformanceIndex Column
# --------------------------------------------------

print("\nAdding PerformanceIndex column")

df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

X_new = df[["StudyHours", "Attendance", "PreviousScore",
            "AssignmentsCompleted", "SleepHours", "PerformanceIndex"]]

Xn_train, Xn_test, yn_train, yn_test = train_test_split(
    X_new, y, test_size=0.3, random_state=42
)

model_new = DecisionTreeClassifier(random_state=42)
model_new.fit(Xn_train, yn_train)

new_feature_accuracy = accuracy_score(yn_test, model_new.predict(Xn_test))

print(f"Accuracy with PerformanceIndex: {new_feature_accuracy*100:.2f}%")


# --------------------------------------------------
#  max_depth=None Model
# --------------------------------------------------

print("\nTraining model with max_depth=None")

deep_model = DecisionTreeClassifier(max_depth=None, random_state=42)
deep_model.fit(X_train, y_train)

train_acc = accuracy_score(y_train, deep_model.predict(X_train))
test_acc = accuracy_score(y_test, deep_model.predict(X_test))

print(f"Training Accuracy: {train_acc*100:.2f}%")
print(f"Testing Accuracy : {test_acc*100:.2f}%")

if train_acc == 1.0 and test_acc < train_acc:
    print("This is Overfitting: Model memorized training data.")