

import sys
import pandas as pd
import matplotlib.pyplot as plt


# Change this if your CSV is in a different location
CSV_PATH = "student_performance_ml.csv"


def load_df(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print(f"ERROR: CSV file not found at: {path}")
        print("Fix: Put CSV in same folder OR update CSV_PATH in the script.")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Could not read CSV: {e}")
        sys.exit(1)

    required_cols = {
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours",
        "FinalResult",
    }
    missing = required_cols - set(df.columns)
    if missing:
        print(f"ERROR: Missing required columns: {sorted(missing)}")
        print("Columns found:", df.columns.tolist())
        sys.exit(1)

    return df


# -----------------------------
# Q1
# -----------------------------
def q1_basic_info(df: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print("Q1) Load CSV + Display basic information")
    print("=" * 60)

    print("\nFirst 5 records:\n", df.head())
    print("\nLast 5 records:\n", df.tail())
    print("\nTotal number of rows and columns:", df.shape)
    print("\nList of column names:", df.columns.tolist())
    print("\nData types of each column:\n", df.dtypes)


# -----------------------------
# Q2
# -----------------------------
def q2_student_counts(df: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print("Q2) Total students + Passed + Failed")
    print("=" * 60)

    total_students = len(df)
    passed = (df["FinalResult"] == 1).sum()
    failed = (df["FinalResult"] == 0).sum()

    print("Total students:", total_students)
    print("Passed students (FinalResult=1):", passed)
    print("Failed students (FinalResult=0):", failed)


# -----------------------------
# Q3
# -----------------------------
def q3_stats(df: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print("Q3) Pandas calculations")
    print("=" * 60)

    print("Average StudyHours:", df["StudyHours"].mean())
    print("Average Attendance:", df["Attendance"].mean())
    print("Maximum PreviousScore:", df["PreviousScore"].max())
    print("Minimum SleepHours:", df["SleepHours"].min())


# -----------------------------
# Q4
# -----------------------------
def q4_distribution(df: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print("Q4) Distribution of FinalResult + Percentage + Balanced?")
    print("=" * 60)

    counts = df["FinalResult"].value_counts()
    percent = df["FinalResult"].value_counts(normalize=True) * 100

    print("Counts:\n", counts)
    print("\nPercentages:\n", percent)

    pass_pct = float(percent.get(1, 0))
    fail_pct = float(percent.get(0, 0))

    print(f"\nPass % = {pass_pct:.2f}%")
    print(f"Fail % = {fail_pct:.2f}%")

    # Simple balance rule: if difference <= 10%, consider "fairly balanced"
    if abs(pass_pct - fail_pct) <= 10:
        print("Dataset is fairly balanced.")
    else:
        print("Dataset is slightly imbalanced (more Pass or more Fail).")


# -----------------------------
# Q5
# -----------------------------
def q5_analysis(df: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print("Q5) Analyze: StudyHours & Attendance effect on FinalResult")
    print("=" * 60)

    means = df.groupby("FinalResult")[["StudyHours", "Attendance"]].mean()
    print("Mean values for Fail(0) vs Pass(1):\n")
    print(means)

    print("\nObservation (write 4-5 lines):")
    print("1) Compare mean StudyHours for FinalResult=1 vs FinalResult=0.")
    print("2) If StudyHours mean is higher for Pass, then higher StudyHours increases chance of passing.")
    print("3) Compare mean Attendance for FinalResult=1 vs FinalResult=0.")
    print("4) If Attendance mean is higher for Pass, then higher Attendance improves FinalResult.")
    print("5) So StudyHours and Attendance together strongly influence passing.")


# -----------------------------
# Q6
# -----------------------------
def q6_hist_studyhours(df: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print("Q6) Histogram of StudyHours")
    print("=" * 60)

    plt.figure()
    plt.hist(df["StudyHours"])
    plt.title("Histogram of StudyHours")
    plt.xlabel("StudyHours")
    plt.ylabel("Frequency")
    plt.show()


# -----------------------------
# Q7
# -----------------------------
def q7_scatter_study_vs_prevscore(df: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print("Q7) Scatter plot: StudyHours vs PreviousScore (Pass vs Fail)")
    print("=" * 60)

    passed = df[df["FinalResult"] == 1]
    failed = df[df["FinalResult"] == 0]

    plt.figure()
    plt.scatter(passed["StudyHours"], passed["PreviousScore"], label="Pass (1)")
    plt.scatter(failed["StudyHours"], failed["PreviousScore"], label="Fail (0)")
    plt.title("StudyHours vs PreviousScore")
    plt.xlabel("StudyHours")
    plt.ylabel("PreviousScore")
    plt.legend()
    plt.show()


# -----------------------------
# Q8
# -----------------------------
def q8_boxplot_attendance_and_outliers(df: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print("Q8) Boxplot for Attendance + Outliers")
    print("=" * 60)

    plt.figure()
    plt.boxplot(df["Attendance"])
    plt.title("Boxplot of Attendance")
    plt.ylabel("Attendance")
    plt.show()

    # IQR outlier detection
    Q1 = df["Attendance"].quantile(0.25)
    Q3 = df["Attendance"].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df["Attendance"] < lower) | (df["Attendance"] > upper)]
    if outliers.empty:
        print("No outliers detected in Attendance using IQR method.")
    else:
        print("Outliers detected in Attendance:\n", outliers)


# -----------------------------
# Q9
# -----------------------------
def q9_assignments_vs_finalresult(df: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print("Q9) Relationship: AssignmentsCompleted vs FinalResult")
    print("=" * 60)

    plt.figure()
    plt.scatter(df["AssignmentsCompleted"], df["FinalResult"])
    plt.title("AssignmentsCompleted vs FinalResult")
    plt.xlabel("AssignmentsCompleted")
    plt.ylabel("FinalResult (0=Fail, 1=Pass)")
    plt.yticks([0, 1])
    plt.show()

    print("\nMean AssignmentsCompleted by FinalResult:")
    print(df.groupby("FinalResult")["AssignmentsCompleted"].mean())
    print("\nObservation: If mean is higher for Pass group, assignments help improve FinalResult.")


# -----------------------------
# Q10
# -----------------------------
def q10_sleephours_vs_finalresult(df: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print("Q10) SleepHours vs FinalResult + Conclusion")
    print("=" * 60)

    plt.figure()
    plt.scatter(df["SleepHours"], df["FinalResult"])
    plt.title("SleepHours vs FinalResult")
    plt.xlabel("SleepHours")
    plt.ylabel("FinalResult (0=Fail, 1=Pass)")
    plt.yticks([0, 1])
    plt.show()

    print("\nMean SleepHours by FinalResult:")
    print(df.groupby("FinalResult")["SleepHours"].mean())

    print("\nConclusion:")
    print("Sleep helps, but if pass and fail students overlap in sleep hours,")
    print("then sleeping more alone does not guarantee success. Other factors matter.")


def main():
    df = load_df(CSV_PATH)

    # Run all questions sequentially
    q1_basic_info(df)
    q2_student_counts(df)
    q3_stats(df)
    q4_distribution(df)
    q5_analysis(df)
    q6_hist_studyhours(df)
    q7_scatter_study_vs_prevscore(df)
    q8_boxplot_attendance_and_outliers(df)
    q9_assignments_vs_finalresult(df)
    q10_sleephours_vs_finalresult(df)

    print("\nAll questions executed successfully.")


if __name__ == "__main__":
    main()