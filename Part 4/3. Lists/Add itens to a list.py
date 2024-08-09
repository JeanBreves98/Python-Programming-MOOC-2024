list = []
items = 0
i = 1

items = int(input("How many items:"))

while i <= items:
    element = int(input(f"Item {i}:"))
    list.append(element)
    i += 1

print(list)