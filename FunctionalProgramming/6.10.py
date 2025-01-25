import matplotlib.pyplot as plt

cities = {
    "Krakow": 7,
    "Warszawa": -2,
    "Sopot": 4,
    "Koszalin": -1,
    "Opole": 3
}

city_names = cities.keys()
temperatures = cities.values()

# city_names = list(map(str, cities.keys()))
# temperatures = list(map(int, cities.values()))

plt.bar(city_names, temperatures, color='blue')

plt.title("Temperatures Recorded in Different Cities")
plt.xlabel("Cities")
plt.ylabel("Temperature (°C)")

# Displaying the chart
plt.show()
