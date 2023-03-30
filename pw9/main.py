from tkinter import *
from system import StudentMarkSystem
import compress_file

class MarksheetGUI:
    def __init__(self, master):
        self.master = master
        self.marksheet = StudentMarkSystem()

        Button(master, text="Student Information", command=self.student_window).grid(row=0, column=0, padx=10, pady=10)
        Button(master, text="Course Information", command=self.course_window).grid(row=0, column=1, padx=10, pady=10)
        Button(master, text="Mark Information", command=self.mark_window).grid(row=1, column=0, padx=10, pady=10)
        Button(master, text="GPA Information", command=self.show_GPAs).grid(row=1, column=1, padx=10, pady=10)
        Button(master, text="Reset System", command=self.reset).grid(row=2, column=0, padx=10, pady=10)
        Button(master, text="Save and Exit", command=self.exit).grid(row=2, column=1, padx=10, pady=10)

    def student_window(self):
        student_window = Tk()
        self.marksheet.student_window(student_window)
        student_window.mainloop()
        
    def course_window(self):
        course_window = Tk()
        self.marksheet.course_window(course_window)
        course_window.mainloop()

    def mark_window(self):
        mark_window = Tk()
        self.marksheet.mark_window(mark_window)
        mark_window.mainloop()

    def show_GPAs(self):
        gpa_window = Tk()
        self.marksheet.show_GPAs(gpa_window)
        gpa_window.mainloop()

    def reset(self):
        self.marksheet.reset()

    def exit(self):
        print("Exiting program...")
        self.marksheet.serialize()
        compress_file.compress()
        self.master.destroy()

if __name__=="__main__":
    root = Tk()
    root.title("Student Mark Management System")
    gui = MarksheetGUI(root)
    root.mainloop()
