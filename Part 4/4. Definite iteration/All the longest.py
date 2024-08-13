def all_the_longest(my_list):
    longest = my_list[0]
    longest_list = []
    
    for i in my_list:
        if len(i) > len(longest):
            longest = i
    
    for i in my_list:
        if len(i) is len(longest):
            longest_list.append(i)
    return longest_list


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)

    print(result)