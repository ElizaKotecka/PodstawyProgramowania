import json

name = 'dogs.json'

with open(name, 'r') as file:
    f = json.load(file)

for element in f:
    if element['age'] < 5:
        for k, v in element.items():
            print(f"{k}: {v}")
    print()
    continue
