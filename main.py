from course_management import add_course, update_course, remove_course, search_courses, sort_courses
from instructor_management import add_instructor, update_instructor, remove_instructor, assign_instructor
from student_enrollment import enroll_student, register_student, update_progress
from assessment_and_grades import create_assessment, input_grade, view_grades

def main():
    while True:
        print("\nWelcome to EduSchema")
        print("1. Course Management")
        print("2. Instructor Management")
        print("3. Student Enrollment")
        print("4. Assessment and Grades")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nCourse Management")
            print("1. Add Course")
            print("2. Update Course")
            print("3. Remove Course")
            print("4. Search Courses")
            print("5. Sort Courses")
            course_choice = input("Enter your choice: ")

            if course_choice == '1':
                course_name = input("Enter course name: ")
                description = input("Enter course description: ")
                duration = int(input("Enter course duration (weeks): "))
                level = input("Enter course level: ")
                add_course(course_name, description, duration, level)
            elif course_choice == '2':
                course_id = int(input("Enter course ID to update: "))
                course_name = input("Enter new course name: ")
                description = input("Enter new course description: ")
                duration = int(input("Enter new course duration (weeks): "))
                level = input("Enter new course level: ")
                update_course(course_id, course_name, description, duration, level)
            elif course_choice == '3':
                course_id = int(input("Enter course ID to remove: "))
                remove_course(course_id)
            elif course_choice == '4':
                keyword = input("Enter keyword to search courses: ")
                results = search_courses(keyword)
                for row in results:
                    print(row)
            elif course_choice == '5':
                by_column = input("Enter column name to sort by (CourseName, CourseDuration, etc.): ")
                results = sort_courses(by_column)
                for row in results:
                    print(row)

        elif choice == '2':
            print("\nInstructor Management")
            print("1. Add Instructor")
            print("2. Update Instructor")
            print("3. Remove Instructor")
            print("4. Assign Instructor to Course")
            instructor_choice = input("Enter your choice: ")

            if instructor_choice == '1':
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                email = input("Enter email: ")
                bio = input("Enter bio: ")
                add_instructor(first_name, last_name, email, bio)
            elif instructor_choice == '2':
                instructor_id = int(input("Enter instructor ID to update: "))
                first_name = input("Enter new first name: ")
                last_name = input("Enter new last name: ")
                email = input("Enter new email: ")
                bio = input("Enter new bio: ")
