# True or False Quiz Application

This Python application implements a True or False quiz game where users are presented with a series of statements and must determine whether each statement is true or false.

## Functionality Overview

The application consists of several components:

### 1. QuestionModel Class

The `QuestionModel` class defines the structure of each quiz question. It contains two attributes:

- `text`: The statement or question presented to the user.
- `answer`: A string representing whether the statement is true or false.

### 2. QuizBrain Class

The `QuizBrain` class manages the quiz process. Its functionalities include:

- Keeping track of the questions available for the quiz.
- Tracking the user's current question number and score.
- Presenting questions to the user and processing their answers.
- Calculating the final score at the end of the quiz.

### 3. Main Program

The main program reads question data from an external source (`question_data`) and uses it to create instances of the `QuestionModel` class. It then initializes a `QuizBrain` object with the list of questions and starts the quiz.

After the user completes the quiz, the program displays the final score along with a summary of correct and incorrect answers.

## Usage

1. **Running the Program**: Execute the Python script to start the True or False quiz application.

    ```bash
    python quiz_app.py
    ```

2. **Answering Questions**: Users are presented with statements and prompted to input whether each statement is true or false.

3. **Scoring**: The program keeps track of the user's score as they progress through the quiz.

4. **Quiz Completion**: Once all questions are answered, the user is provided with their final score and a summary of correct and incorrect answers.

## Dependencies

- Python 3.x

## Contributing

Contributions to enhance the functionality, improve user experience, or fix issues of this quiz application are welcome. Feel free to fork the repository, make changes, and submit pull requests.
