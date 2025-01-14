import csv

try:
    province_dict = {}
    with open('province.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            province_dict[row[0]] = row[1]

except Exception as e:
    print(f"An error occurred: {e}")

# Initialize count for each province
vehicle_count = {key: 0 for key in province_dict.keys()}

try:

    with open('vehicle.txt', 'r') as file:
        for line in file:
            first_letter = line[0]

            # Check if the first letter matches a province letter
            if first_letter in vehicle_count:
                vehicle_count[first_letter] += 1

except Exception as e:
    print(f"An error occurred: {e}")

for letter, count in vehicle_count.items():
    print(f"Province {province_dict[letter]}: {count} vehicles.")
