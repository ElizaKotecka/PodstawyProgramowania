# Write a program that prints a survey consisting of three questions. Save the answers to logical type variables.

question_1 = input("Are you interested in computer science? (y/n): ") == 'y'
question_2 = input("Do you like playing computer games? (y/n): ") == 'y'
question_3 = input("Do you have an Instagram account? (y/n): ") == 'y'

print("SURVEY RESULTS")
print(f"Interested in computer science: {'Yes' if question_1 else 'No'}") #conditional expression (wyrażenie warunkowe)
print(f"Playing computer games: {'Yes' if question_2 else 'No'}")
print(f"Has an Instagram account: {'Yes' if question_3 else 'No'}")