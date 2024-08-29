def create_tuple(x: int, y: int, z: int):
    check = []
    check.append(x)
    check.append(y)
    check.append(z)
    smallest = x
    greatest = x
    list_sum = sum(check)

    for item in check:
        if item < smallest:
            smallest = item
        if item > greatest:
            greatest = item

    my_tuple = (smallest, greatest, list_sum)

    return my_tuple
    
    
if __name__ == "__main__":
    print(create_tuple(5, 3, -1))