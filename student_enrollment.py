# student_enrollment.py

from db_connection import create_connection

def enroll_student(first_name, last_name, email):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Students (FirstName, LastName, Email) VALUES (%s, %s, %s)", 
                   (first_name, last_name, email))
    connection.commit()
    cursor.close()
    connection.close()
    print("Student enrolled successfully.")

def register_student(course_id, student_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Enrollments (StudentID, CourseID) VALUES (%s, %s)", 
                   (student_id, course_id))
    connection.commit()
    cursor.close()
    connection.close()
    print("Student registered to course successfully.")

def update_progress(enrollment_id, progress):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Enrollments SET Progress=%s WHERE EnrollmentID=%s", 
                   (progress, enrollment_id))
    connection.commit()
    cursor.close()
    connection.close()
    print("Progress updated successfully.")
