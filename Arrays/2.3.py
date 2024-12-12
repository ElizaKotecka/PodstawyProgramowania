# Write a program that calculates and prints:

# total expenses for each category
# total expenses for each week
# total expenses for a month


# Weekly expenses for different categories

# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements

food_total = 0
transport_total = 0
utilities_total = 0
week_total = [0, 0, 0, 0]
month_total = 0

for row in range(4):
    food_total += monthly_expenses[row][0]
    transport_total += monthly_expenses[row][1]
    utilities_total += monthly_expenses[row][2]
    week_total[row] = sum(monthly_expenses[row])

month_total = food_total + transport_total + utilities_total



# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food_total)
print('Transport:', transport_total)
print('Utilities:', utilities_total)
print('Week 1:', week_total[0])
print('Week 2:', week_total[1])
print('Week 3:', week_total[2])
print('Week 4:', week_total[3])
print('---------------')
print('TOTAL:', month_total)
