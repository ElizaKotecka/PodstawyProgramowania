# Write a program that checks whether the EAN-13 number entered from the keyboard consists of exactly 13 characters (digits).
    
ean = input("Enter EAN-13: ")
    
if len(ean) == 13 and ean.isdigit():
    print("Article number is correct.")

    if ean.startswith('590'):
        print("Article manufactured in Poland.")
else:
    print("Invalid EAN-13 number.")