import math
from domains import *

class Input:
    def input_students(self):
        num_students = int(input("Enter the number of students in the class: "))
        for i in range(num_students):
            student_id = input(f"Enter student {i+1} ID: ")
            student_name = input(f"Enter student {i+1} name: ")
            student_dob = input(f"Enter student {i+1} date of birth (DD/MM/YYYY): ")
            student_info = Student(student_id, student_name, student_dob)
            self.students.append(student_info)

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for i in range(num_courses):
            course_id = input(f"Enter course {i+1} ID: ")
            course_name = input(f"Enter course {i+1} name: ")
            course_credit = int(input(f"Enter course {i+1} number of credits: "))
            course_info = Course(course_id, course_name, course_credit)
            self.courses.append(course_info)

    def input_marks(self):
        print("Select a course to input marks for students:")
        for i, course in enumerate(self.courses):
            print(f"{i+1}. {course.name}")
        course_index = int(input("Enter the course number: ")) - 1
        selected_course = self.courses[course_index]
        for student in self.students:
            mark = float(input(f"Enter mark for student {student.name} in course {selected_course.name}: "))
            mark = math.floor(mark * 10) / 10
            mark = Mark(student, selected_course, mark)
            self.marks.append(mark)