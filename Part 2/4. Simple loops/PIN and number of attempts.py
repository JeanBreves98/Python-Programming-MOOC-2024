attempts = 0
pin = "4321"
while True:
    attempted_pin = input("PIN:")
    attempts += 1
    if attempted_pin == pin and attempts == 1:
        print("Correct! It only took you one single attempt!")
        break
    elif attempted_pin == pin and attempts > 1:
        print(f"Correct! It took you {attempts} attempts")
        break
    else:
        print("Wrong")