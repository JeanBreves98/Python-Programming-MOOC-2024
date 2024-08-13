def sum_of_positives(list):
    sum_of_positives = 0
    for i in list:
        if i > 0:
            sum_of_positives += i
    return sum_of_positives

if __name__ == "__main__":  
    list = [1, -2, 3, -4, 5]
    result = sum_of_positives(list)
    print("The result is", result)