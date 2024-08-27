def times_ten(start_index: int, end_index: int):
    dictionary = {}
    k = start_index

    for i in range(end_index + 1):
        if i >= start_index:
            dictionary[k] = k * 10
            k += 1

    return dictionary


if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)