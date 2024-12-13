# Then, write a program, call the functions and print results.

# Text: An apple a day keeps the doctor away
# Number of words: 8
# Words from the longest: doctor,apple,…
# Words ordered alphabetically: a,An,apple,away,…

from MyText import count_words, longest_to_shortest, alphabetically

text = "An apple a day keeps the doctor away"

print("Text:", text)
print("Number of words:", count_words(text))
print("Words from the longest:", longest_to_shortest(text))
print("Words ordered alphabetically:", alphabetically(text))