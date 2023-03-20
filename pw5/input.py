import math
import os
from domains import *

class Input:
    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        file_exist = os.path.isfile("./students.txt")
        f = open("students.txt", "a")
        if not file_exist:
            f.write("List of students:\n")
            f.write("{:<12}{:<15}{}\n".format("Student ID", "Name", "Date of Birth"))
            f.write("{:<12}{:<15}{}\n".format("----------", "----", "-------------"))
        for i in range(num_students):
            student_id = input(f"Enter student {i+1} ID: ")
            student_name = input(f"Enter student {i+1} name: ")
            student_dob = input(f"Enter student {i+1} date of birth (DD/MM/YYYY): ")
            student_info = Student(student_id, student_name, student_dob)
            self.students.append(student_info)
            f.write(f"{student_id:<12}{student_name:<15}{student_dob}\n")
        f.close()

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        file_exist = os.path.isfile("./courses.txt")
        f = open("courses.txt", "a")
        if not file_exist:
            f.write("List of courses:\n")
            f.write("{:<12}{:<12}{}\n".format("Course ID", "Course Name", "No. credits"))
            f.write("{:<12}{:<12}{}\n".format("---------", "-----------", "-----------"))
        for i in range(num_courses):
            course_id = input(f"Enter course {i+1} ID: ")
            course_name = input(f"Enter course {i+1} name: ")
            course_credit = int(input(f"Enter course {i+1} number of credits: "))
            course_info = Course(course_id, course_name, course_credit)
            self.courses.append(course_info)
            f.write(f"{course_id:<12}{course_name:<12}{course_credit}\n")
        f.close()

    def input_marks(self):
        file_exist = os.path.isfile("./marks.txt")
        f = open("marks.txt", "a")
        if not file_exist:
            f.write("Marks:\n")
            f.write("{:<12}{:<15}{:<15}{}\n".format("Student Id", "Student Name", "Course Name", "Mark"))
            f.write("{:<12}{:<15}{:<15}{}\n".format("----------", "------------", "-----------", "----"))
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
            f.write(f"{student.id:<12}{student.name:<15}{selected_course.name:<15}{mark.get_mark()}\n")
        f.close()            