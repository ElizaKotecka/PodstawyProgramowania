class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f"Distance: {self.distance}. Rate per km: {self.rate_per_km}. Fare: {self.fare}.")


def main():
    taxi1 = TaxiRide(5)
    taxi2 = TaxiRide(7)
    taxi1.calculate_fare(15)
    taxi2.calculate_fare(30)

    taxi1.print_receipt()
    taxi2.print_receipt()


if __name__ == "__main__":
    main()