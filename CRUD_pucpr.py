"""
Nome: Rogerio Raimundo Weirich
Curso: Análise e Desenvolvimento de Sistemas
"""
import random # import random numbers for ID

students = [] #empty list for students registration
professors = [] # empty list for professors
classes = [] # empty list for classes :D
enrollments = [] #empty list for enrollments (help me)

# noinspection PyShadowingNames
def generate_id(existing_ids): # generates random ID for new studentes/professor
    while True:
        new_id = random.randint(10000, 99999) # make ID always have 5 digits
        if new_id not in existing_ids: # guarantee that each ID is unique
            return new_id

# noinspection PyShadowingNames
def format_cpf(cpf): # this function aims to format the CPF to a XXX.XXX.XXX-XX format, for aesthetics purpose
    cpf_str = str(cpf) # convert 'cpf' to a string
    return f'{cpf_str[0:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}' # XXX.XXX.XXX-XX format

# noinspection PyShadowingNames
def add_student(new_student): #defines a function for name and surname
    students.append(new_student) # add the value 'name' and 'surname' to the list 'students'
    return students #returns the list 'students' updated

# noinspection PyShadowingNames
def add_professor(new_professor): # defines a function for name and surname
    professors.append(new_professor) # add the value 'name' and 'surname' to the list 'professors'
    return professors # returns the list 'professors' updated

# noinspection PyShadowingNames
def add_class(new_class): # defines a function for classes
    classes.append(new_class) # add the value class to the list classes
    return classes # returns the classes updated

# noinspection PyShadowingNames
def show_students(students):
    if not students: # verify if students are registered
        print("No registered students yet.")
        return
    print("\n=== Students ===") # prints the student list
    for i, student in enumerate(students): # adds index for each student registered for better readability
        print(
            f"{i} - ID: {student['ID']}, "
            f"Full name: {student['Name']} {student['Surname']}, "
            f"CPF: {format_cpf(student['CPF'])}, "
            f"Course: {student['Course']}"
        )

# noinspection PyShadowingNames
def show_professors(professors):
    if not professors: # verify if professors are registered
        print("No registered professors yet.")
        return
    print("\n=== Professors ===") # prints the professor list
    for i, professor in enumerate(professors): # adds index for each professor registered for better readability
        print(
            f"{i} - ID: {professor['ID']}, "
            f"Full name: {professor['Name']} {professor['Surname']}, "
            f"CPF: {format_cpf(professor['CPF'])}, "
            f"Course: {professor['Course']}"
        )

# noinspection PyShadowingNames
def show_classes(classes): # this function aim to show the classes
    if not classes:
        print("No registered classes yet.") # message shown if no class existing
        return
    print("\n=== Classes ===") # formated display for classes (for aesthetics purpose)
    for i, class_ in enumerate(classes): # ordenates classes with index (i)
        professor = class_['Professor'] # fetch dictionary with professor data for that class
        students_count = len(class_['Students']) # counts how many students in the class (max 20)
        # displays the basic info of the class
        print( # Mucho texto
            f"{i} - ID: {class_['ID']}, "
            f"Course: {class_['Course']}, "
            f"Professor: {professor['Name']} {professor['Surname']} "
            f"(ID: {professor['ID']}), "
            f"Students Enrolled: {students_count}/20")
        # if enrolled students, shows students list
        if students_count > 0:
            print(" Enrolled students:")
            for j, student in enumerate(class_['Students']):
                print(f"    {j} - {student['Name']} {student['Surname']} (ID: {student['ID']})")

# noinspection PyShadowingNames
def show_enrollments(enrollments, students, classes):
    if not students or not classes:
        print("No students or classes registered. Enrollments cannot be listed.")
        return
    if not enrollments: # check enrollments, if not, shows message and quit
        print("No students enrolled in any classes yet.")
        return
    print("\n=== Enrollments ===")
    for enrollment in enrollments: # iterate through each enrollment in enrollment list
        student = None
        for current_student in students:
            if current_student['ID'] == enrollment['StudentID']:
                student = current_student
                break
        for current_class in classes:
            if current_class['ID'] == enrollment['ClassID']:
                class_ = current_class
                break
            print( # why is that so extensive?! T-T
                f"Student: {student['Name']} {student['Surname']}, "
                f"CPF: {format_cpf(student['CPF'])}, "
                f"Course: {class_['Course']}, "
                f"Class ID: {class_['ID']}"
            )
    print(f"Total enrollments: {len(enrollments)}") # show total number of enrollment

def show_menu(title, menu_option, extra): #show the formatted menu
    print(f'\n==={title}===') #show the titles for each menu
    for key, label in menu_option.items():
        print(f'{key} - {label}') #shows the dictionary for each menu
    print(extra) #additional text shown at the end

# noinspection PyShadowingNames
def show_course_details(course_menu, classes): # I miss the three lines functions T^T
    # Check if there are any courses available
    if not course_menu:
        print("No courses available.")
        return
    # Display list of available courses with their original keys
    print("\n=== Available Courses ===")
    for key, course in course_menu.items():
        print(f"{key}: {course}")
    # Prompt user to select a course by key
    key_input = input("Enter a course to view details: ")
    # Check if the input key exists in COURSE_MENU
    if key_input in course_menu:
        selected_course = course_menu[key_input]  # Get the course name
        print(f"\n=== Details for Course: {selected_course} ===")
        # Filter classes by the selected course
        course_classes = [class_ for class_ in classes if class_['Course'] == selected_course]
        if not course_classes:
            print("No classes available for this course.")
            return
        # Display filtered classes with professor and students
        print("\nClasses for this course:")
        for i, class_ in enumerate(course_classes):
            professor = class_['Professor']
            students_count = len(class_['Students'])
            print( # why is that so extensive?! T-T
                f"{i} - ID: {class_['ID']}, "
                f"Professor: {professor['Name']} {professor['Surname']} "
                f"(ID: {professor['ID']}, CPF: {format_cpf(professor['CPF'])}, "
                f"Course: {professor['Course']}), "
                f"Students Enrolled: {students_count}/20")
            if students_count > 0:
                print("  Enrolled Students:")
                for j, student in enumerate(class_['Students']):
                    print( # why is that so extensive too?! T-T
                        f"    {j} - {student['Name']} {student['Surname']} "
                          f"(ID: {student['ID']}, "
                          f"CPF: {format_cpf(student['CPF'])}, "
                          f"Course: {student['Course']})"
                    )
    else:
        print("Invalid course key.")

def select_course(): # defines the course menu
    if not COURSE_MENU: # verify if there is any course available
        print("No courses available.")
        return None
    show_menu('COURSE MENU', COURSE_MENU, 'X - No course selected yet')# formatted menu for course
    course_option = input('Choose a course:').upper() # prompt user to choose a course
    if course_option == 'X': # if cancels, return None
        print("Course selection cancelled.")
        return None
    if course_option in COURSE_MENU: # validates the course selected beforehand
        return COURSE_MENU[course_option]
    else:
        print("Invalid course option selected.")
        return None

# noinspection PyShadowingNames
def select_professor():
    if not professors: # check if professors are registered
        print("No professors registered. Register one first.")
        return None
    show_professors(professors) # shows the list of registered professors
    index = input("Enter the index of the professor to assign: ") # prompt user to enter index
    try:
        index = int(index) # convert to integer
        if 0 <= index < len(professors): # verify if its within range
            return professors[index] # return professor dictionary
        else: # display invalid index input
            print("Invalid index.")
            return None
    except ValueError: # deal with NaN input
        print("Invalid input. Must be a number.")
        return None

# noinspection PyShadowingNames
def select_student(): # ctrl c + ctrl v of the above "def" ;)
    if not students: # check if students are registered
        print("No students registered. Register one first.")
        return None
    show_students(students) # shows the list of registered professors
    index = input("Enter the index of the student to enroll: ")
    try:
        index = int(index) # convert to integer
        if 0 <= index < len(students): # verify if its within range
            return students[index] # return professor dictionary
        else: # display invalid index input
            print("Invalid index.")
            return None
    except ValueError: # deal with NaN input
        print("Invalid input. Must be a number.")
        return None

# noinspection PyShadowingNames
def select_class(): # another copy paste of the above "def"
    if not classes: # check if classes are registered
        print("No classes created. Create one first.")
        return None
    show_classes(classes)     # shows the list of registered classes
    index = input("Enter the index of the class: ")
    try:
        index = int(index) # convert to integer
        if 0 <= index < len(classes): # verify if its within range
            return classes[index] # return professor dictionary
        else: # display invalid index input
            print("Invalid index.")
            return None
    except ValueError: # deal with NaN input
        print("Invalid input. Must be a number.")
        return None

MAIN_MENU = { # Dictionary for the options
    'A':'Student',
    'B':'Professor',
    'C':'Course',
    'D':'Class',
    'E':'Enrollment',
}
OPERATION_MENU = { # Dictionary for the operations
    'A':'Include',
    'B':'List',
    'C':'Exclude',
    'D':'Change',
    'X':'Back to main Menu',
}
COURSE_MENU = { # Dictionary for the courses
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
finish_all = False
while True: #looping for option menu
    show_menu( # show the menu with the following options for Main Menu
        'MAIN MENU', MAIN_MENU, "X - Exit"
    )
    #fetches user's chosen option for the main menu
    option = input("Choose an option: ").upper()
    if option == 'X':
        print("Exiting the system...")
        break #breaks the loop if "exit" is chosen
    elif option not in MAIN_MENU:
        print("Invalid option...")
        continue
    else: # back to main menu if invalid
        print(f"The selected option is: {MAIN_MENU[option]}")

    while True: #Variables for the second menu, shown only if a valid option has been picked up in the main menu
        #Show the menu for the Operation Menu
        show_menu('OPERATION MENU', OPERATION_MENU, 'Q - Quit Program')
        # fetches user's chosen option for the second menu
        operation = input("Choose a valid operation: ").upper()

        if operation == 'A' and option == 'A': # Student registration
            add_name = input("Do you want to add students? [Y = YES / N = NO] ").upper()
            if add_name == 'Y': # Register a student's course, name, surname and cpf
                name = input("Enter the student\'s name: ").capitalize()
                surname = input("Enter the student\'s last name: ").capitalize()
                while True: # changed the treatment for cpf, now it consider 11 numbers
                    try:
                        cpf = int(input('Enter student\'s cpf: '))
                        if 10000000000 <= cpf <= 99999999999: # verify if the cpf has 11 digits
                            break
                        print('CPF must have 11 digits')
                    except ValueError:
                        print('Missing a number or no number digited') # validate the cpf
                course = select_course() # fetch course menu
                existing_ids = set() # creates an empty set to keep existing IDs
                for student in students: # creates an unique ID
                    existing_ids.add(student['ID'])
                student_id = generate_id(existing_ids) # gererates an unique ID
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
                    print(f"New student added successfully!") # show both new and previous registered students
                    show_students(students)
                else:
                    # if the previous menu wasn't validated, shows current students and cancel the entry for new one
                    print("Registration canceled. The student was not added.")
                    show_students(students)
            else:
                # Skip the students registration and goes to the operation menu
                print("If you want to check students, go to List Operation.")

        elif operation == 'A' and option == 'B': # Professor registration
            add_name = input('Do you want to add professors? [Y = YES / N = NO] ').upper()
            if add_name == 'Y':
                # Register a professor's course, name, surname and cpf
                name = input("Enter professor\'s name: ").capitalize()
                surname = input("Enter professor\'s last name: ").capitalize()
                while True:
                    try: # changed the treatment for cpf, now it consider 11 numbers
                        cpf = int(input('Enter professor\'s cpf: '))
                        if 10000000000 <= cpf <= 99999999999: # verify if the cpf has 11 digits
                            break
                        print('CPF must have 11 digits')
                    except ValueError:
                        print('Missing a number or no number digited') # validate the cpf
                course = select_course() # fetch course menu
                existing_ids = set() # creates an empty set to keep existing IDs
                for professor in professors:
                    existing_ids.add(professor['ID'])
                professor_id = generate_id(existing_ids) # generates an unique ID
                confirm = input(f'Do you confirm the registration of {name} {surname} as professor? [Y = YES / N = NO] ').upper()
                if confirm == 'Y': # creates a dictionary for the 'professors' list if the previous menu was validated.
                    new_professor = {
                        'ID': professor_id,
                        'Name': name,
                        'Surname': surname,
                        'CPF': cpf,
                        'Course': course,
                    }
                    professors.append(new_professor)
                    print(f"New professor added successfully!") # show both new and previous registered professors
                    show_professors(professors)
                else:
                    # if the previous menu wasn't validated, shows current professors and cancel the entry for new one
                    print("Registration canceled. The professor was not added.")
                    show_professors(professors)
            else:
                # Skip the professors registration and goes to the operation menu
                print("If you want to check professors, go to List Operation.")

        elif operation == 'A' and option == 'C': # Course creation (which is impossible!) >:(
            confirm = input("You can not include any other course. Press [Y = Yes/N = Back] to continue.").upper()
            if confirm == 'Y':
                print("Please consult the system administration.")
            else:
                print("Operation canceled.")

        elif operation == 'A' and option == 'D': # Class Creation
            if len(classes) >= 3:  # Limit to 3 classes as per request
                print("Maximum of 3 classes already created.")
                continue
            print("Creating a new class...")
            course = select_course() # fetches course from course menu
            if course is None: # cancel class creation
                print("Class creation cancelled (no course selected).")
                continue
            existing_ids = set() # creates an empty set to keep existing IDs
            for class_ in classes:
                existing_ids.add(class_['ID']) # generates an unique ID
            class_id = generate_id(existing_ids)  # Generate unique ID for class
            professor = select_professor() # fetchs registered professors to attach to a class
            if professor is None:
                print("Class creation cancelled (no professor selected).")
                continue
            # Check if professor is already assigned to another class (max 1 professor per class)
            if any(class_['Professor']['ID'] == professor['ID'] for class_ in classes):
                print("Professor already assigned to a class. Choose another.")
                continue
            # Check if professor's course matches the class course
            if professor['Course'] != course: # verification for professor matches the discipline
                print("Professor's course does not match the selected course for the class.")
                continue
            new_class = { # dictionary for classes
                'ID': class_id,
                'Course': course,
                'Professor': professor,
                'Students': []  # Starts empty, max 20 students
            }
            add_class(new_class)
            print(
                f"New class created successfully for course {course} with professor {professor['Name']} {professor['Surname']}."
            )
            show_classes(classes)

        elif operation == 'A' and option == 'E': # Enroll student in a class
            selected_class = select_class() # selects a class for enrollment
            if selected_class is None:
                continue
            if len(selected_class['Students']) >= 20: # check if the class is not full (max 20)
                print("Class is full (max 20 students).")
                continue
            student = select_student() # select student to enroll
            if student is None: # check if no student registered
                continue
            # Check if student is already enrolled in this class
            if student in selected_class['Students']:
                print("Student already enrolled in this class.")
                continue
            # Check if student's course matches the class course
            if student['Course'] != selected_class['Course']:
                print("Student's course does not match the class course.")
                continue
            selected_class['Students'].append(student) # add to the class's student list
            enrollments.append({
                'StudentID': student['ID'],
                'ClassID': selected_class['ID']
            })
            print(
                f"Student {student['Name']} {student['Surname']} enrolled successfully in class for '{selected_class['Course']}'."
            )
            show_classes(classes) # show the updated class list

        elif operation == 'B' and option == 'A': # List Students
            if len(students) == 0: #verify if no students are registered
                print("No registered students yet.")
            else: #show the registered students updated
                show_students(students)

        elif operation == 'B' and option == 'B': # List Professors
            if len(professors) == 0: # verify if no professors are registered
                print("No registered professors yet.")
            else: # show the registered professors updated
                show_professors(professors)

        elif operation == 'B' and option == 'C': # list course
            show_course_details(COURSE_MENU, classes) # shows available courses and allow menu to see details

        elif operation == 'B' and option == 'D': # list classes
            show_classes(classes) # show classes

        elif operation == 'B' and option == 'E': # list enrollments
            show_enrollments(enrollments, students, classes)

        elif operation == 'C' and option == 'A': # Exclude Students
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
                        indices = []
                        for i in indices_input.split(','):
                            indices.append(int(i)) # convert string of indices into list of integers
                        if not indices: # verifies if user gave any indices
                            print("No indices provided. Operation cancelled.")
                            continue
                        invalid_indices = []
                        for i in indices: # verifies if the indices are within the actual range of the lis
                            if i < 0 or i >= len(students):
                                invalid_indices.append(i)
                        if invalid_indices:
                            print(f"Invalid indices: {invalid_indices}. Please enter valid indices.")
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
                                removed_student = students.pop(i)
                                for class_ in classes: # will remove students from any enrolled class
                                    if removed_student in class_['Students']:
                                        class_['Students'].remove(removed_student)
                                        print(f"Removed {removed_student['Name']} from class {class_['Course']}.")
                                # the slice assignment [:] modifies the list in-place
                                temporary_enrollments = []
                                for enrollment in enrollments:
                                    if enrollment['StudentID'] != removed_student['ID']:
                                        temporary_enrollments.append(enrollment)
                                enrollments[:] = temporary_enrollments
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

        elif operation == 'C' and option == 'B': # Exclude Professors (copy paste of C and A, changed variables)
            if len(professors) == 0: # verify if no professors are registered
                print("No registered professors to exclude.")
                continue
            else: # if registered professors, proceeds to exclusion process
                print("Registered professors:")
                for i, professor in enumerate(professors): # enumerates the professors list with index
                    print(f"{i}. - {professor['Name']} {professor['Surname']}") # shows the enumerated professors in the 'students' list
                exclude = input("Do you want to remove professors? [Y = YES / N = NO] ").upper()
                if exclude == 'Y':
                    # prompt the user to enter the indices of professors to be excluded
                    indices_input = input("Enter the indices of professors to be excluded: ")
                    try:
                        # convert string of indices into list of integers
                        indices = []
                        for i in indices_input.split(','):
                            indices.append(int(i))
                        if not indices: # verifies if user gave any indices
                            print("No indices provided. Operation cancelled.")
                            continue
                        invalid_indices = []
                        for i in indices: # verifies if the indices are within the actual range of the list
                            if i < 0 or i >= len(professors):
                                invalid_indices.append(i)
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
                                removed_professor = professors.pop(i)
                                for class_ in classes:
                                    if class_['Professor']['ID'] == removed_professor['ID']:
                                        class_['Professor'] = None
                                        print(f"Removed professor from class {class_['Course']}. Assign a new one.")
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

        elif operation == 'C' and option == 'D': # Exclude Classes
            if not classes: # verify is no classes registered
                print("No classes to exclude.")
                continue
            show_classes(classes) # show classes list
            index = input("Enter the index of the class to exclude: ")
            try:
                index = int(index) # convert to integer
                if 0 <= index < len(classes): # verify if the index is valid
                    removed_class = classes.pop(index) # remove class from classes list
                    # removes all enrollments attached to the excluded class
                    temporary_enrollments = []
                    for enrollment in enrollments:
                        if enrollment['ClassID'] != removed_student['ID']:
                            temporary_enrollments.append(enrollment)
                    enrollments[:] = temporary_enrollments
                    print(f"Class for '{removed_class['Course']}' excluded successfully.")
                    show_classes(classes) # display updated class
                else:
                    print("Invalid index.")
            except ValueError: # deal with NaN input
                print("Invalid input. Must be a number.")

        elif operation == 'D' and option == 'A': # Editing Students
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
                        indices = []
                        for i in indices_input.split(','):
                            indices.append(int(i.strip()))  # convert the input string into a list of integers and strip to handle spaces
                        if not indices:  # check if indices list is empty
                            print("No indices provided. Operation cancelled.")
                            continue
                        # check if the indices is impty
                        if not indices:
                            print("No indices provided. Operation cancelled.")
                            # skip the loop
                            continue
                            # check for invalid indices (negatives or beyong lenght)
                        invalid_indices = []
                        for i in indices:
                            if i < 0 or i >= len(students):
                                invalid_indices.append(i)
                        if invalid_indices:
                            # inform the user about invalid indices and skip
                            print(f"Invalid {invalid_indices}. Operation cancelled.")
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

        elif operation == 'D' and option == 'B': # Editing Professor (copy paste of D and A, changed variables)
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
                            indices = []
                            for i in indices_input.split(','):
                                indices.append(int(i.strip()))  # convert the input string into a list of integers and strip to handle spaces
                            # check if the indices is impty
                            if not indices:
                                print("No indices provided. Operation cancelled.")
                                continue # skip the loop
                            invalid_indices = []
                            for i in indices:
                                if i < 0 or i >= len(professors): # check for invalid indices (negatives or beyong lenght)
                                    invalid_indices.append(i)
                            if invalid_indices:
                                # inform the user about invalid indices and skip
                                print(f"Invalid {invalid_indices}. Operation cancelled.")
                                continue
                            print("You are about to edit the following student:") # shows professor for editing
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

        elif operation == 'D' and option == 'D': # Editing Classes
            selected_class = select_class() # makes user select a class to edit
            if selected_class is None:
                continue
            print(f"Editing class for {selected_class['Course']}.")
            # show edit options
            print("1 - Change Professor")
            print("2 - Change Course")
            edit_option = input("Choose an option (1-2): ") # makes user select an edit option
            edited = False
            if edit_option == '1': # will prompt the user to select a new professor
                new_professor = select_professor()
                if new_professor is None:
                    print("Edit cancelled.")
                else: # Check if new professor's course matches
                    if new_professor['Course'] != selected_class['Course']:
                        print("Professor's course does not match the class course.")
                    else: # update professor for the class
                        selected_class['Professor'] = new_professor
                        edited = True
                        print("Professor changed successfully.")
            elif edit_option == '2': # will prompt the user to select a new course
                new_course = select_course()
                if new_course: # Check if professor's course matches new course
                    if selected_class['Professor']['Course'] != new_course:
                        print("Current professor's course does not match the new course. Change professor first.")
                    else: # update course for the class
                        selected_class['Course'] = new_course
                        edited = True
                        print("Course changed successfully.")
                else:
                    print("Edit cancelled.")
            if edited: # show updated classes list if its changed
                show_classes(classes)

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
    if finish_all: #finish the looping
        break