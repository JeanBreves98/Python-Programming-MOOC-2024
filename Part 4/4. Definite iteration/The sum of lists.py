def list_sum(a,b):
    index = 0
    sum_list = []

    while index < len(a):
        sum = a[index] + b[index]
        sum_list.append(sum)
        index += 1
    return sum_list


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    
    print(list_sum(a, b)) # [8, 10, 12]