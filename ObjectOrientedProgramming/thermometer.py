class Thermometer:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print("Turning on...")
        else:
            print("Your termometer is already on!")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print("Turning off...")
        else:
            print("Your termometer is already off!")

    def measure_and_display_temp(self):
        import random

        if not self.is_on:
            print("The thermometer is off. Please turn it on first.")

        temp = round(random.uniform(34, 42), 1)
        if temp >= 37 and temp < 41:
            print(f"Temperature: {temp}C (fever)")
        elif temp >= 41:
            print(f"Temperature: {temp}C (fever) CRITICAL TEMPERATURE!!")
        else:
            print(f"Temperature: {temp}C OK")
