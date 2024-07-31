limit = int(input("Limit:"))
sum = 0
num = 1
consecutive_sum = ""

while sum < limit:
    sum += num
    consecutive_sum += str(num)
    if sum < limit:
        consecutive_sum += " + "
    num += 1
print(f"The consecutive sum: {consecutive_sum} = {sum}")