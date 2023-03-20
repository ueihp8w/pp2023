from output import StudentMarkSystem
import compress_file

if __name__=="__main__":
    marksheet = StudentMarkSystem()

    while True:
        print("\nStudent Mark Management System\n")
        print("1. Input number of students and their information")
        print("2. Input number of courses and their information")
        print("3. Select a course to input marks for students")
        print("4. List all courses")
        print("5. List all students")
        print("6. Show marks for a given course")
        print("7. Show average GPA of student")
        print("8. Exit\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            marksheet.input_students()
        elif choice == "2":
            marksheet.input_courses()
        elif choice == "3":
            marksheet.input_marks()
        elif choice == "4":
            marksheet.list_courses()
        elif choice == "5":
            marksheet.list_students()
        elif choice == "6":
            marksheet.show_marks()
        elif choice == "7":
            marksheet.show_GPAs()
        elif choice == "8":
            print("Exiting program...")
            compress_file.compress()
            break
        else:
            print("Invalid choice. Please try again.")