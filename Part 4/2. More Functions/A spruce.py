def spruce(size):
    i = 1
    k = 1
    space = size - 1
    blank = (space * " ")
    print(blank + (body * k) + blank)
    
    while i < size:
        space -= 1
        blank = space * " "
        k += 2
        i += 1
        print(blank + (body * k) + blank)
        
    print((size - 1) * " " + "*" + (size - 1) * " ")
        
    
size = 7
body = '*'
base = (size - 1) * 2 + 1

spruce(size)