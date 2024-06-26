# assessment_and_grades.py

from db_connection import create_connection

def create_assessment(course_id, assessment_name, max_score):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Assessments (CourseID, AssessmentName, MaxScore) VALUES (%s, %s, %s)", 
                   (course_id, assessment_name, max_score))
    connection.commit()
    cursor.close()
    connection.close()
    print("Assessment created successfully.")

def input_grade(enrollment_id, assessment_id, score):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Grades (EnrollmentID, AssessmentID, Score) VALUES (%s, %s, %s)", 
                   (enrollment_id, assessment_id, score))
    connection.commit()
    cursor.close()
    connection.close()
    print("Grade inputted successfully.")

def view_grades(enrollment_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Grades WHERE EnrollmentID=%s", (enrollment_id,))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results
