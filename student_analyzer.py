students = {}  # Using a dictionary to store student names and their scores

def main_menu():  # Function to display the main menu
    print("\nMenu")
    print("1 - Display All Scores")
    print("2 - Find Highest Scorer")
    print("3 - Find Lowest Scorer")   
    print("4 - Calculate Average Score")
    print("5 - Count Above/Below Average Scores")   
    print("6 - Exit the menu")

def score_entry():  # Function to input student names and scores
    while True:
        name = input("Enter Student name (or 'done' to finish): ").strip()
        if name.lower() == "done":  # Condition to stop taking inputs
            break
        if name in students:  # Ensure unique student names
            print("Entry already exists. Try again.")
            continue
        if name == "John Doe":  # Special condition for John Doe
            print("John Doe, we have been expecting you!")
        
        try:
            score = int(input("Enter Student's score (0-100): "))  # Ensure valid integer input
            if 0 <= score <= 100:  # Validate score range
                students[name] = score  # Store name and score in dictionary
            else:
                print("Invalid input. Enter a score between 0 and 100.")
        except ValueError:  # Handle non-integer inputs
            print("Invalid input. Please enter a valid integer score.")

def score_board():  # Function to display all student scores
    if not students:  # Check if dictionary is empty
        print("No entries available.")
    else:
        print("\nStudent Scores:")
        for name, score in students.items():  # Iterate over dictionary
            print(f"{name} - {score}")  # Display name and score

def topper():  # Function to find and display the highest scorer(s)
    if not students:
        print("No entries available.")
    else:
        highest_score = max(students.values())  # Find highest score
        highest_scorers = [name for name, score in students.items() if score == highest_score]  # Find all with highest score
        print(f"Highest Scorer(s): {', '.join(highest_scorers)} with {highest_score} points.")

def stupid():  # Function to find and display the lowest scorer(s)
    if not students:
        print("No entries available.")
    else:
        lowest_score = min(students.values())  # Find lowest score
        lowest_scorers = [name for name, score in students.items() if score == lowest_score]  # Find all with lowest score
        print(f"Lowest Scorer(s): {', '.join(lowest_scorers)} with {lowest_score} points.")

def average():  # Function to calculate and display the average score
    if not students:
        print("No scores available.")
    else:
        avg = sum(students.values()) / len(students)  # Compute average
        print(f"Average Score: {avg:.2f}")  # Display rounded average
        return avg  # Return the calculated average

def count_above_below_average():  # Function to count students above and below average
    if not students:
        print("No scores available.")
    else:
        avg = average()  # Get the average score
        above = sum(1 for score in students.values() if score > avg)  # Count students above average
        below = sum(1 for score in students.values() if score < avg)  # Count students below average
        print(f"Students above average: {above}")
        print(f"Students below average: {below}")

def main():  # Main function to run the program
    score_entry()  # Get student scores first
    while True:
        main_menu()  # Show menu options
        choice = input("Choose an option: ")  # Get user choice
        if choice == "1":
            score_board()  # Display all scores
        elif choice == "2":
            topper()  # Find and display highest scorer
        elif choice == "3":
            stupid()  # Find and display lowest scorer
        elif choice == "4":
            average()  # Calculate and display average score
        elif choice == "5":
            count_above_below_average()  # Count above/below average students
        elif choice == "6":
            print("Exiting program...")
            break  # Exit the loop and end the program
        else:
            print("Invalid option. Try again.")  # Handle invalid input

if __name__ == "__main__":
    main()  # Run the main function
