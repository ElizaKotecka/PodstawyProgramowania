###
# Credit card payment 
#140, 499, 500, 501, 720
account_balance = 500
total_payment = int(input("Your total payment is:"))

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')