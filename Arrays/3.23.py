# A variable contains text:

# An apple a day keeps the doctor away

# Create a module MyText, containing:

# A function that returns the number of words in the text
# A function that returns an ordered array of words, from longest to shortest
# A function that returns an alphabetically ordered array of words
# Then, write a program, call the functions and print results. Sample result:

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