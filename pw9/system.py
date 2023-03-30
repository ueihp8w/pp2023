import numpy as np
from domains import *
import extract_file
import os
import pickle
import threading
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import math

class StudentMarkSystem():
    def __init__(self):
        extract_file.extract()
        if os.path.isfile("./students"):
            t = threading.Thread(target=self.deserializeThreadFunction, args=("students",))
            t.start()
            t.join()
        else:
            self.students = []
        if os.path.isfile("./courses"):
            t = threading.Thread(target=self.deserializeThreadFunction, args=("courses",))
            t.start()
            t.join()
        else:
            self.courses = []
        if os.path.isfile("./marks"):
            t = threading.Thread(target=self.deserializeThreadFunction, args=("marks",))
            t.start()
            t.join()
        else:
            self.marks = []

    def deserializeThreadFunction(self, data):
        with open(data, "rb") as f:
            if (data == "students"):
                self.students = pickle.load(f)
            elif (data == "courses"):
                self.courses = pickle.load(f)
            elif (data == "marks"):
                self.marks = pickle.load(f)

    def student_window(self, window):
        window.title("Student Information")
        frame = ttk.Frame(window)
        frame.pack()
        widgets_frame = ttk.LabelFrame(frame, text="Insert Student")
        widgets_frame.grid(row=0, column=0, padx=10, pady=10)

        ttk.Label(widgets_frame, text="Student ID:").grid(row=0, column=0, padx=10, pady=10)
        self.student_id_entry = ttk.Entry(widgets_frame)
        self.student_id_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

        ttk.Label(widgets_frame, text="Student Name:").grid(row=1, column=0, padx=10, pady=10)
        self.student_name_entry = ttk.Entry(widgets_frame)
        self.student_name_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=10)

        ttk.Label(widgets_frame, text="Date of Birth:").grid(row=2, column=0, padx=10, pady=10)
        self.student_dob_entry = ttk.Entry(widgets_frame)
        self.student_dob_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=10)

        button = ttk.Button(widgets_frame, text="Insert", command=self.insert_student)
        button.grid(row=3, column=0, sticky="nsew", columnspan=2, padx=10, pady=10)

        treeFrame = ttk.Frame(frame)
        treeFrame.grid(row=0, column=1, padx=10, pady=10)
        treeScroll = ttk.Scrollbar(treeFrame)
        treeScroll.pack(side="right", fill="y")

        cols = ("ID", "Student Name", "Date of Birth")
        self.treeview = ttk.Treeview(treeFrame, show="headings", 
                                yscrollcommand=treeScroll.set, columns=cols, height=10)
        self.treeview.column("ID", width=50)
        self.treeview.column("Student Name", width=200)
        self.treeview.column("Date of Birth", width=160)
        for col_name in cols:
            self.treeview.heading(col_name, text=col_name)
        self.treeview.pack()
        treeScroll.config(command=self.treeview.yview)

        for student in self.students:
            self.treeview.insert('', tk.END, values=[student.id, student.name, student.dob])

    def insert_student(self):
        student_id = self.student_id_entry.get()
        student_name = self.student_name_entry.get()
        student_dob = self.student_dob_entry.get()
        student_info = Student(student_id, student_name, student_dob)
        self.students.append(student_info)
        self.treeview.insert('', tk.END, values=[student_id, student_name, student_dob])
        self.student_id_entry.delete(0, "end")
        self.student_name_entry.delete(0, "end")
        self.student_dob_entry.delete(0, "end")

    def course_window(self, window):
        window.title("Course Information")
        frame = ttk.Frame(window)
        frame.pack()
        widgets_frame = ttk.LabelFrame(frame, text="Insert Course")
        widgets_frame.grid(row=0, column=0, padx=10, pady=10)

        ttk.Label(widgets_frame, text="Course ID:").grid(row=0, column=0, padx=10, pady=10)
        self.course_id_entry = ttk.Entry(widgets_frame)
        self.course_id_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

        ttk.Label(widgets_frame, text="Course Name:").grid(row=1, column=0, padx=10, pady=10)
        self.course_name_entry = ttk.Entry(widgets_frame)
        self.course_name_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=10)

        ttk.Label(widgets_frame, text="No. of Credits:").grid(row=2, column=0, padx=10, pady=10)
        self.course_credit_entry = ttk.Entry(widgets_frame)
        self.course_credit_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=10)

        button = ttk.Button(widgets_frame, text="Insert", command=self.insert_course)
        button.grid(row=3, column=0, sticky="nsew", columnspan=2, padx=10, pady=10)

        treeFrame = ttk.Frame(frame)
        treeFrame.grid(row=0, column=1, padx=10, pady=10)
        treeScroll = ttk.Scrollbar(treeFrame)
        treeScroll.pack(side="right", fill="y")

        cols = ("ID", "Course Name", "No. of Credits")
        self.treeview = ttk.Treeview(treeFrame, show="headings", 
                                yscrollcommand=treeScroll.set, columns=cols, height=10)
        self.treeview.column("ID", width=50)
        self.treeview.column("Course Name", width=200)
        self.treeview.column("No. of Credits", width=160)
        for col_name in cols:
            self.treeview.heading(col_name, text=col_name)
        self.treeview.pack()
        treeScroll.config(command=self.treeview.yview)

        for course in self.courses:
            self.treeview.insert('', tk.END, values=[course.id, course.name, course.credit])

    def insert_course(self):
        course_id = self.course_id_entry.get()
        course_name = self.course_name_entry.get()
        course_credit = self.course_credit_entry.get()
        course_info = Course(course_id, course_name, course_credit)
        self.courses.append(course_info)
        self.treeview.insert('', tk.END, values=[course_id, course_name, course_credit])
        self.course_id_entry.delete(0, "end")
        self.course_name_entry.delete(0, "end")
        self.course_credit_entry.delete(0, "end")

    def mark_window(self, window):
        window.title("Grade Book")
        frame = tk.Frame(window)
        frame.pack()

        select_course_frame = tk.LabelFrame(frame, text="Select a course to input marks for students:")
        select_course_frame.grid(row=0, column=0, padx=10, pady=10)

        self.course_var = tk.StringVar(select_course_frame)
        self.course_var.set(self.courses[0].name)
        course_dropdown = tk.OptionMenu(select_course_frame, self.course_var, *[course.name for course in self.courses])
        course_dropdown.grid(row=1, column=0, padx=10, pady=10)

        input_marks_button = tk.Button(select_course_frame, text="Input Marks", command=self.input_marks)
        input_marks_button.grid(row=1, column=1, padx=10, pady=10)

        view_marks_frame = tk.LabelFrame(frame, text="Select a course to show marks:")
        view_marks_frame.grid(row=2, column=0, padx=10, pady=10)

        self.view_course_var = tk.StringVar(view_marks_frame)
        self.view_course_var.set(self.courses[0].name)
        view_course_dropdown = tk.OptionMenu(view_marks_frame, self.view_course_var, *[course.name for course in self.courses])
        view_course_dropdown.grid(row=3, column=0, padx=10, pady=10)

        view_marks_button = tk.Button(view_marks_frame, text="View Marks", command=self.show_marks)
        view_marks_button.grid(row=3, column=1, padx=10, pady=10)

    def input_marks(self):
        selected_course = next((course for course in self.courses if course.name == self.course_var.get()), None)
        if selected_course:
            for student in self.students:
                mark_input = simpledialog.askfloat(title="Input Marks", prompt=f"Enter mark for student {student.name} in course {selected_course.name}: ")
                if mark_input is not None:
                    mark = math.floor(mark_input * 10) / 10
                    mark = Mark(student, selected_course, mark)
                    self.marks.append(mark)
        else:
            messagebox.showerror("Error", "No course selected.")    

    def show_marks(self):
        selected_course = next((course for course in self.courses if course.name == self.view_course_var.get()), None)
        if selected_course:
            marks = [mark for mark in self.marks if mark.get_course().id == selected_course.id]
            if marks:
                window = tk.Tk()
                window.title(selected_course.name)
                frame = ttk.Frame(window)
                frame.pack()

                treeFrame = ttk.Frame(frame)
                treeFrame.grid(row=0, column=0, padx=10, pady=10)
                treeScroll = ttk.Scrollbar(treeFrame)
                treeScroll.pack(side="right", fill="y")

                cols = ("ID", "Student Name", "Mark")
                self.treeview = ttk.Treeview(treeFrame, show="headings", 
                                        yscrollcommand=treeScroll.set, columns=cols, height=10)
                self.treeview.column("ID", width=50)
                self.treeview.column("Student Name", width=180)
                self.treeview.column("Mark", width=80)
                for col_name in cols:
                    self.treeview.heading(col_name, text=col_name)
                self.treeview.pack()
                treeScroll.config(command=self.treeview.yview)
                for mark in marks:
                    student_id = mark.get_student().id
                    student_name = mark.get_student().name
                    mark_value = mark.get_mark()
                    self.treeview.insert('', tk.END, values=[student_id, student_name, mark_value])
                window.mainloop()
            else:
                messagebox.showwarning("Warning", "No marks for this course.")
        else:
            messagebox.showerror("Error", "No course selected.")

    def show_GPAs(self, window):
        window.title("GPA")
        frame = ttk.Frame(window)
        frame.pack()

        treeFrame = ttk.Frame(frame)
        treeFrame.grid(row=0, column=0, padx=10, pady=10)
        treeScroll = ttk.Scrollbar(treeFrame)
        treeScroll.pack(side="right", fill="y")

        cols = ("ID", "Student Name", "GPA")
        self.gpaview = ttk.Treeview(treeFrame, show="headings", 
                                yscrollcommand=treeScroll.set, columns=cols, height=10)
        self.gpaview.column("ID", width=50)
        self.gpaview.column("Student Name", width=180)
        self.gpaview.column("GPA", width=80)
        for col_name in cols:
            self.gpaview.heading(col_name, text=col_name)
        self.gpaview.pack()
        treeScroll.config(command=self.gpaview.yview)

        GPAs = [] 
        for student in self.students:
            scores_list = []
            credits_list = []
            data = {}
            for mark in self.marks:
                if mark.get_student().id == student.id:
                    scores_list.append(mark.get_mark())
                    credits_list.append(mark.get_course().credit)
            scores = np.array(scores_list).astype(float)
            credits = np.array(credits_list).astype(float)
            weighted_sum = np.dot(scores, credits)
            total_credits = np.sum(credits)
            gpa = weighted_sum / total_credits
            data['id'] = student.id
            data['name'] = student.name
            data['gpa'] = math.floor(gpa * 10) / 10
            GPAs.append(data)
        sorted_GPAs = sorted(GPAs, key=lambda x: x['gpa'], reverse=True)
        for gpa in sorted_GPAs:
            self.gpaview.insert('', tk.END, values=[gpa['id'], gpa['name'], gpa['gpa']])

    def serializeThreadFunction(self):
        dbfile = open("students", "wb")
        pickle.dump(self.students, dbfile)
        dbfile.close()

        dbfile = open("courses", "wb")
        pickle.dump(self.courses, dbfile)
        dbfile.close()

        dbfile = open("marks", "wb")
        pickle.dump(self.marks, dbfile)
        dbfile.close()
    
    def serialize(self):
        t = threading.Thread(target=self.serializeThreadFunction)
        t.start()
        t.join()

    def reset(self):
        self.students = []
        self.courses = []
        self.marks = []