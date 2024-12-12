# Create a module MyText, containing:

# A function that returns the number of words in the text
# A function that returns an ordered array of words, from longest to shortest
# A function that returns an alphabetically ordered array of words

def count_words(text):
    return len(text.split())

def longest_to_shortest(text):
    words = text.split()
    words.sort(key=len, reverse=True)
    return words

def alphabetically(text):
    text = text.lower()
    words = text.split()
    words.sort()
    return words

