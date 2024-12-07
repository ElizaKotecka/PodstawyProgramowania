# Write a program that checks if the PIN code entered in the payment terminal is correct.
# The user has up to three possibilities for entering a PIN code.
# In case of three unsuccessful attempts, the card is blocked.

correct_pin = "0805"
max_attempts = 3

while max_attempts > 0:
    entered_pin = input("Enter the PIN code: ")
    
    if entered_pin == correct_pin:
        print("PIN code correct.")
        break
    else:
        print("Incorrect PIN. Try again.")
        max_attempts -= 1
        
else:
    print("Sorry, your payment card has been blocked.")


