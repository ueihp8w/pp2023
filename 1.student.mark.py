# Ask the user to input a number of unit (course / student)
def input_number(unit):
    return int(input(f"Enter the number of {unit} in this class: "))

# Ask the user to enter a list of info for an unit_type
def input_infos(unit_type, infos):
    item = {}

    # TODO: input info for the unit_type (student/course info)
    for i in infos:
        value = input(f"Enter the {i} of {unit_type}: ")
        item.update({i:value})

    return item

# Input the student mark in a course base on the course id
def input_mark():

    student["marks"] = {}
    # TODO: check mark in student or not (can use dict)
    # If not, enter the mark for the course


# Display a list of students
def list_students(students):

    # TODO: check what happens if there's no student (hint: len(students))
    print("There aren't any students yet")

    # TODO: display the student list
    print("Here is the student list: ")
    # TODO: add loop function to check the info of student
    print(f"{i+1}. {student['id']} - {student['name']} - {student['DoB']}")

        # TODO: check if mark student and print out the information
        if "marks" in student:
            print("Marks (Course Id - Mark): ", end="")
            
            

# Display a list of courses
def list_courses(courses):
    # TODO: check what happens if there's no course (hint: (lencourse))
    print("There aren't any courses yet")
        
    print("Here is the course list: ")
    # TODO: add loop function to check the info of course
    print(f"{i+1}. {course['id']} - {course['name']}")

# Ask the user to enter an integer to select an option
def select(option_range, input_message="Choose an option: "):
    selection = input(input_message)
    if not selection.isnumeric():
        return -1
    selection = int(selection)
    if selection not in option_range:
        return -1
    return selection

# Pause the program
def pause():
    input("Press Enter to continue...")

# Main function for the "game"
def main():
    # Initialize the list
    courses = []
    students = []
    num_students = 0
    num_courses = 0
    student_infos = ("ID", "name", "DoB")
    course_infos = ("ID", "name")

    while(True):
        print("""
Welcome to the student managament system! Please choose an option as below:
    0. Exit
    1. Input number of students
    2. Input students information (ID, name, DoB)
    3. Input number of courses
    4. Input course information (ID, name)
    5. Input marks for student in a course
    6. List courses
    7. List students""") 
        selection = select(range(0, 8))                                                                 # Choose option from 0 -> 7
        if selection == 0:
            break

        elif selection == 1:                                                                            # Option 1
            num_students = input_number("students")
        elif selection == 2:                                                                            # Option 2                                                     
            students.append(input_infos("student", student_infos))
        elif selection == 3:                                                                            # Option 3
            num_courses = input_number("courses")
        elif selection == 4:                                                                            # Option 4
            courses.append(input_infos("course", course_infos))
        elif selection == 5:                                                                            # Option 5

        elif selection == 6:                                                                            # Option 6

        elif selection == 7:                                                                            # Option 7

        else:
            print("Invalid input. Please try again!")
        pause() 

# Call the main function
if __name__ == "__main__":
    main()