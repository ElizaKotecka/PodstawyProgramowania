class C:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def m(self, n):
        first_quadrant_points = 0
        
        for x, y in self.coordinates:
            if x > 0 and y > 0:
                first_quadrant_points += 1

        return first_quadrant_points >= n


def main():
    points = C([[2, 3], [1, 8], [-6, 4], [3, -7]])

    print(points.m(2))  # True
    print(points.m(3))  # False


if __name__ == "__main__":
    main()