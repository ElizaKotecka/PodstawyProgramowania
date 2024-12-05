# ATM (cash machine) simulator

balance = 1000  # Initial balance
pin = '1111'  # Initial 4-digit PIN code
entered_pin = None
# Check PIN

while entered_pin != pin:
    entered_pin = input("Enter your 4-digit PIN: ")
    if entered_pin != pin:
        print(f"Incorrect PIN. Try again.")

# Main ATM menu
while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change PIN")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        while True:
            new_pin = input("Enter your new 4-digit PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                confirm_pin = input("Confirm your new PIN: ")
                if new_pin == confirm_pin:
                    pin = new_pin
                    print("PIN successfully changed!")
                    break
                else:
                    print("PINs do not match. Try again.")
            else:
                print("Invalid PIN format. Please enter exactly 4 digits.")
    elif choice == '5':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")