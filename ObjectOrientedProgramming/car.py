class Car:
    def __init__(self, brand, model, year):
        self.brand = brand  # Object attribute
        self.model = model  # Object attribute
        self.year = year    # Object attribute

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"


my_car = Car("Toyota", "Corolla", 2021)  # Creating an object of the Car class
my_car.display_info()  # Calling a method on the object
# Print the object
print(my_car)  # Output: 2021 Toyota Corolla