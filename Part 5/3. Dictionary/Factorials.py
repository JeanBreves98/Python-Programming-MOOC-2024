def factorials(n: int):
    dictionary = {}
    i = 1
    
    for i in range(i, n + 1):
        if i == 1:
            dictionary[i] = 1
        else:
            dictionary[i] = dictionary[i - 1] * i
    
    return dictionary


if __name__ == "__main__":

    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])