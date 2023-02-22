# 1.student.mark.py

# Function to input number of students in class and their information
def input_students():
    num_students = int(input("Enter the number of students in the class: "))
    for i in range(num_students):
        student_id = input(f"Enter student {i+1} ID: ")
        student_name = input(f"Enter student {i+1} name: ")
        student_dob = input(f"Enter student {i+1} date of birth (DD/MM/YYYY): ")
        student_info = (student_id, student_name, student_dob)
        students.append(student_info)

# Function to input number of courses and their information
def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    for i in range(num_courses):
        course_id = input(f"Enter course {i+1} ID: ")
        course_name = input(f"Enter course {i+1} name: ")
        course_info = (course_id, course_name)
        courses.append(course_info)

# Function to select a course and input marks for students in that course
def input_marks():
    print("Select a course to input marks for students:")
    for i, course in enumerate(courses):
        print(f"{i+1}. {course[1]}")
    course_index = int(input("Enter the number of the course: ")) - 1
    selected_course = courses[course_index]
    for student in students:
        student_id = student[0]
        mark = int(input(f"Enter mark for student {student_id} in course {selected_course[1]}: "))
        if selected_course not in marks:
            marks[selected_course] = {}
        marks[selected_course][student_id] = mark

# Function to list all courses
def list_courses():
    print("List of courses:")
    print("{:<12}{}".format("Course ID", "Course Name"))
    print("{:<12}{}".format("---------", "-----------"))
    for i, course in enumerate(courses):
        print(f"{course[0]:<12}{course[1]}")

# Function to list all students
def list_students():
    print("List of students:")
    print("{:<12}{:<15}{}".format("Student ID", "Name", "Date of Birth"))
    print("{:<12}{:<15}{}".format("----------", "----", "-------------"))
    for student in students:
        print(f"{student[0]:<12}{student[1]:<15}{student[2]}")

# Function to show marks for a given course
def show_marks():
    print("Select a course to show marks:")
    for i, course in enumerate(courses):
        print(f"{i+1}. {course[1]}")
    course_index = int(input("Enter the number of the course: ")) - 1
    selected_course = courses[course_index]
    print(f"Marks for course {selected_course[1]}:")
    if selected_course in marks:
        for student in students:
            student_id = student[0]
            if student_id in marks[selected_course]:
                mark = marks[selected_course][student_id]
                print(f"{student_id} - {student[1]}: {mark}")
            else:
                print(f"{student_id} - {student[1]}: No mark")
    else:
        print("No marks for this course.")

# Main program
if __name__=="__main__":
    students = []
    courses = []
    marks = {}
    
    while True:
        print("\nStudent Mark Management System\n")
        print("1. Input number of students and their information")
        print("2. Input number of courses and their information")
        print("3. Select a course to input marks for students")
        print("4. List all courses")
        print("5. List all students")
        print("6. Show marks for a given course")
        print("7. Exit\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            input_students()
        elif choice == 2:
            input_courses()
        elif choice == 3:
            input_marks()
        elif choice == 4:
            list_courses()
        elif choice == 5:
            list_students()
        elif choice == 6:
            show_marks()
        elif choice == 7:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

