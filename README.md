# Student Performance Analytics System

## 1. Project Title & Student Details
* **Project Title**: Student Performance Analytics System[cite: 1]
* **Student Name**: [Insert Your Full Name Here][cite: 3]
* **Course**: Python with AI - EWB Courses[cite: 1]
* **Submission Date**: October 2026[cite: 1]

---

## 2. Objective
The objective of this project is to build a Python-based data analytics system that processes student records, calculates totals and average marks, assigns letter grades, evaluates pass/fail status, and generates summary insights (such as class averages and top performers) using Pandas and NumPy[cite: 1, 2].

---

## 3. Technologies Used
* **Python**: Core programming language[cite: 1, 3]
* **Pandas**: Used for reading CSV datasets, structuring data into DataFrames, and filtering[cite: 1, 3, 4]
* **NumPy**: Used for efficient numerical calculations such as matrix operations, row sums, and column averages[cite: 1, 3, 4]

---

## 4. Dataset Description
The dataset (`student.csv`) contains student academic records with the following columns:
* `Student ID`: Unique identifier for each student[cite: 1, 2]
* `Name`: Full name of the student[cite: 1, 2]
* `Department`: Academic department (e.g., Computer Science, Data Science, IT)[cite: 1, 2]
* `Math`, `Science`, `English`: Marks scored out of 100 in each subject[cite: 1, 2]
* `Attendance`: Attendance percentage of each student[cite: 1, 2]

---

## 5. Implementation
1. **Data Loading**: Loaded `student.csv` into a Pandas DataFrame using `pd.read_csv()`[cite: 2].
2. **Data Processing**:
   * Converted subject mark columns into a NumPy array[cite: 1, 2].
   * Calculated `Total Marks` using `np.sum()` across columns[cite: 1, 2].
   * Calculated `Average Marks` using `np.mean()` across columns[cite: 1, 2].
3. **Logic & Grading**:
   * Assigned letter grades (`A`, `B`, `C`, `F`) based on average cutoffs using a custom function[cite: 1, 2].
   * Determined `Pass`/`Fail` status using conditions for both marks ($\ge 50$) and attendance ($\ge 75\%$)[cite: 1, 2].
4. **Data Export**: Exported the processed performance summary into `processed_students.csv`[cite: 2].

---

## 6. Key Features
* Automatic calculation of student total and average marks[cite: 1, 2]
* Grade assignment based on defined performance tiers[cite: 1, 2]
* Pass/Fail determination using attendance and mark criteria[cite: 1, 2]
* Class-wide statistical evaluation (Overall average, top performing student, subject-wise best average)[cite: 1, 2]
* Summary table printout and CSV export[cite: 2]

---

## 7. Final Outcome
The project successfully processes student records and outputs clear analytical summaries without errors[cite: 2, 3]. It eliminates manual grade calculations and generates immediate class-level statistics[cite: 1, 2].

---

## 8. Challenges & Learning
* **Challenges Faced**: Resolving file path errors (`FileNotFoundError`) and column key mismatches (`KeyError`)[cite: 2].
* **Key Learnings**: Learned how to integrate Pandas with NumPy for structured data manipulation and conditional data filtering in Python[cite: 1, 4].

---

## 9. GitHub Repository
* **Repository Link**: `[Paste your GitHub Repository URL here once created]`