times = float(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
groceries = float(input("How much monehy do you spend on groceries in a week?"))
food_expenses = times * price + groceries

print("Average food expenditure:")
print(f"Daily: {food_expenses / 7} euros")
print(f"Weekly: {food_expenses} euros")