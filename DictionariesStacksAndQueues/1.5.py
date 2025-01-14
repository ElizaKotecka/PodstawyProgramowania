countries = [
{"name":"Poland", "population":38000000},
{"name":"Germany", "population":84480000},
{"name":"Japan", "population":124500000},
{"name":"Norway", "population":5520000},
{"name":"China", "population":1411000000},
]

print(f"{'COUNTRY':<10} {'POPULATION':<10}")

for country in countries:
    print(f"{country['name']:<10} {country['population']:<10}")