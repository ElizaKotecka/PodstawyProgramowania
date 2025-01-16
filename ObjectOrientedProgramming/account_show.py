from account import Bank

def main():
    account1 = Bank('12 3456 5555 9090 1111 0000 7722', )
    account1.display()
    account1.deposit()
    account1.display()
    account1.withdraw()
    account1.withdraw()
    account1.display()

if __name__ == '__main__':
    main()
