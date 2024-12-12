# Calculates which expense category was the most expensive.

categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

most_expensive_index = expenses.index(max(expenses))
most_expensive = categories[most_expensive_index]

print("The most expensive category is:", most_expensive)

