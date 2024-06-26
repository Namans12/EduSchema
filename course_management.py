from db_connection import create_connection

def add_course(course_name, description, duration, level):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Courses (CourseName, CourseDescription, CourseDuration, CourseLevel) VALUES (%s, %s, %s, %s)", 
                   (course_name, description, duration, level))
    connection.commit()
    cursor.close()
    connection.close()
    print("Course added successfully.")

def update_course(course_id, course_name, description, duration, level):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Courses SET CourseName=%s, CourseDescription=%s, CourseDuration=%s, CourseLevel=%s WHERE CourseID=%s",
                   (course_name, description, duration, level, course_id))
    connection.commit()
    cursor.close()
    connection.close()
    print("Course updated successfully.")

def remove_course(course_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Courses WHERE CourseID=%s", (course_id,))
    connection.commit()
    cursor.close()
    connection.close()
    print("Course removed successfully.")

def search_courses(keyword):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Courses WHERE CourseName LIKE %s", (f"%{keyword}%",))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

def sort_courses(by_column):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Courses ORDER BY {by_column}")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results