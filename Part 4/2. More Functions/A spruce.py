def spruce(size):
    body = '*'
    i = 1
    k = 1
    space = size - 1
    blank = (space * " ")

    print("a spruce!")
    print(blank + (body * k) + blank)
    
    while i < size:
        space -= 1
        blank = space * " "
        k += 2
        i += 1
        print(blank + (body * k) + blank)
        
    print((size - 1) * " " + "*" + (size - 1) * " ")


if __name__ == "__main__":
    size = 7
    base = (size - 1) * 2 + 1
    spruce(size)