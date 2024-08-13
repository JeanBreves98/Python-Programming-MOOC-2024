def distinct_numbers(list1):
    list1.sort()
    distinct = []
    distinct.append(list1[0])

    for i in list1:
        if i not in distinct:
            distinct.append(i)

    return distinct
       

if __name__ == "__main__":
    list1 = [3, 2, 2, 1, 3, 3, 1]

    print(distinct_numbers(list1)) # [1, 2, 3]