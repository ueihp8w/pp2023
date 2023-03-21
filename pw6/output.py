import numpy as np
from domains import *
from input import Input
import extract_file
import os
import pickle

class StudentMarkSystem(Input):
    def __init__(self):
        extract_file.extract()
        if os.path.isfile("./students"):
            dbfile = open("students", "rb")
            self.students = pickle.load(dbfile)
            dbfile.close()
        else:
            self.students = []
        if os.path.isfile("./courses"):
            dbfile = open("courses", "rb")
            self.courses = pickle.load(dbfile)
            dbfile.close()
        else:
            self.courses = []
        if os.path.isfile("./marks"):
            dbfile = open("marks", "rb")
            self.marks = pickle.load(dbfile)
            dbfile.close()
        else:
            self.marks = []

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
            if mark.get_course().id == selected_course.id:
                student_id = mark.get_student().id
                student_name = mark.get_student().name
                mark_value = mark.get_mark()
                print(f"{student_id} - {student_name}: {mark_value}")
        if not any(mark.get_course().id == selected_course.id for mark in self.marks):
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

    def serialize(self):
        dbfile = open("students", "wb")
        pickle.dump(self.students, dbfile)
        dbfile.close()

        dbfile = open("courses", "wb")
        pickle.dump(self.courses, dbfile)
        dbfile.close()

        dbfile = open("marks", "wb")
        pickle.dump(self.marks, dbfile)
        dbfile.close()