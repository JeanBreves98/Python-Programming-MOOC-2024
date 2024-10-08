def same_chars(string, index1, index2):
    if index1 >= len(string) or index2 >= len(string) or index1 < 0 or index2 < 0:
        return False
    elif string[index1] == string[index2]:
        return True
    else:
        return False


if __name__ == "__main__":
    # same characters m and m
    print(same_chars("programmer", 6, 7)) # True
    # different characters p and r
    print(same_chars("programmer", 0, 4)) # False
    # the second index is not within the string
    print(same_chars("programmer", 0, 12)) # False
    print(same_chars("abc", 0, 3))