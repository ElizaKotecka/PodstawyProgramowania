def eng_to_pl(word):
    translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
    }
    
    return translations.get(word, 'Translation unavailable')

print(eng_to_pl(input("Enter word in english:")))