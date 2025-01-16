class C:
    def __init__(self, sectors):
        self.sectors = sectors

    def m1(self, s, n):
        self.sectors[s] = n

    def m2(self, s):
        result = 0
        for elem in s:
            if elem in self.sectors:
                result += self.sectors[elem]
        return result

def main():
    stadium = C({"A": 120, "D": 150, "G": 90, "K": 110})

    stadium.m1("G", 130)
    stadium.m1('E', 100)

    print("Fans in sectors GD:", stadium.m2("GD"))  # 280
    print("Fans in sectors KEJ:", stadium.m2("KEJ"))  # 210

if __name__ == "__main__":
    main()