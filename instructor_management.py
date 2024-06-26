# instructor_management.py

from db_connection import create_connection

def add_instructor(first_name, last_name, email, bio):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Instructors (FirstName, LastName, Email, Bio) VALUES (%s, %s, %s, %s)", 
                   (first_name, last_name, email, bio))
    connection.commit()
    cursor.close()
    connection.close()
    print("Instructor added successfully.")

def update_instructor(instructor_id, first_name, last_name, email, bio):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Instructors SET FirstName=%s, LastName=%s, Email=%s, Bio=%s WHERE InstructorID=%s",
                   (first_name, last_name, email, bio, instructor_id))
    connection.commit()
    cursor.close()
    connection.close()
    print("Instructor updated successfully.")

def remove_instructor(instructor_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Instructors WHERE InstructorID=%s", (instructor_id,))
    connection.commit()
    cursor.close()
    connection.close()
    print("Instructor removed successfully.")

def assign_instructor(course_id, instructor_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Course_Instructors (CourseID, InstructorID) VALUES (%s, %s)", 
                   (course_id, instructor_id))
    connection.commit()
    cursor.close()
    connection.close()
    print("Instructor assigned to course successfully.")
