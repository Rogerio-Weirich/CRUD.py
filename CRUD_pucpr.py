"""
Nome: Rogerio Raimundo Weirich
Curso: Análise e Desenvolvimento de Sistemas
"""
import random # import random numbers for ID

students = [] #empty list for students registration
professors = [] # empty list for professors

# noinspection PyShadowingNames
def generate_id(existing_ids):
    while True:
        new_id = random.randint(10000, 99999)
        if new_id not in existing_ids:
            return new_id

# noinspection PyShadowingNames
# this function aims to format the CPF to a XXX.XXX.XXX-XX format, has no big impact on the code, only aesthetics
def format_cpf(cpf):
    cpf_str = str(cpf)
    return f'{cpf_str[0:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}'

# noinspection PyShadowingNames
def add_student(new_student): #defines a function for name and surname
    students.append(new_student) # add the value 'name' and 'surname' to the list 'students'
    return students #returns the list 'students' updated

# noinspection PyShadowingNames
def add_professor(new_professor): # defines a function for name and surname
    professors.append(new_professor) # add the value 'name' and 'surname' to the list 'professors'
    return professors # returns the list 'professors' updated

# noinspection PyShadowingNames
def show_students(students):
    if not students:
        print("No registered students yet.")
        return
    print("\n=== Students ===")
    for i, student in enumerate(students):
        print(f"{i} - ID: {student['ID']}, Full name: {student['Name']} {student['Surname']}, CPF: {format_cpf(student['CPF'])}, Course: {student['Course']}")

# noinspection PyShadowingNames
def show_professors(professors):
    if not professors:
        print("No registered professors yet.")
        return
    print("\n=== Professors ===")
    for i, professor in enumerate(professors):
        print(f"{i} - ID: {professor['ID']}, Full name: {professor['Name']} {professor['Surname']}, CPF: {format_cpf(professor['CPF'])}, Course: {professor['Course']}")

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
        print("No course selected yet")
        return None
    else:
        print('Invalid course option. No course assigned.')
        return None


#Dictionary for the Menus
MAIN_MENU = {
    'A':'Student',
    'B':'Professor',
    'C':'Course',
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
    if option == 'C':
        if len(students) == 0: # verify if students have been added beforehand
            print('No registed students in a course yet.')
        else: # if students registered, show current list
            print(f'Registered students: {students}')
            continue
    if option == 'X':
        print("Exiting the system...")
        break #breaks the loop if "exit" is chosen
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
        operation = input("Choose a valid operation: ").upper()

        if operation == 'A' and option == 'A':
            add_name = input("Do you want to add students? [Y = YES / N = NO] ").upper()
            # Register a student's course, name, surname and cpf
            if add_name == 'Y':
                name = input("Enter the student\'s name: ").capitalize()
                surname = input("Enter the student\'s last name: ").capitalize()
                # changed the treatment for cpf, not it consider 11 numbers
                while True:
                    try:
                        cpf = int(input('Enter student\'s cpf: '))
                        if 10000000000 <= cpf <= 99999999999:
                            break
                        print('CPF must have 11 digits')
                    except ValueError:
                        print('Missing a number or no number digited')
                course = select_course() # fetch course menu
                student_id = generate_id({student['ID'] for student in students})
                confirm = input(f"Do you confirm the registration of {name} {surname} as student? [Y = YES / N = NO] ").upper()
                #creates a dictionary for the 'students' list if the previous menu was validated.
                if confirm == 'Y':
                    new_student = {
                        'ID': student_id,
                        'Name': name,
                        'Surname': surname,
                        'CPF': cpf,
                        'Course': course,
                    }
                    students.append(new_student)
                    # show both new and previous registered students
                    print(f"New student added successfully!")
                    show_students(students)
                else:
                    # if the previous menu wasn't validated, shows current students and cancel the entry for new one
                    print("Registration canceled. The student was not added.")
                    show_students(students)
            else:
                # Skip the students registration and goes to the operation menu
                print("If you want to check students, go to List Operation.")

        elif operation == 'A' and option == 'B':
            add_name = input('Do you want to add professors? [Y = YES / N = NO] ').upper()
            if add_name == 'Y':
                # Register a professor's course, name, surname and cpf
                name = input("Enter professor\'s name: ").capitalize()
                surname = input("Enter professor\'s last name: ").capitalize()
                # changed the treatment for cpf, not it consider 11 numbers
                while True:
                    try:
                        cpf = int(input('Enter professor\'s cpf: '))
                        if 10000000000 <= cpf <= 99999999999:
                            break
                        print('CPF must have 11 digits')
                    except ValueError:
                        print('Missing a number or no number digited')
                course = select_course() # fetch course menu
                professor_id = generate_id({professor['ID'] for professor in professors})
                confirm = input(f'Do you confirm the registration of {name} {surname} as professor? [Y = YES / N = NO] ').upper()
                # creates a dictionary for the 'professors' list if the previous menu was validated.
                if confirm == 'Y':
                    new_professor = {
                        'ID': professor_id,
                        'Name': name,
                        'Surname': surname,
                        'CPF': cpf,
                        'Course': course,
                    }
                    professors.append(new_professor)
                    # show both new and previous registered professors
                    print(f"New professor added successfully!")
                    show_professors(professors)
                else:
                    # if the previous menu wasn't validated, shows current professors and cancel the entry for new one
                    print("Registration canceled. The professor was not added.")
                    show_professors(professors)
            else:
                # Skip the professors registration and goes to the operation menu
                print("If you want to check professors, go to List Operation.")

        elif operation == 'B' and option == 'A':
            if len(students) == 0: #verify if no students are registered
                print("No registered students yet.")
            else: #show the registered students updated
                # added that simply to a better visual impact
                show_students(students)

        elif operation == 'B' and option == 'B':
            if len(professors) == 0: # verify if no professors are registered
                print("No registered professors yet.")
            else: # show the registered professors updated
                # added that simply to a better visual impact
                show_professors(professors)

        elif operation == 'C' and option == 'A':
            if len(students) == 0: # verify if no students are registered
                print("No registered students to exclude.")
                continue
            else: # if registered students, proceeds to exclusion process
                print("Registered students:")
                for i, student in enumerate(students): # enumerates the students list with index
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
                            print("Selected students successfully excluded!")
                            show_students(students)
                        else:
                            print("Operation cancelled.")
                    except ValueError:
                        # deal with user's input cannot be converted to integer
                        print("Invalid input. Please enter numbers separated by commas")
                else:
                    # user chose not to proceed with exclusion of students
                    print("Returning to previous menus.")
                    continue

        elif operation == 'C' and option == 'B':
            if len(professors) == 0: # verify if no professors are registered
                print("No registered professors to exclude.")
                continue
            else: # if registered professors, proceeds to exclusion process
                print("Registered professors:")
                for i, professor in enumerate(professors): # enumerates the professors list with index
                    print(f"{i}. - {professor['Name']} {professor['Surname']}") # shows the enumerated professors in the 'students' list
                exclude = input("Do you want to remove professors? [Y = YES / N = NO] ").upper()
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
                        invalid_indices = [i for i in indices if i < 0 or i >= len(professors)]
                        if invalid_indices:
                            print(f"Invalid {invalid_indices}. Please enter a valid index.")
                            continue
                        # show the students chosen to be excluded
                        print("You are about to exclude the following professor:")
                        for i in sorted(indices):
                            print(f"{i}. - {professors[i]['Name']} {professors[i]['Surname']}")
                        # final confirmation for exclusion
                        confirm_exclusion = input("Do you confirm? [Y = YES / N = NO] ").upper()
                        if confirm_exclusion == 'Y':
                            # exclude professor and return updated professors list
                            for i in sorted(indices, reverse=True):
                                professors.pop(i)
                            print("Selected professor successfully excluded!") # >:)
                            show_professors(professors)
                        else:
                            print("Operation cancelled.")
                    except ValueError:
                        # deal with user's input cannot be converted to integer
                        print("Invalid input. Please enter numbers separated by commas")
                else:
                    # user chose not to proceed with exclusion of students
                    print("Returning to previous menus.")
                    continue

        elif operation == 'D' and option == 'A':
            if len(students) == 0: # verify if no students are registered
                print("No registered students to edit")
            else: # if registered students, proceeds to edit process
                print("Registered Students:")
                for i, student in enumerate(students): # enumerates the students list with index
                    print(f"{i}. - {student['Name']} {student['Surname']}") # shows the index of student and name to edit
                edit = input("Do you want to edit student? [Y = YES / N = NO] ").upper() # ask if confirm edition
                if edit == 'Y':
                    # prompt the user to enter coma separated indices of student
                    indices_input = input("Enter the indices of students to be edited: ")
                    try: # code that might present error
                        # convert the input string into a list of integers
                        indices = [int(i) for i in indices_input.split(',')]
                        # check if the indices is impty
                        if not indices:
                            print("No indices provided. Operation cancelled.")
                            # skip the loop
                            continue
                            # check for invalid indices (negatives or beyong lenght)
                        invalid_indices = [i for i in indices if i < 0 or i >= len(students)]
                        if invalid_indices:
                            # inform the user about invalid indices and skip
                            print(f"Invalid {invalid_indices}. Please enter a valid index.")
                            continue
                        # shows student for editing
                        print("You are about to edit the following student:")
                        for i in sorted(indices):
                            # show details of student (name surname cpf course)
                            print(f"{i}. - Name: {students[i]['Name']} Surname: {students[i]['Surname']} CPF: {students[i]['CPF']} Course: {students[i]['Course']}")
                        # ask for confirmation to proceed edit
                        confirm_edit = input("Do you confirm? [Y = YES / N = NO] ").upper()
                        if confirm_edit == 'Y':
                            # avoid index issues, iterate over indices in reverse
                            for i in sorted(indices, reverse=True):
                                print(f"\nEditing student: {new_student['Name']} {new_student['Surname']}")
                                print('What would you like to edit?')
                                # show edit menu options
                                print("1 - Name")
                                print("2 - Surname")
                                print("3 - CPF")
                                print("4 - Course")
                                # prompt the user to choose edit option
                                edit_option = input("Choose and option (1 - 4): ")
                                # track if any change were made
                                edited = False
                                if edit_option == '1':
                                    # prompt for new name
                                    new_name = input("Enter new name for student: ").capitalize()
                                    # check if input is not empty
                                    if new_name.strip():
                                        confirm = input(f'Confirm new name "{new_name}"? [Y = YES / N = NO] ').upper()
                                        if confirm == 'Y':
                                            new_student['Name'] = new_name
                                            edited = True # this marks that there was an edit
                                        else:
                                            print("Name edit cancelled.")
                                    else:
                                        print("Empty input. Name edit cancelled.")
                                elif edit_option == '2':
                                    # prompt for new surname
                                    new_surname = input("Enter new surname for student: ").capitalize()
                                    # check if input is not empty
                                    if new_surname.strip():
                                        confirm = input(f'Confirm new name "{new_surname}"? [Y = YES / N = NO] ').upper()
                                        if confirm == 'Y':
                                            new_student['Surname'] = new_surname
                                            edited = True # this marks that there was an edit
                                        else:
                                            print("Surname edit cancelled.")
                                    else:
                                        print("Empty input. Surname edit cancelled.")
                                elif edit_option == '3':
                                    # prompt for new cpf
                                    new_cpf = input("Enter new cpf for student: ")
                                    # check if input is not empty
                                    if new_cpf.strip():
                                        confirm = input(f'Confirm new cpf "{format_cpf(new_cpf)}"? [Y = YES / N = NO] ').upper()
                                        if confirm == 'Y':
                                            new_student['CPF'] = new_cpf
                                            edited = True # this marks that there was an edit
                                        else:
                                            print("CPF edit cancelled.")
                                    else:
                                        print("Empty input. CPF edit cancelled.")
                                elif edit_option == '4':
                                    # call a function to select course from COURSE MENU
                                    new_course = select_course()
                                    if new_course:
                                        confirm = input(f"Confirm new course '{new_course}'? [Y = YES / N = NO] ").upper()
                                        if confirm == 'Y':
                                            new_student['Course'] = new_course
                                            edited = True # this marks that there was an edit
                                        else:
                                            print("Course edit cancelled.")
                                    else:
                                        print("Invalid course. Course edit cancelled.")
                                else:
                                    print("Invalid option. No changes made.")
                                # if any changes were made, show success message
                                if edited:
                                    print(f"Student {new_student['Name']} {new_student['Surname']} has been updated.")
                            # show the current and updated list
                            show_students(students)
                        else:
                            # if no confirmation is given, cancel operation
                            print("Operation cancelled.")
                    except ValueError:
                        # deal with invalid input like NaN indices
                        print("Invalid input. Please enter numbers separated by commas")
                else:
                        # if use choose not to edit, return previous menu
                        print("Returning to previous menus.")
                continue

        # this block is basically a copy paste of operation == 'D' and option == 'A'
        elif operation == 'D' and option == 'B':
            if len(professors) == 0: # verify if no professors are registered
                print("No registered students to edit")
            else: # if registered professors, proceeds to edit process
                print("Registered Professors:")
                for i, professor in enumerate(professors): # enumerates the professors list with index
                    print(f"{i}. - {professor['Name']} {professor['Surname']}") # shows the index of professors and name to edit
                    edit = input("Do you want to edit professor? [Y = YES / N = NO] ").upper() # ask if confirm edition
                    if edit == 'Y':
                        # prompt the user to enter coma separated indices of professor
                        indices_input = input("Enter the indices of professors to be edited: ")
                        try: # code that might present error
                            # convert the input string into a list of integers
                            indices = [int(i) for i in indices_input.split(',')]
                            # check if the indices is impty
                            if not indices:
                                print("No indices provided. Operation cancelled.")
                                # skip the loop
                                continue
                                # check for invalid indices (negatives or beyong lenght)
                            invalid_indices = [i for i in indices if i < 0 or i >= len(students)]
                            if invalid_indices:
                                # inform the user about invalid indices and skip
                                print(f"Invalid {invalid_indices}. Please enter a valid index.")
                                continue
                            # shows professor for editing
                            print("You are about to edit the following student:")
                            for i in sorted(indices):
                                # show details of professor (name surname cpf course)
                                print(f"{i}. - Name: {professors[i]['Name']} Surname: {professors[i]['Surname']} CPF: {professors[i]['CPF']} Course: {professors[i]['Course']}")
                            # ask for confirmation to proceed edit
                            confirm_edit = input("Do you confirm? [Y = YES / N = NO] ").upper()
                            if confirm_edit == 'Y':
                                # avoid index issues, iterate over indices in reverse
                                for i in sorted(indices, reverse=True):
                                    print(f"\nEditing professor: {new_professor['Name']} {new_professor['Surname']}")
                                    print('What would you like to edit?')
                                    # show edit menu options
                                    print("1 - Name")
                                    print("2 - Surname")
                                    print("3 - CPF")
                                    print("4 - Course")
                                    # prompt the user to choose edit option
                                    edit_option = input("Choose and option (1 - 4): ")
                                    # track if any change were made
                                    edited = False # begin as false, assuming that no edition has been made yet
                                    if edit_option == '1':
                                        # prompt for new name
                                        new_name = input("Enter new name for professor: ").capitalize()
                                        # check if input is not empty
                                        if new_name.strip():
                                            confirm = input(f'Confirm new name "{new_name}"? [Y = YES / N = NO] ').upper()
                                            if confirm == 'Y':
                                                new_professor['Name'] = new_name
                                                edited = True # this marks that there was an edit
                                            else:
                                                print("Name edit cancelled.")
                                        else:
                                            print("Empty input. Name edit cancelled.")
                                    elif edit_option == '2':
                                        # prompt for new surname
                                        new_surname = input("Enter new surname for professor: ").capitalize()
                                        # check if input is not empty
                                        if new_surname.strip():
                                            confirm = input(f'Confirm new name "{new_surname}"? [Y = YES / N = NO] ').upper()
                                            if confirm == 'Y':
                                                new_professor['Surname'] = new_surname
                                                edited = True # this marks that there was an edit
                                            else:
                                                print("Surname edit cancelled.")
                                        else:
                                            print("Empty input. Surname edit cancelled.")
                                    elif edit_option == '3':
                                        # prompt for new cpf
                                        new_cpf = input("Enter new cpf for professor: ")
                                        # check if input is not empty
                                        if new_cpf.strip():
                                            confirm = input(f'Confirm new cpf "{format_cpf(new_cpf)}"? [Y = YES / N = NO] ').upper()
                                            if confirm == 'Y':
                                                new_professor['CPF'] = new_cpf
                                                edited = True # this marks that there was an edit
                                            else:
                                                print("CPF edit cancelled.")
                                        else:
                                            print("Empty input. CPF edit cancelled.")
                                    elif edit_option == '4':
                                        # call a function to select course from COURSE MENU
                                        new_course = select_course()
                                        if new_course:
                                            confirm = input(f"Confirm new course '{new_course}'? [Y = YES / N = NO] ").upper()
                                            if confirm == 'Y':
                                                new_professor['Course'] = new_course
                                                edited = True # this marks that there was an edit
                                            else:
                                                print("Course edit cancelled.")
                                        else:
                                            print("Invalid course. Course edit cancelled.")
                                    else:
                                        print("Invalid option. No changes made.")
                                    # if any changes were made, show success message
                                    if edited:
                                        print(f"Professor {new_professor['Name']} {new_professor['Surname']} has been updated.")
                                # show the current and updated list
                                show_professors(new_professor)
                            else:
                                # if no confirmation is given, cancel operation
                                print("Operation cancelled.")
                        except ValueError:
                            # deal with invalid input like NaN indices
                            print("Invalid input. Please enter numbers separated by commas")
                    else:
                            # if use choose not to edit, return previous menu
                            print("Returning to previous menus.")
                    continue

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