number = int(input("Please type in a number:"))
i = 1
start = 1
end = number

while i <= number:
    print(start)
    if start == end:
        break
    print(end)
    start += 1
    if start == end:
        break
    end -= 1
    i += 1