hourly_wage = float(input("Hourly wage:"))
hours_worked = float(input("Hours worked:"))
day = input("Day of the week:")
daily_wages = hourly_wage * hours_worked
if day == "Sunday":
    print(f"Daily wages: {daily_wages * 2} euros")
else:
    print(f"Daily wages: {daily_wages} euros")