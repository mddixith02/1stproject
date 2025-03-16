# Student Analyzer

## ABSTRACT
In this project I have done apython script to analyze the student scores , the program is designed to analyze the scores of multiple students on a same time.
In this I have added functionalities like including calculating the highest and lowest scores, determining the average score, and counting students who scored above or below average. It also ensures proper data validation and prevents duplicate entries. 
Additionally, a special condition is included where entering a student named "John Doe" triggers a unique message.

## Project Goals
The primary objectives of this project include:
- Allowing users to enter and store student names along with their respective scores.
- Displaying all entered student scores in an organized format.
- Identifying the student(s) with the highest and lowest scores.
- Calculating and displaying the average score.
- Counting the number of students who scored above or below the average.
- Ensuring valid input and preventing duplicate student entries.
- Providing a menu-driven interface for smooth user interaction.

## Data Input
- Users will enter student names and their respective scores.
- Names must be unique to avoid duplicate entries.
- Scores must be within the range of **0 to 100**.
- Typing **'done'** stops the input process.

## Functions included
The project is implemented using Python and follows a structured modular approach with functions handling different operations:
- `score_entry()`: Captures student names and scores with validation.
- `score_board()`: Displays all entered scores.
- `topper()`: Identifies the highest scorer(s).
- `stupid()`: Identifies the lowest scorer(s).
- `average()`: Computes the average score.
- `count_above_below_average()`: Counts students above and below average.
- `main_menu()`: Displays the menu options.
- `main()`: Controls the program flow and user interaction.

## Edge Cases Considered
- **No student entries**: Displays appropriate messages if no scores are available.
- **Duplicate names**: Prevents duplicate student name entries.
- **Invalid inputs**: Ensures only numeric scores between 0 and 100 are accepted.
- **Special message for "John Doe"**: Prints a unique message when the name is entered.
- **Handling ties**: Displays multiple students if they have the same highest/lowest score.

## Conclusion
The **Student Score Analyzer** provides an efficient and user-friendly way to manage and analyze student scores. The program ensures accuracy through data validation and helps users gain insights into student performance using various statistical operations. This project can be extended in multiple ways to enhance usability and data handling capabilities.
