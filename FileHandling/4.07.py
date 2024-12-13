import re

# Function to count vowels using regular expressions
def count_vowels(text):
    vowels = re.findall('[aeiouAEIOU]', text)
    return len(vowels)

text = input("Enter a text: ")
vowel_count = count_vowels(text)
print(f"The number of vowels in the entered text is: {vowel_count}")