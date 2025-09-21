# Flowchart for the CRUD system:

[ START ]

MAIN MENU:

Options:    
(A) Student 
(B) Professor   
(C) Course  
(D) Class   
(E) Enrollment  
(X) Exit    
Choose an option    
If = (X) Exit   
Saves data  
[ END ]

Else if = (A) Student or (B) Professor  
Displays: "Selected option: {Student|Professor}"    
SECONDARY MENU  
(A) Add     
Requests: Name, Surname, CPF, Course    
Validates inputs    
Confirms    
If yes: Adds to list, displays list     
If no: Cancels, returns to submenu  
(B) List    
Displays: ID, Name, Surname, CPF, Course    
Returns to submenu  
(C) Edit    
Displays list, selects indexes  
Chooses: Name, Surname, CPF, Course     
Validates: confirms, updates and displays updated list  
Cancels: Returns to submenu 
(D) Delete  
Displays list, selects indexes  
Confirms    
If yes: Removes from list, updates classes/enrollments  
If no: Cancels and displays updated list    
Returns to submenu  
(X) Back    
Returns to MAIN MENU    
(Q) Quit    
Saves data  
[ END ]
    
(C) Course  
SECONDARY MENU  
(A) Add, (C) Edit, (D) Delete   
Displays: "You cannot change courses"   
Waits for [ENTER]   
Returns to submenu  
(B) List    
Displays available courses  
Selects course  
If valid: Displays classes, professor, students     
If invalid: Error message   
Returns to submenu  
(X) Back    
Returns to MAIN MENU    
(Q) Quit    
Saves data  
[ END ]

(D) Class   
SECONDARY MENU  
(A) Add     
Selects course, professor   
Validates: Class limit, professor's course  
Confirms    
If yes: Adds class, displays classes    
If no: Cancels  
Returns to submenu  
(B) List    
Displays: ID, Course, Professor, Students   
Returns to submenu  
(C) Edit    
Selects class   
Chooses: Professor or Course    
Validates, updates, displays classes    
Cancels: Returns to submenu 
(D) Delete  
Selects class, confirms     
If yes: Removes class and enrollments, displays classes     
If no: Cancels  
Returns to submenu  
(X) Back    
Returns to MAIN MENU    
(Q) Quit    
Saves data  
[ END ]

(E) Enrollment  
SECONDARY MENU  
(A) Add     
Selects class, student  
Validates: Student limit, compatible course     
Confirms    
If yes: Adds enrollment, displays classes   
If no: Cancels  
Returns to submenu  
(B) List    
Displays: Professor, Student, Course, IDs   
Returns to submenu  
(C) Edit    
No action (empty)   
Returns to submenu  
(D) Delete  
Selects class, student  
Confirms    
If yes: Removes enrollment, displays enrollments    
If no: Cancels  
Returns to submenu  
(X) Back    
Returns to MAIN MENU    
(Q) Quit    
Saves data  
[ END ]

AFTER EACH OPERATION    
(Y) Continue:   
Repeats SECONDARY MENU  
(N) Back:   
Returns to MAIN MENU    
(Q) Quit:   
Saves data  
[ END ]