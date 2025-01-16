from statistic import Statistics

def main():
    stat1 = Statistics()


    while len(stat1.numbers) <5:
        try:
            number = float(input('Enter a number: '))
            stat1.add_to_list(number)
        except ValueError:
            print("Wrong input")

    stat1.print_statistics()

if __name__ == '__main__':
    main()