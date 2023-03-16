import math
import numpy as np
from domains import Student, Course, Mark

class StudentMarkSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []
        
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

    def list_courses(self):
        print("List of courses:")
        print("{:<12}{:<12}{}".format("Course ID", "Course Name", "No. credits"))
        print("{:<12}{:<12}{}".format("---------", "-----------", "-----------"))
        for course in self.courses:
            print(course)

    def list_students(self):
        print("List of students:")
        print("{:<12}{:<15}{}".format("Student ID", "Name", "Date of Birth"))
        print("{:<12}{:<15}{}".format("----------", "----", "-------------"))
        for student in self.students:
            print(student)

    def show_marks(self):
        print("Select a course to show marks:")
        for i, course in enumerate(self.courses):
            print(f"{i+1}. {course.name}")
        course_index = int(input("Enter the number of the course: ")) - 1
        selected_course = self.courses[course_index]
        print(f"Marks for course {selected_course.name}:")
        for mark in self.marks:
            if mark.get_course() == selected_course:
                student_id = mark.get_student().id
                student_name = mark.get_student().name
                mark_value = mark.get_mark()
                print(f"{student_id} - {student_name}: {mark_value}")
        if not any(mark.get_course() == selected_course for mark in self.marks):
            print("No marks for this course.")

    def show_GPAs(self):
        GPAs = [] 
        for student in self.students:
            scores_list = []
            credits_list = []
            data = {}
            for mark in self.marks:
                if mark.get_student().id == student.id:
                    scores_list.append(mark.get_mark())
                    credits_list.append(mark.get_course().credit)
            scores = np.array(scores_list)
            credits = np.array(credits_list)
            weighted_sum = np.dot(scores, credits)
            total_credits = np.sum(credits)
            gpa = weighted_sum / total_credits
            data['id'] = student.id
            data['name'] = student.name
            data['gpa'] = gpa
            GPAs.append(data)
        sorted_GPAs = sorted(GPAs, key=lambda x: x['gpa'], reverse=True)
        print("{:<12}{:<15}{}".format("Student ID", "Name", "GPA"))
        print("{:<12}{:<15}{}".format("----------", "----", "---"))
        for gpa in sorted_GPAs:
            print(f"{gpa['id']:<12}{gpa['name']:<15}{gpa['gpa']:.1f}")
