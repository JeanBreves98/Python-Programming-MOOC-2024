def mean(list):
    return sum(list) / len(list)


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    result = mean(list)
    print("mean value is", result)