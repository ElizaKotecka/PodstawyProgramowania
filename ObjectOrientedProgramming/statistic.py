import statistics

class Statistics:
    def __init__(self):
        self.numbers = []

    def add_to_list(self, number):
        self.numbers.append(number)
    
    def display(self):
        return '-'.join(self.numbers)
    
    def greatest(self):
        return max(self.numbers)
    
    def smallest(self):
        return min(self.numbers)
    
    def arth_mean(self):
        return statistics.mean(self.numbers)

    def median_of_num(self):
        return statistics.median(self.numbers)
    
    def print_statistics(self):
        print(f"Minimum: {self.smallest()}")
        print(f"Maximum: {self.greatest()}")
        print(f"Arithmetic Mean: {self.arth_mean():.2f}")
        print(f"Median: {self.median_of_num()}")


