import json

favorite = {
    "title": "The City of Bones",
    "author": "Cassandra Clare",
    "genre": "Fantasy",
    "year": 2009,
    "core_characters": ['Clary Farchaild', 'Jace Herondale', ' Simon Lewis']
}

file_name = 'favourite.json'

with open(file_name, 'w') as f:
    json.dump(favorite, f, indent=4)

print("Data has been written to", file_name)

