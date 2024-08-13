def even_numbers(list1):
    even_list = []
    for i in list1:
        if i % 2 == 0:
            even_list.append(i)
    
    return even_list


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    new_list = even_numbers(list1)

    print("original", list1)
    print("new", new_list)