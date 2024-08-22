def double_items(numbers: list):
    doubled_list = numbers[:]
    index = 0

    for index in range(len(numbers)):
        doubled_list[index] = numbers[index] * 2
        
    return doubled_list


if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)

    print("original:", numbers)
    print("doubled:", numbers_doubled)