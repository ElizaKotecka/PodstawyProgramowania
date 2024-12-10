# Masks the card number. The function returns a character string in which
# only the first two and the last four digits of the card number are visible.
# The remaining digits of the card number are replaced with an asterisk.

def hide(card_number):

    first_part = card_number[:2]
    last_part = card_number[-4:]
    masked_part = '*' * (len(card_number) - len(first_part) - len(last_part))


    return first_part + masked_part + last_part
        

if __name__ == "__main__":
    print(hide("5290312400019022"))