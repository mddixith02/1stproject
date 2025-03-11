student = {} # using empty dictionary for data input

def main_menu(): # defining main_menu function for providing options to the user
    print("\nMenu")
    print("1. All scores")
    print("2. Highest Score")
    print("3. Lowest score")
    print("4. Avg Score")
    print("5. Above Avg/Below Avg Score")
    print("6. Exit the menu!!")

def score_entry(): # defining score_entry function for the student name and student score input
    while True:
        name = input("Enter Student name")
        if name == done or Done: # conditional statement to stop the loop of taking input from the user
            break
        if name in student: # conditional statement to avoid same values
            print("Entry already exist")
        if name == "Atyeti": # giving special condition for the name Atyeti
            print("Always Deliver More than Expected")
        score = int(input("Enter Student's score"))
        try:  # using try and except block to avoid the invalid values
            if 0 <= score <= 100:
                students[name] = score
            else:
                print("Invalid Input. Enter b/w 1 - 100")
        except ValueError:
            print("Invalid Input")

def score_board(): #defining score_board function to print all the user integrated values
    if len(student) == 0: # using conditional statement to handle no value exception
        print("Entries aren't available")
    else:
        print("\nStudent Scores:")
        for name in students:  
            score = students[name]  # Accessing score using the name as the key
            print(name + '-' + score)

def topper():
    if len(student) == 0:  
        print("Entries aren't available")
    else:
        higest_score = -1 # initializing variable for score comaprision
        highest_scorer = ''  # initializing empty variable to store the name of the highest scorer
        for name in students:  # Iterate over the dictionary student names
                score = students[name]  # Accessing score using the name as the key
            if score > highest_score:
                highest_score = score
                highest_scorer = name
        print(highest_scorer + '-' + highest_score + "scored higest marks among all the students")

def stupid():
    if len(Student) == 0:
        print("Entries aren't available")
    else:
        lowest_score = 101
        lowest_scorer = ""
        for name in students:  
                score = students[name]  
            if score < lowest_score:
                lowest_score = score
                lowest_scorer = name
        print(lowest_scorer + '-' + lowest_score + "scored lowest marks among all the students")
    
