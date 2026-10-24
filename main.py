"""Main program: Student Performance Analytics System."""

import os
import numpy as np
import pandas as pd
from functions import SUBJECTS, add_student_analysis


INPUT_FILE = "students.csv"
OUTPUT_FILE = "student_analysis_results.csv"
REQUIRED_COLUMNS = [
    "StudentID", "Name", "Department",
    "Python", "Maths", "AI", "Attendance"
]


def load_data(filename):
    """Load the CSV and check that it has the required columns."""
    if not os.path.exists(filename):
        raise FileNotFoundError(
            f"Could not find '{filename}'. Put it in the same folder as main.py."
        )

    data = pd.read_csv(filename)
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in data.columns]
    if missing_columns:
        raise ValueError(f"Missing required column(s): {', '.join(missing_columns)}")

    if data.empty:
        raise ValueError("The dataset is empty. Add student records to students.csv.")

    # Ensure marks and attendance are numeric and within the expected range.
    for column in SUBJECTS + ["Attendance"]:
        data[column] = pd.to_numeric(data[column], errors="raise")
        if ((data[column] < 0) | (data[column] > 100)).any():
            raise ValueError(f"Values in '{column}' must be between 0 and 100.")

    return data


def show_student_results(data):
    """Print each student's total, average, grade, and pass/fail result."""
    columns = ["StudentID", "Name", "Department", "Total", "Average", "Grade", "Result"]
    print("\n===== INDIVIDUAL STUDENT RESULTS =====")
    print(data[columns].to_string(index=False))


def show_class_summary(data):
    """Print overall statistics calculated with NumPy."""
    averages = data["Average"].to_numpy()
    print("\n===== CLASS PERFORMANCE =====")
    print(f"Number of students: {len(data)}")
    print(f"Overall class average: {np.mean(averages):.2f}")
    print(f"Highest student average: {np.max(averages):.2f}")
    print(f"Lowest student average: {np.min(averages):.2f}")


def show_subject_analysis(data):
    """Print the average, highest mark, and lowest mark for each subject."""
    print("\n===== SUBJECT-WISE ANALYSIS =====")
    subject_averages = data[SUBJECTS].mean()

    for subject in SUBJECTS:
        print(
            f"{subject}: average = {subject_averages[subject]:.2f}, "
            f"highest = {data[subject].max()}, lowest = {data[subject].min()}"
        )

    best_subject = subject_averages.idxmax()
    print(f"Best-performing subject by average: {best_subject}")


def show_pass_fail_statistics(data):
    """Count students who passed and failed."""
    pass_count = int((data["Result"] == "Pass").sum())
    fail_count = int((data["Result"] == "Fail").sum())

    print("\n===== PASS/FAIL STATISTICS =====")
    print(f"Students passed: {pass_count}")
    print(f"Students failed: {fail_count}")


def show_top_performers(data):
    """Display the three students with the highest averages."""
    top_students = data.nlargest(3, "Average")
    columns = ["StudentID", "Name", "Department", "Average", "Grade", "Result"]

    print("\n===== TOP 3 PERFORMERS =====")
    print(top_students[columns].to_string(index=False))


def show_department_analysis(data):
    """Compare average marks by department."""
    print("\n===== DEPARTMENT-WISE ANALYSIS =====")
    department_averages = data.groupby("Department")[SUBJECTS].mean().round(2)
    print(department_averages.to_string())


def main():
    """Run all steps of the project."""
    print("=" * 58)
    print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 58)

    try:
        students = load_data(INPUT_FILE)
        print(f"\nDataset loaded successfully: {len(students)} student records.")
        print("\n===== DATASET PREVIEW =====")
        print(students.head().to_string(index=False))

        analyzed_students = add_student_analysis(students)

        show_student_results(analyzed_students)
        show_class_summary(analyzed_students)
        show_subject_analysis(analyzed_students)
        show_pass_fail_statistics(analyzed_students)
        show_top_performers(analyzed_students)
        show_department_analysis(analyzed_students)

        analyzed_students.to_csv(OUTPUT_FILE, index=False)
        print(f"\nAnalysis completed successfully.")
        print(f"Full results saved to '{OUTPUT_FILE}'.")

    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        print(f"\nERROR: {error}")
        print("Please check the dataset and try again.")


if __name__ == "__main__":
    main()
