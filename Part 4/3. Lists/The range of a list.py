def range_of_list(x):
    return max(x) - min(x)


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5,]
    result = range_of_list(list)
    print("The range of my list is", result)