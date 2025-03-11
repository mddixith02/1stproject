students = {}

def display_menu():
    print("\nMenu:")
    print("1. Display All Scores")
    print("2. Find Highest Scorer")
    print("3. Find Lowest Scorer")
    print("4. Calculate Average Score")
    print("5. Count Above/Below Average")
    print("6. Exit")

def enter_scores():
    while True:
        name = input("Enter student name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        if name in students:
            print("Student name must be unique. Try again.")
            continue
        if name == "John Doe":
            print("John Doe, we have been expecting you!")
        score = input(f"Enter {name}'s score: ")
        if score.isdigit():
            score = int(score)
            if score >= 0 and score <= 100:
                students[name] = score
            else:
                print("Score must be between 0 and 100. Try again.")
        else:
            print("Invalid input. Please enter a valid integer score.")

def display_scores():
    if len(students) == 0:
        print("No scores available.")
    else:
        print("\nStudent Scores:")
        for name, score in students.items():
            print(f"{name} - {score}")

def find_highest_scorer():
    if len(students) == 0:
        print("No scores available.")
        return
    highest_score = -1
    highest_scorer = ""
    for name, score in students.items():
        if score > highest_score:
            highest_score = score
            highest_scorer = name
    print(f"Highest Scorer: {highest_scorer} with {highest_score} points.")

def find_lowest_scorer():
    if len(students) == 0:
        print("No scores available.")
        return
    lowest_score = 101
    lowest_scorer = ""
    for name, score in students.items():
        if score < lowest_score:
            lowest_score = score
            lowest_scorer = name
    print(f"Lowest Scorer: {lowest_scorer} with {lowest_score} points.")

def calculate_average():
    if len(students) == 0:
        print("No scores available.")
        return
    total_score = 0
    for score in students.values():
        total_score += score
    average = total_score / len(students)
    print(f"Average Score: {average:.2f}")
    return average

def count_above_below_average():
    if len(students) == 0:
        print("No scores available.")
        return
    average = calculate_average()
    above = 0
    below = 0
    for score in students.values():
        if score > average:
            above += 1
        elif score < average:
            below += 1
    print(f"Students above average: {above}")
    print(f"Students below average: {below}")

def main():
    while True:
        enter_scores()
        while True:
            display_menu()
            choice = input("Choose an option: ")
            if choice == "1":
                display_scores()
            elif choice == "2":
                find_highest_scorer()
            elif choice == "3":
                find_lowest_scorer()
            elif choice == "4":
                calculate_average()
            elif choice == "5":
                count_above_below_average()
            elif choice == "6":
                print("Exiting...")
                return
            else:
                print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
