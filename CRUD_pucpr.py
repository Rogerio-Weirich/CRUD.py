import random
import json

'''=== MENUS ===''' 
MAIN_MENU = { # Main options dictionary
    'A':'Student',
    'B':'Professor',
    'C':'Course',
    'D':'Class',
    'E':'Enrollment',
}

OPERATION_MENU = { # Operations Dictionary
    'A':'Include',     # C
    'B':'List',        # R
    'C':'Change/Edit', # U
    'D':'Exclude',     # D
    'X':'Back to main Menu',
}

COURSE_MENU = { # Courses Dictionary
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

'''=== DATA STORAGE ===''' 
students = [] #empty list for students registration
professors = [] # empty list for professors
classes = [] # empty list for classes :D
enrollments = [] #empty list for enrollments (help me t-t)


def save_data(students, professors, classes, enrollments, filename='data.json'): # save date yay
    data = { # groups all lists in a single dictionary (hope its alright)
        'students': students,
        'professors': professors,
        'classes': classes,
        'enrollments': enrollments
    }
    with open(filename, 'w') as f: # opens the file in write mode. File will close automatically, even if error
        json.dump(data, f, indent=4) # equal a tab \o/, also uses json library to write in the file
    print(f"Data successfully saved at {filename}")


def load_data(filename='data.json'): # load data yay
    try: # deal with the file if it do not exists
        with open(filename, 'r') as f:
            data = json.load(f)
        return( #if the key do not exists, return empty list instead of error
            data.get('students', []),
            data.get('professors', []),
            data.get('classes', []),
            data.get('enrollments', [])
        )
    except FileNotFoundError: # if no file, display this message below
        print(f"File {filename} not found! Starting with empty lists...")
        return [], [], [], []



'''=== SUPPORT FUNCTIONS(I guess 👀) ==='''
def generate_id(existing_ids): # generates random ID for new studentes/professor
    while True:
        new_id = random.randint(10000, 99999) # make ID always have 5 digits
        if new_id not in existing_ids: # ensure it is unique!!!
            return new_id


def format_cpf(cpf): # this function aims to format the CPF to a XXX.XXX.XXX-XX format, for aesthetics purpose
    cpf_str = str(cpf) # convert 'cpf' to a string
    return f'{cpf_str[0:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}' # XXX.XXX.XXX-XX format


def validate_cpf():
    while True: 
        try: # validates if cpf has 11 digits and if its valid
            cpf = int(input('Enter CPF (11 digits): '))
            if 10000000000 <= cpf <= 99999999999: # ensure it has 11 digits
                return cpf
            print("CPF must have 11 digits.")
        except ValueError: # treatment for NaN
            print("Please enter a valid CPF (Numbers only).")


'''=== ENTITY MANAGEMENT === "'entity' for the lack of better generic word"'''
def add_entity(entity_type, entity_list): # adds student or professor
    add_name = input(f"Do you want to add {entity_type}s? [Y = Yes | N = No]: ").upper().strip()
    if add_name == 'Y': # fetch basic data (full name, course, cpf, random ID)
        name = input(f"Enter the {entity_type}'s name: ").strip().capitalize()
        surname = input(f"Enter the {entity_type}'s surname: ").strip().capitalize()
        cpf = validate_cpf() # calls validate cpf function
        course = select_course() # calls course function
        if course is None: # cancel if no course was chosen
            print(f"{entity_type.strip().capitalize()} registration cancelled.")
            return
        existing_ids = set() # will generate unique ID
        for entity in entity_list:
            existing_ids.add(entity['ID'])
        entity_id = generate_id(existing_ids)
        confirm = input(f"Do you confirm the registration of {name} {surname}? [Y = Yes | N = No]: ").upper().strip()
        if confirm == 'Y': # confirms registration
            new_entity = { # data for new entity? person? individual? human? argh >:(
                'ID': entity_id,
                'Name': name,
                'Surname': surname,
                'CPF': cpf,
                'Course': course,
            }
            entity_list.append(new_entity) # get the data to its dictionary
            print(f"New {entity_type} added successfully!")
            show_entity(entity_type, entity_list)
        elif confirm == 'N':
            print(f"Registration cancelled. The {entity_type} was not added.")
            show_entity(entity_type, entity_list) 
            return
        else:
            print("Invalid option. Try again.")
    elif add_name == 'N': 
        print(f"If you want to check {entity_type}s, go to 'List'.")
        return
    else:
        print("Invalid Option, please try again.")
        return
        

def add_enrollment(classes, students, enrollments): # enroll student into a class
    selected_class = select_class() # call the 'select class' function
    if selected_class is None:
        return
    if len(selected_class['Students']) >= 20: # defines a max capacity for a class
        print("Class full. (Max 20 students allowed)")
        return
    student = select_entity('student', students) # select students within 'select_entity' function
    if student in selected_class['Students']: # treatment for students already in classes
        print("Student already enrolled in this class.")
        return 
    if student['Course'] != selected_class['Course']: # treatment if students' course is different
        print("Student's Course does not match the class Course.")
        return
    selected_class['Students'].append(student)
    enrollments.append({ #
        'StudentID': student['ID'],
        'ClassID': selected_class['ID']
    })
    print(
        f"Student: {student['Name']} {student['Surname']} "
        f"successfully enrolled in {selected_class['Course']}'s class."
    )
    show_classes(classes)


def add_class(classes, professors): # creates classes
    if len(classes) >= 3: # limit of three classes per course
        print("Maximum of 3 classes already created.")
        return
    print("Creating a new class...")
    course = select_course() # selects a course
    if course is None:
        print("Class creation cancelled. (No Course selected)")
        return
    existing_ids = set() # generates a unique ID
    for class_ in classes:
        existing_ids.add(class_['ID'])
    class_id = generate_id(existing_ids)
    professor = select_entity('professor', professors) # selects a professor
    if professor is None:
        print("Class creation cancelled. (No professor selected)")
        return
    professor_assigned = False
    for class_ in classes: # ensure that professor is not already assigned
        if class_['Professor']['ID'] == professor['ID']:
            professor_assigned = True
            break
    if professor_assigned:
        print("Professor already assigned to a class.")
        return
    if professor['Course'] != course: # ensure that its the same course
        print("Professor's Course, does not match the selected class' course.")
        return
    new_class = { # data for new class
        'ID': class_id,
        'Course': course,
        'Professor': professor,
        'Students': []
    }
    classes.append(new_class)
    print(
        f"New class created successfully for {course} with professor:"
        f"{professor['Name']} {professor['Surname']}."
          )
    show_classes(classes)


'''=== SELECTION FUNCTIONS ==='''
def select_entity(entity_type, entity): # selects the entidades
    if not entity: #verifies is the list is not empy
        print(f"No {entity_type}s registered. Register one first.")
        return None
    show_entity(entity_type, entity) # show the current entities
    i = input(f"Enter the {entity_type}'s index to assign: ")
    try: # tries to convert the  entries for valid indices
        i = int(i)
        if 0 <= i < len(entity): # verifies if indices is within list
            return entity[i]
        else:
            print("Invalid index.")
            return None
    except ValueError: # fetches the error if NaN
        print("Invalid input. Must be a Number.")
        return None


def select_class(): # selects classes
    if not classes: # verifies if there is classes 
        print("No classes created. Create one first.")
        return None
    show_classes(classes) # shows the classes
    i = input("Enter class' index:")
    try: # tries to convert the  entries for valid indices
        i = int(i)  
        if 0 <= i < len(classes): # verifies if indices is within list
            return classes[i]
        else:
            print("Invalid index.")
    except ValueError: # fetches the error if NaN
        print("Invalid input. Must be a Number.")
        return None


def select_course(): # selects a course 
    if not COURSE_MENU: # verifies if the dictionary is not empty 
        print("No courses available.")
        return None
    show_menu('COURSE MENU', COURSE_MENU, 'X - Back') # uses 'show_menu' function and fecthes user's choice
    course_option = input('Select a course: ').upper().strip()
    if course_option == 'X': # allows cancel
        print("Course selection cancelled.")
        return None
    for key, course in COURSE_MENU.items(): #s get the matching key
        if key == course_option:
            return course
    print("Invalid course option selected.")
    return None # treatment if key do not match


'''==== REMOVE & EDIT ENTITIES ==='''
def remove_entity(entity_type, entity_list, classes, enrollments=None): # remove entities
    if not entity_list: # if there is no "ENTITIES 🙄"
        print(f"No registered {entity_type}s to exclude.")
        return
    print(f"Registered {entity_type}s:") # show registered entities via indices
    for i, entity in enumerate(entity_list):
        print(
            f"{i} - {entity['Name']} "
            f"{entity['Surname']}"
              )
    exclude = input(f"Removing {entity_type}s, proceed? [Y = Yes | N = No]: ").upper().strip() 
    if exclude == 'Y': 
        indices_input = input(f"Enter the indices of {entity_type}s to be excluded: ")
        try: # tries to convert entry for valid indices
            indices = []
            for i in indices_input.split(','): # formats the string from (1,2, 3) to (1, 2, 3)
                indices.append(int(i.strip())) # used to accept entries like: (1, 2, 3) w/o erros and convert to integer
            if not indices:
                print("No indices provided. Operation cancelled.")
                return
            invalid_indices = []
            for i in indices: # verifies if indicies are within range
                if i < 0 or i >= len(entity_list):
                    invalid_indices.append(i)
                if invalid_indices: 
                    print(f"Invalid indices: {invalid_indices}. Please enter valid indices.")
                    return
                print(f"You're about to exclude the following {entity_type}s:")
                for i in sorted(indices): # iterate indices in order to avoid errors
                    print(
                        f"{i} - {entity_list[i]['Name']} "
                        f"{entity_list[i]['Surname']}"
                          )
                confirm_exclusion = input("Exclusion is permanent. Proceed? [Y = Yes | N = No]: ").upper().strip()
                if confirm_exclusion == 'Y': # final confirmation for exclusion
                    for i in sorted(indices, reverse=True):
                        removed_entity = entity_list.pop(i)
                        if entity_type == 'student': # if entity is assigned somewhere, will be treated here
                            for class_ in classes: # remove student from the class
                                if removed_entity in class_['Students']:
                                    class_['Students'].remove(removed_entity)
                                    print(f"Removed {removed_entity['Name']} from class {class_['Course']}.")
                            if enrollments: # remove all the register of the student ID
                                temporary_enrollments = []
                                for enrollment in enrollments:
                                    if enrollment['StudentID'] != removed_entity['ID']:
                                        temporary_enrollments.append(enrollment)
                                enrollments[:] = temporary_enrollments
                        elif entity_type == 'professor': # remove teatcher assignment of classes and else
                            for class_ in classes: # removes from the class
                                if class_['Professor']['ID'] == removed_entity['ID']: 
                                    class_['Professor'] = None
                                    print(f"Removed professor from class {class_['Course']}. Please assign a new one.")
                    print(f'Selected {entity_type}s sucessfully excluded!')
                    show_entity(entity_type, entity_list)
                else:
                    print("Operation cancelled.")
        except ValueError:
            print("Invalid input. Please enter a valid input.")
    else:
        print("Returning previous menu.")


def remove_enrollment(enrollments, students, classes): # remove enrollment
    if not students or not classes: # verifies if there is valid students or classes
        print("No students or classes registered. No enrollment available to be removed.")
        return
    if not enrollments: # verifies if there is valid enrollments
        print("No enrolled students in any class yet.")
        return
    show_enrollments(enrollments, students, classes)
    print("\n=== Remove Enrollment ===")
    selected_class = select_class() # selects which class to delete first
    if selected_class is None: 
        print("Enrollment removal cancelled. (No class selected)")
        return
    if not selected_class['Students']: # verifies if there is students in the class
        print("No enrolled students in this class.")
        return
    print(
        f"\nEnrolled student in {selected_class['Course']} "
        f"Class ID: {selected_class['ID']} "
          )
    for i, student in enumerate(selected_class['Students']):
        print( # shows the students and their indices in the class
            f"{i} - {student['Name']} {student['Surname']} "
            f"ID: {student['ID']}"
        )
        indices_input = input("Enter the index of the student to unenroll: ")
        try: # asks for the valid indices
            i = int(indices_input.strip())
            if 0 <= i < len(selected_class['Students']): # verifies if its within range
                student_to_remove = selected_class['Students'][i]
                print(
                    f"You are about to unenroll: " 
                    f"{student_to_remove['Name']} {student_to_remove['Surname']} "
                    f"from {selected_class['Course']}."
                    )
                confirm = input("Confirm unenroll? [Y = Yes | N = No]: ").upper().strip()
                if confirm == 'Y': # confirmation for removal
                    selected_class['Students'].pop(i)
                    temporary_enrollments = []
                    for enrollment in enrollments:
                        if not (enrollment['StudentID'] == student_to_remove['ID'] and enrollment['ClassID'] == selected_class['ID']):
                            temporary_enrollments.append(enrollment)
                    enrollments[:] = temporary_enrollments # removes enrollment register recreating the list 
                    print(
                        f"Student: {student_to_remove['Name']} {student_to_remove['Surname']} " 
                        f"sucessfully unenrolled from {selected_class['Course']}."
                        )
                    show_enrollments(enrollments, students, classes) # shows current enrollment
                else:
                    print("Enrollment exclusion cancelled.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Must be a number.")
                            

def remove_class(classes, enrollments): # remove classes
    if not classes: # verifies if there is no classes 
        print("No classes to exclude.")
        return
    show_classes(classes) # show the classes for user to remove
    i = input("Enter the index of class to exclude: ")
    i = int(i)
    try: # asks the index and deal with possible erros
        if 0 <= i < len(classes): # verifies if within range
            removed_class = classes.pop(i) # temporary removes to get its id
            temporary_enrollment = [] 
            for enrollment in enrollments: # update enrollment, removing what belonged to the class and recreates the list
                if enrollment['ClassID'] != removed_class['ID']:
                    temporary_enrollment.append(enrollment) 
            enrollments[:] = temporary_enrollment
            print(f"Class for {removed_class['Course']} excluded succesfully!")
            show_classes(classes)
        else:
            print("Invalid index. Please enter a valid one.")
    except ValueError:
        print("Invalid index. Must be a Number.")
    

def edit_entity(entity_type, entity_list): # edit entity 
    if not entity_list: # guarantee that the list is not empyt
        print(f"No registered {entity_type}s to edit.")
        return
    print(f"Registered {entity_type.strip().capitalize()}s:")
    for i, entity in enumerate(entity_list): # entity's selection via index
        print(f"{i}. - {entity['Name']} {entity['Surname']}")
    edit = input(f"Proceed with {entity_type}'s edition? [Y = Yes | N = No]: ").upper().strip()
    if edit == 'Y': # confirms access to edit
        indices_input = input(f"Enter the indices of {entity_type}s to be edited: ")
        try: # asks the index and treat NaN errors
            indices = [] # temporary list 
            for i in indices_input.split(','): # formats the string from (1,2, 3) to (1, 2, 3)
                indices.append(int(i.strip())) # used to accept entries like: (1, 2, 3) w/o erros and convert to integer
            if not indices: # validates if index is valid
                print("No indices provided. Operation cancelled.")
                return
            invalid_indices = []
            for i in indices:
                if i < 0 or i >=len(entity_list): # verify if index is within range
                    invalid_indices.append(i)
                if invalid_indices:
                    print(f"Invalid indices: {invalid_indices}. Operation cancelled.")
                    return
            print(f"You're about to edit the following {entity_type}s:")
            for i in sorted(indices): # shows selected entities details e asks confirmation
                print(
                    f"{i}. - Name: {entity_list[i]['Name']} "
                    f"Surname: {entity_list[i]['Surname']} "
                    f"CPF: {format_cpf(entity_list[i]['CPF'])} "
                    f"Course: {entity_list[i]['Course']}"
                )
            confirm_edit = input("Proceed with editing? [Y = Yes | N = No]: ").upper().strip()
            if confirm_edit == 'Y':
                for i in sorted(indices, reverse=True):
                    entity = entity_list[i] # iterates among each index to edit
                    print(f"\nEditing {entity_type}: {entity['Name']} {entity['Surname']}")
                    print("What would you like to edit?") # displays edit menu
                    print("1 - Name")
                    print("2 - Surname")
                    print("3 - CPF")
                    print("4 - Course")
                    edit_option = input("Select an option (1 - 4): ")
                    edited = False # controls if the edit was indeed made
                    if edit_option == '1': # logic for each edit 
                        new_name = input(f"Enter a new name for {entity_type}: ").strip().capitalize() 
                        if new_name.strip(): # prevent empty spaces
                            confirm = input(f"Confirm new name: {new_name}? [Y = Yes | N = No]: ").upper().strip()
                            if confirm == 'Y':
                                entity['Name'] = new_name # adds new data to the variable
                                edited = True
                            else:
                                print("Name edit cancelled.")
                        else:
                            print("Empty input. Name edit cancelled.")
                    elif edit_option == '2':
                        new_surname = input(f"Enter a new surname for{entity_type}: ").strip().capitalize()
                        if new_surname.strip():
                            confirm = input(f"Confirm new surname: {new_surname}? [Y = Yes | N = No]: ").upper().strip()
                            if confirm == 'Y':
                                entity['Surname'] = new_surname
                                edited = True
                            else:
                                print("Name edit cancelled.")
                        else:
                            print("Empty input. Name edit cancelled.")
                    elif edit_option == '3':
                        while True:
                            try: # verify if new cpf has 11 digits and if NaN
                                new_cpf = int(input(f"Enter new {entity_type}'s CPF: "))
                                if 10000000000 <= new_cpf <= 99999999999:
                                    confirm = input(f"Confirm new CPF: {format_cpf(new_cpf)}? [Y = Yes | N = No]: ").upper().strip()
                                    if confirm == 'Y':
                                        entity['CPF'] = new_cpf
                                        edited = True
                                        break
                                    else:
                                        print("CPF edit cancelled.")
                                        break
                                print("CPF must have 11 digits.")
                            except ValueError:
                                print("Missing a number or no numbers provided.")
                    elif edit_option == '4': 
                        new_course = select_course()
                        if new_course: # simnply selecter new course
                            confirm = input(f"Confirm new course: {new_course}? [Y = Yes | N = No]: ").upper().strip()
                            if confirm == 'Y':
                                entity['Course'] = new_course
                                edited = True
                            else:
                                print("Course edit cancelled.")
                        else:
                            print("Invalid course. Course edit cancelled.")
                    else:
                        print("Invalid option. No changes made.")
                    if edited:
                        print( # displays edited data
                            f"{entity_type.strip().capitalize()}: "
                            f"{entity['Name']} "
                            f"{entity['Surname']} "
                            f"has been updated"
                            )
                show_entity(entity_type, entity_list) # displays updated list
            else:
                print("Operation cancelled.")
        except ValueError:
            print("Invalid indices. Please enter a valid one.")
    else:
        print("Returning previous menu.")
        

def edit_class(classes, professors): # edit classes
    selected_class = select_class() # asks to select a class
    if selected_class is None:
        return
    print(f"Editing class for {selected_class['Course']}.") # displays menu to edit class
    print("1 - Change Professor")
    print("2 - Change Course")
    edit_option = input("Select an option (1 - 2): ")
    edited = False # flag to know if changes were made
    if edit_option == '1': # asks to select a new professor
        new_professor = select_entity('professor', professors)
        if new_professor is None:
            print("Edit cancelled.")
        else: # verify if professor matches course
            if new_professor['Course'] != selected_class['Course']:
                print("Professor's course does not match the class course.")
            else:
                selected_class['Professor'] = new_professor
                edited = True
                print("Professor successfully changed.")
    elif edit_option == '2': # edits course
        new_course = select_course() # asks to select a new course
        if new_course: 
            if selected_class['Professor']['Course'] != new_course: # guarantee professor matches course
                print("Current Professor's Course does not match the new Course. Change Professor first.")
            else: # if matches, update class' course
                selected_class['Course'] = new_course
                edited = True
                print("Course successfully changed.")
        else:
            print("Edit cancelled.")
    if edited: # displays updated class
        show_classes(classes)


def edit_course_attempt(): # prevent course editions
    # reason why input used here is to ensure user will read the message
    input("You can not change any course. Press [ ENTER ] to continue.")
    return "Please consult the system administration."


'''=== DISPLAY FUNCTIONS ==='''    
def show_enrollments(enrollments, students, classes): # display enrollment
    if not students or not classes: # verifies if there is students and classes
        print("No Students nor Classes found. Enrollment can not be listed.")
        return
    if not enrollments: # verify if there is any enrollment
        print("No students enrolled in any class yet.")
        return
    print("\n=== Enrollments ===") # awnt, formated display 🥺
    for enrollment in enrollments:
        student = None # searches among enrollment for the 'StudentID'
        for current_student in students:
            if current_student['ID'] == enrollment['StudentID']:
                student = current_student
                break # breaks when student found
        class_ = None # same as above but for classes
        for current_class in classes:
            if current_class['ID'] == enrollment['ClassID']:
                class_ = current_class
                break
        if student and class_: # if student and class, display details
            print(
                f"Student: {student['Name']} {student['Surname']}, "
                f"CPF: {format_cpf(student['CPF'])}, "
                f"Course: {class_['Course']}, "
                f"Class ID: {class_['ID']}"
            )
    print(f"Total enrollment: {len(enrollments)}") 

    
def show_entity(entity_type, entity): # display "ENTITY" 
    if not entity: # verifies if list is empty
        print(f"No registered {entity_type}s yet")
        return 
    print(f"\n=== {entity_type.strip().capitalize()}s ===") # formated header * - *
    for i, entity in enumerate(entity):
        print( # displays the entity list with an index for better readability
            f"{i} - ID: {entity['ID']}"
            f"Full name: {entity['Name']} {entity['Surname']},"
            f"CPF: {format_cpf(entity['CPF'])},"
            f"Course: {entity['Course']}"
        )                        
        

def show_classes(classes): # display classses
    if not classes: # verifies if list is not empty
        print("No registered classes yet.")
        return
    print("\n=== Classes ===") # header yay
    for i, class_ in enumerate(classes):
        professor = class_['Professor'] # iterates list to display each one
        students_count = len(class_['Students'])
        print( # intention indent for a diversified display
            f"{i} - ID: {class_['ID']}, "
            f"Course: {class_['Course']}, "
            f"Professor: {professor['Name']} {professor['Surname']}, "
            f"ID: {professor['ID']}, "
            f"Students Enrolled: {students_count}/20"
        )
        if students_count > 0: 
            print(" Enrolled students:") # same as above
            for j, student in enumerate(class_['Students']):
                print(
                        f"{j} - {student['Name']} {student['Surname']}"
                        f"ID: {student['ID']}"
                    )


def show_course_details(course_menu, classes): # displays course details
    if not course_menu: # guerantee that the menu exists (if it doesn't I'm worried)
        print("No course available.")
        return
    print("\n=== Available Courses ===") # Header? Header!
    for key, course in course_menu.items():
        print(f"{key}: {course}") # displays the COURSE_MENU dictionary
    key_input = input("Select a course to view details: ")
    if key_input in course_menu: # verifies if the key is valid
        selected_course = course_menu[key_input]
        print(f"\n=== Details for {selected_course} ===")
        course_classes = [] # filters if classes list matches selected course
        for class_ in classes:
            if class_['Course'] == selected_course:
                course_classes.append(class_)
        if not course_classes: # if no class, print there is no class
            print("No Classes available for this course.")
            return
        print(f"\nClasses for {selected_course}: ")
        for i, class_ in enumerate(course_classes):
            professor = class_["Professor"] # if filtered classes, iterate the lsit to display
            students_count = len(class_['Students'])
            print( # display several data about the course
                f"{i}. - ID: {class_['ID']}, "
                f"Professor: {professor['Name']} {professor['Surname']}, "
                f"ID ({professor['ID']}, CPF: {format_cpf(professor['CPF'])}), "
                f"Course: {professor['Course']}, "
                f"Students Enrolled: {students_count}/20"
            )
            if students_count > 0:
                print("  Enrolled Students:")
                for j, student in enumerate(class_['Students']):
                    print( # more data yay
                        f"  {j} - {student['Name']} {student['Surname']}, "
                        f"ID: ({student['ID']}, CPF: {format_cpf(student['CPF'])}), "
                        f"Course: {student['Course']}"
                    )
    else:
        print("Invalid course key.")

        
def show_menu(title, options, extra): # displays the menus
    print(f"\n=== {title} ===") #Header!!! \o/
    for key, value in options.items(): # iterate about dictionary to print each item and key
        print(f"{key} - {value}")
    if extra: # adds an extra option that's not in dictionary
        print(extra)


def finish_operation(): # finish
    while True:
        finish = input("Do you want to Continue? [Y = Yes | N = No | Q = Quit]: ").upper().strip()
        if finish == 'Y':
            print("Operation successfully finished...")
            return 'Continue' # flags to continue same screen
        elif finish == 'N':
            print("Returning previous menu...")
            return 'Back' # flags to break and back to previous menu
        elif finish == 'Q':
            print("Quitting program...")
            return 'Quit' # finishes the program!!!
        else:
            print("Invalid option.") # asks for valid input

        
''' === MAIN LOOP(yay) ==='''
finish_all = False # controlls the looping execution
students, professors, classes, enrollments = load_data() # will read the file data.json
while True: 
    show_menu('MAIN MENU', MAIN_MENU, "X - Exit") # displays the MAIN MENU e fetch user's choice
    option = input("Select an Option: ").upper().strip()
    if option == 'X': # if x, breaks looping and quit program
        print("Exiting system...")
        save_data(students, professors, classes, enrollments) # will save data at file data.json
        break
    elif option not in MAIN_MENU: # if invalid option, returns main menu
        print("Invalid Option.")
        continue
    else: # if valid, access OPERATION MENU
        print(f"The selected Option is: {MAIN_MENU[option]}")
        
    while True: # Looping about CRUD: Include, List, Exclude and Edit
        show_menu('OPERATION MENU', OPERATION_MENU, 'Q - Quit Program')
        operation = input("Select an Operation: ").upper().strip() 
        if operation == 'A': # Include
            if option == 'A':
                add_entity('student', students)
            elif option == 'B':
                add_entity('professor', professors)
            elif option == 'C':
                attempt = edit_course_attempt()
            elif option == 'D':
                add_class(classes, professors)
            elif option == 'E':
                add_enrollment(classes, students, enrollments)
            
        elif operation == 'B': # List
            if option == 'A':
                show_entity('student', students)
            elif option == 'B':
                show_entity('professor', professors)
            elif option == 'C':
                show_course_details(COURSE_MENU, classes)
            elif option == 'D':
                show_classes(classes)
            elif option == 'E':
                show_enrollments(enrollments, students, classes)
        
        elif operation == 'C': # Edit/Change
            if option == 'A':
                edit_entity('student', students)
            elif option == 'B':
                edit_entity('professor', professors)
            elif option == 'C':
                attempt = edit_course_attempt()
                print(attempt)
            elif option == 'D':
                edit_class(classes, professors)
            elif option == 'E':
                print()
            
        elif operation == 'D': # Exclude
            if option == 'A':
                remove_entity('student', students, classes, enrollments)
            elif option == 'B':
                remove_entity('professor', professors, classes)
            elif option == 'C':
                attempt = edit_course_attempt()
                print(attempt)    
            elif option == 'D':
                remove_class(classes, enrollments)
            elif option == 'E':
                remove_enrollment(enrollments, students, classes)
                                  
        elif operation == 'X': # Back to main menu
            print("Returning to main menu...")
            break
        elif operation == 'Q': # Closes program
            print("Quitting program...")
            finish_all = True
            break
        else: # If invalid!!!
            print("Invalid operation, try again.")
            
        action = finish_operation() # calls function for next action and controls the flow
        if action == 'Continue':
           continue # skips to next iteration loop
        elif action == 'Back':
            break # breaks the actual loop (backs to previous menu)
        elif action == 'Quit':
            finish_all = True # breaks the external loop
            break # breaks the actual loop
    if finish_all:
        save_data(students, professors, classes, enrollments) # will save data at file data.json
        break
    
    