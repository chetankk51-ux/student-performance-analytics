import numpy as np
import pandas as pd

def calculate_grade(avg):
    """Assigns letter grades based on average marks."""
    if avg >= 85:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'F'

def main():
    print("=== STUDENT PERFORMANCE ANALYTICS SYSTEM ===")
    
    # Step 1: Read the data using Pandas
    try:
        df = pd.read_csv('student.csv')
    except FileNotFoundError:
        print("Error: 'students.csv' file not found. Please create it first.")
        return

    print("\n--- Raw Data Overview ---")
    print(f"Total Records Loaded: {len(df)}")
    print(df.head())

    # Step 2: Process Data (Calculate Totals and Averages using NumPy)
    subject_columns = ['Math', 'Science', 'English']
    
    # Convert marks to a NumPy array for fast numerical calculations
    marks_matrix = df[subject_columns].to_numpy()
    
    # Calculate Total and Average per student
    df['Total Marks'] = np.sum(marks_matrix, axis=1)
    df['Average Marks'] = np.mean(marks_matrix, axis=1)

    # Step 3: Assign Grades and Pass/Fail Status
    df['Grade'] = df['Average Marks'].apply(calculate_grade)
    # Passing condition: Average marks >= 50 and Attendance >= 75
    df['Status'] = np.where((df['Average Marks'] >= 50) & (df['Attendance'] >= 75), 'Pass', 'Fail')

    # Step 4: Perform Practical Analysis
    print("\n--- Performance Analysis ---")
    
    # Overall class average
    class_avg = np.mean(df['Average Marks'])
    print(f"Overall Class Average Mark: {class_avg:.2f}")

    # Highest average student
    top_student_idx = df['Average Marks'].idxmax()
    top_student = df.loc[top_student_idx]
    print(f"Top Performing Student: {top_student['Name']} (Average: {top_student['Average Marks']:.2f})")

    # Subject-wise best average
    subject_averages = df[subject_columns].mean()
    best_subject = subject_averages.idxmax()
    print(f"Subject with Best Average: {best_subject} ({subject_averages[best_subject]:.2f})")

    # Pass/Fail statistics
    pass_count = (df['Status'] == 'Pass').sum()
    fail_count = (df['Status'] == 'Fail').sum()
    print(f"Students Passed: {pass_count} | Students Failed: {fail_count}")

    # Display processed dataframe summary
    print("\n--- Final Processed Data Summary ---")
    print(df[['Student ID', 'Name', 'Total Marks', 'Average Marks', 'Grade', 'Status']])

    # Export processed data if needed
    df.to_csv('processed_students.csv', index=False)
    print("\nProcessed data successfully saved to 'processed_students.csv'.")

if __name__ == "__main__":
    main()