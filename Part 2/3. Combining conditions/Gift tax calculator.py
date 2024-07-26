value = float(input("Value of gift:"))

if value >= 5000 and value < 25000:
    rate = 8/100
    tax = (100 + (value - 5000) * rate)
    print(f"Amount of tax: {tax} euros")
elif value >= 25000 and value < 55000:
    rate = 10/100
    tax = (1700 + (value - 25000) * rate)
    print(f"Amount of tax: {tax} euros")
elif value >= 55000 and value < 200000:
    rate = 12/100
    tax = (4700 + (value - 55000) * rate)
    print(f"Amount of tax: {tax} euros")
elif value >= 200000 and value < 1000000:
    rate = 15/100
    tax = (22100 + (value - 200000) * rate)
    print(f"Amount of tax: {tax} euros")
elif value >= 1000000:
    rate = 17/100
    tax =(142100 + (value - 1000000) * rate)
    print(f"Amount of tax: {tax} euros")
elif value < 5000:
    print("No tax!")