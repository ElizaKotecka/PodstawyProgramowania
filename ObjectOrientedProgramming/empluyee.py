class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        name_initial = self.name[0]

        if self.age >= 18:
            return f"{self.surname.upper()}{name_initial.upper()}{self.seniority}"
        else:
            return f"{self.surname.lower()}{name_initial.lower()}{self.seniority}"


def main():
    emp1 = C("Anna", "May", 17, 7)
    print(emp1)

    emp2 = C("George", "Brown", 21, 4)
    print(emp2)


if __name__ == "__main__":
    main()