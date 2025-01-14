import json

try:
    
    try:
        with open('voting.json', 'r', encoding='utf-8') as f:
            file = json.load(f)
    except FileNotFoundError as e:
        file = {}

    person_name = input('Name of the person you are voting for:')

    if person_name in file:
        file[person_name] += 1
    else:
        file[person_name] = 1

    with open('voting.json', 'w', encoding='utf-8') as f:
        json.dump(file, f, ensure_ascii=False)

except Exception as e:
    print(f"An error occurred: {e}")
