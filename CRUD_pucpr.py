"""
Nome: Rogerio Raimundo Weirich
Curso: Análise e Desenvolvimento de Sistemas
"""
import random # import random numbers for ID

students = [] #empty list for students registration
professors = [] # empty list for professors

# noinspection PyShadowingNames
def add_student(new_student): #defines a function for name and surname
    students.append(new_student) # add the value 'name' and 'surname' to the list 'students'
    return students #returns the list 'students' updated

def add_professor(new_professor): # defines a function for name and surname
    professors.append(new_professor) # add the value 'name' and 'surname' to the list 'professors'
    return professors # returns the list 'professors' updated

def show_menu(title, menu_option, extra): #show the formatted menu
    print(f'\n==={title}===') #show the titles for each menu
    for key, label in menu_option.items():
        print(f'{key} - {label}') #shows the dictionary for each menu
    print(extra) #additional text shown at the end

def select_course(): # defines the course menu
    COURSE_MENU = {
        '1': 'System Analysis and Development',
        '2': 'Computer Science',
        '3': 'Data Science and Artificial Intelligence',
        '4': 'Computer Engineering',
        '5': 'Software Engineering',
        '6': 'Information Technology Management',
        '7': 'Digital Games',
        '8': 'Information Systems',
        '9': 'Web Design'
    }
    show_menu('COURSE MENU', COURSE_MENU, '0 - No course selected yet') # formatted menu for course
    course_option = input("Choose a course: ").upper()
    if course_option in COURSE_MENU: # validates the course options
        return COURSE_MENU[course_option]
    elif course_option == '0':
        return None
    else:
        print('Invalid course option. No course assigned.')
        return None


#Dictionary for the Menus
MAIN_MENU = {
    'A':'Student',
    'B':'Course',
    'C':'Professor',
    'D':'Class',
    'E':'Enrollment',
}
OPERATION_MENU = {
    'A':'Include',
    'B':'List',
    'C':'Exclude',
    'D':'Change',
    'X':'Back to main Menu',
}
#looping for which option below
finish_all = False
while True:
    # show the menu with the following options for Main Menu
    show_menu(
        'MAIN MENU', MAIN_MENU, "X - Exit"
    )
    #fetches user's chosen option for the main menu
    option = input("Choose an option: ").upper()
    if option == 'B':
        if len(students) == 0: # verify if students have been added beforehand
            print('No registed students in a course yet.')
        else: # if students registered, show current list
            print(f'Registered students: {students}')
            continue
    if option == 'X':
        print("Exiting the system...")
        break #breaks the loop if "exit" is chosen
    elif option != 'A': #This elif has to be removed in the future, option set only to ignore other menu entries for study purposes.
        print("Under development... Try again later!")
        continue
    elif option not in MAIN_MENU:
        print("Invalid option...")
        continue
    else: # back to main menu if invalid
        print(f"The selected option is: {MAIN_MENU[option]}")


    #Variables for the second menu, shown only if a valid option has been picked up in the main menu
    while True:
        #Show the menu for the Operation Menu
        show_menu('OPERATION MENU', OPERATION_MENU, 'Q - Quit Program')
        # fetches user's chosen option for the second menu
        operation = input("Choose a valid operation: "
        ).upper()


        if operation == 'A' and option == 'A':
            add_name = input("Do you want to add students? [Y = YES / N = NO] ").upper()
            # Register a student's name and last name
            if add_name == 'Y':
                name = input("Enter the student\'s name: ").capitalize()
                surname = input("Enter the student\'s last name: ").capitalize()
                cpf = int(input("Enter the student\'s cpf: "))
                course = select_course() # fetch course menu
                # confirmation to validate registration
                confirm = input(f"Do you confirm the registration of {name} {surname}? [Y = YES / N = NO] ").upper()
                #creates a dictionary for the 'students' list if the previous menu was validated.
                if confirm == 'Y':
                    new_student = {
                        'Name': name,
                        'Surname': surname,
                        'CPF': cpf,
                        'Course': course,
                    }
                    students.append(new_student)
                    #show both new students and previous students registered
                    print(f"New student added successfully!")
                    print("Current list:", students)
                else:
                    #if the previous menu wasn't validated, shows current students and cancel the entry for new one
                    print("Registration canceled. The student was not added.")
                    print("Current list:", students)
            else:
                # Skip the students registration and goes to the operation menu
                print("If you want to check students, go to List Operation.")

        elif operation == 'B':
            if len(students) == 0: #verify if no students are registered
                print("No registered students yet.")
            else: #show the registered students
                print(f"The students registered are: {students}")

        elif operation == 'C':
            if len(students) == 0: # verify if no students are registered
                print("No registered students to exclude.")
                continue
            else: # if registered students, proceeds to exclusion process
                print("Registered students:")
                for i, student in enumerate(students): # enumerates the students list with index (i.e.: 0, 1, 2, 3)
                    print(f"{i}. - {student['Name']} {student['Surname']}") # shows the enumerated students in the 'students' list
                    exclude = input("Do you want to remove students? [Y = YES / N = NO] ").upper()
                    if exclude == 'Y':
                        # prompt the user to enter the indices of students to be excluded
                        indices_input = input("Enter the indices of students to be excluded: ")
                        try:
                            # convert string of indices into list of integers
                            indices = [int(i) for i in indices_input.split(',')]
                            # verifies if user gave any indices
                            if not indices:
                                print("No indices provided. Operation cancelled.")
                                continue
                            # verifies if the indices are within the actual range of the list
                            invalid_indices = [i for i in indices if i < 0 or i >= len(students)]
                            if invalid_indices:
                                print(f"Invalid {invalid_indices}. Please enter a valid index.")
                                continue
                            # show the students chosen to be excluded
                            print("You are about to exclude the following students:")
                            for i in sorted(indices):
                                print(f"{i}. - {students[i]['Name']} {students[i]['Surname']}")
                            # final confirmation for exclusion
                            confirm_exclusion = input("Do you confirm? [Y = YES / N = NO] ").upper()
                            if confirm_exclusion == 'Y':
                                # exclude students and return updated students list
                                for i in sorted(indices, reverse=True):
                                    students.pop(i)
                                print("Selected students excluded successfully!")
                                print("Current list:", students)
                            else:
                                print("Operation cancelled.")
                        except ValueError:
                            # deal with user's input cannot be converted to integer
                            print("Invalid input. Please enter numbers separated by commas")
                    else:
                        # user chose not to proceed with exclusion of students
                        print("Returning to previous menus.")
                        continue

        elif operation == 'D':
            print("Under development... Try again later!")
        elif operation == 'X': # exit second menu and go back to main menu
            print("Returning to main menu...")
            break

        elif operation == 'Q': #Quits the prrogram
            print("Quitting program...")
            finish_all = True
            break

        elif operation not in OPERATION_MENU: #if invalid, show the operation menu again
            print("Invalid operation, try again")
            continue

        #asks the user if they want to continue
        finish = input("Do you want to continue? [Y = Yes / N = Back]: ").upper()
        if finish == 'Y': #validate the second menu option
            print("Operation successfully finished...")
            continue

        elif finish == 'N': #returns to the previous menu
            print("Returning the previous menu")
            continue

        elif finish == 'Q': #quits the program
            print("Quitting program...")
            finish_all = True
            break
        else:
            print("Invalid option")
            continue

    #finish the looping
    if finish_all:
        break

    #waiting for next steps...