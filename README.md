# Quiz-Game
A quiz game that asks users multiple-choice questions
Imports modules: None required in this version.
Defines quiz content:
questions: A list of trivia questions (replace with your own).
options: A list of nested lists containing answer options for each question.
answers: A list of correct answers for each question.
Initializes variables:
guesses: An empty list to store user guesses.
score: Set to 0 to track correct answers.
question_num: Set to 0 to track the current question.
Iterates through questions:
for question in questions: Loops through each question in the list.
print("########################"): Adds a visual separator for each question.
print(question): Prints the current question.
for option in options[question_num]: Iterates through the answer options for the current question.
print(option): Displays each option.
guess = input("enter the options A,B,C,D:").upper(): Prompts the user for their answer and converts it to uppercase.
guesses.append(guess): Adds the user's guess to the guesses list.
if guess == answers[question_num]: Checks if the guess is correct.
score += 1: Increments the score if the answer is correct.
print("CORRECT"): Provides positive feedback.
else: If the answer is incorrect.
print("INCORRECT"): Provides negative feedback.
print(f"{answers[question_num]} is the correct answer"): Reveals the correct answer.
question_num += 1: Moves to the next question.
Shows results:
print("   Results  "): Headers for results.
print("answers: ",end=""): Prints answer labels.
for answer in answers: Iterates through correct answers.
print(answer,end=" "): Prints each answer.
print(): Inserts a newline.
print("guesses: ",end=""): Prints guess labels.
for guess in guesses: Iterates through user guesses.
print(guess,end=" "): Prints each guess.
print(): Inserts a newline.
score = int(score/len(questions)*100): Calculates the percentage score.
print(f"your score is:{score}%"): Displays the calculated score.
print("Do you want to play again?"): Asks the user if they want to replay.
