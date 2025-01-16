class Phone:
    def __init__(self, brand, model, colour):
        self.brand = brand
        self.model = model
        self.colour = colour
        self.is_on = False
        self.installed_apps = []

    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def power_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

    def install_app(self, app_name):
        if self.is_on:
            if app_name not in self.installed_apps:
                self.installed_apps.append(app_name)
                print(f"'{app_name}' has been installed.")
            else:
                print(f"'{app_name}' is already installed.")
        else:
            print("Cannot install apps while the phone is OFF.")

    def display_status(self):
        power_status = "ON" if self.is_on else "OFF"
        apps = ', '.join(self.installed_apps) if self.installed_apps else "No apps installed"
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Colour: {self.colour}")
        print(f"Power: {power_status}")
        print(f"Installed Apps: {apps}")



my_phone = Phone("Samsung", "Galaxy S22", "white")
my_phone.display_status()

print("\n--- Powering On ---")
my_phone.power_on()

print("\n--- Installing Apps ---")
my_phone.install_app("Instagram")
my_phone.install_app("Spotify")

print("\n--- Displaying Updated Status ---")
my_phone.display_status()

print("\n--- Powering Off ---")
my_phone.power_off()
