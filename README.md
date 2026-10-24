# Student Performance Analytics System

A beginner-friendly Python data-analysis project that reads student records from a CSV file and analyzes their marks and attendance using Python, Pandas, and NumPy.

## Features

- Loads and validates student data from `students.csv`
- Calculates each student's total and average marks
- Assigns grades using a clearly defined grading scale
- Determines Pass/Fail status using subject marks and attendance
- Reports class average, highest average, and lowest average
- Reports subject-wise average, highest mark, and lowest mark
- Identifies the best-performing subject by average
- Counts pass and fail students
- Displays the top three students by average
- Compares average marks by department
- Exports the analysis to `student_analysis_results.csv`

## Technologies

- Python 3
- Pandas
- NumPy

## Project files

- `main.py` — main program and analysis report
- `functions.py` — reusable functions and grading/pass rules
- `students.csv` — input dataset containing 20 sample student records
- `student_analysis_results.csv` — generated after running the program
- `Project_Documentation.docx` — project report template/description
- `screenshots/` — place screenshots of your actual program output here

## Setup

1. Install Python 3.
2. Open this folder in VS Code.
3. Open Terminal → New Terminal.
4. Install the dependencies:

   ```bash
   python -m pip install pandas numpy
   ```

5. Run the program:

   ```bash
   python main.py
   ```

   On some Windows setups, use `py main.py`.

## Rules used in this sample

### Grades

- A: average >= 90
- B: average >= 80 and < 90
- C: average >= 70 and < 80
- D: average >= 60 and < 70
- F: average < 60

### Pass/Fail

A student passes only when they score at least 40 in every subject and have at least 75% attendance. These are sample project rules; confirm or change them if your trainer has provided different rules.

## Output

The program prints the analysis in the terminal and creates `student_analysis_results.csv` with the original data plus Total, Average, Grade, and Result columns.

## Before submitting

- Run the program and confirm it completes without errors.
- Inspect the generated CSV.
- Add screenshots of your actual output to `screenshots/`.
- Replace any placeholder student details in the documentation with your own.
- Create a GitHub repository and upload the project files.
- Add your actual GitHub repository URL to your documentation and submit it using the Google Form provided by your trainer.
