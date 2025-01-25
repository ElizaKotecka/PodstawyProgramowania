temperatures = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

positive_temperatures = filter(lambda city: temperatures[city] > 0, temperatures)

# Print the result
print("Cities with positive temperatures:", ", ".join(positive_temperatures))