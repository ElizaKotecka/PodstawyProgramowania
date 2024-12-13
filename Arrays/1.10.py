###
# Prints test statistics

test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# calculates the number of test questions
num_of_questions = len(test_results)

# calculates the number of correct answers
correct_answers = 0
for answer in test_results:
    if answer:
        correct_answers += 1

# calculates the number of incorrect answers
incorrect_answers = num_of_questions - correct_answers

# calculates the percentage of correct answers
percentage_of_correct_answers = (correct_answers/num_of_questions) * 100

print('TEST STATISTICS')
print('===============')
print('Number of questions:', num_of_questions)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print(f'Percentage of correct answers: {percentage_of_correct_answers:.0f}%')
