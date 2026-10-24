"""Reusable functions for the Student Performance Analytics System."""

SUBJECTS = ["Python", "Maths", "AI"]
PASS_MARK = 40
MIN_ATTENDANCE = 75


def assign_grade(average):
    """Return a letter grade based on the student's average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def check_result(row):
    """Return Pass only if every subject mark and attendance meet the rules."""
    for subject in SUBJECTS:
        if row[subject] < PASS_MARK:
            return "Fail"

    if row["Attendance"] < MIN_ATTENDANCE:
        return "Fail"

    return "Pass"


def add_student_analysis(data):
    """Return a copy of the data with total, average, grade, and result columns."""
    result = data.copy()
    result["Total"] = result[SUBJECTS].sum(axis=1)
    result["Average"] = result[SUBJECTS].mean(axis=1).round(2)
    result["Grade"] = result["Average"].apply(assign_grade)
    result["Result"] = result.apply(check_result, axis=1)
    return result
