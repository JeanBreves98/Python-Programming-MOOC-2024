def longest_series_of_neighbours(my_list):
    new_list = []
    lenght = 0
    previous_item = 0

    for item in my_list:
        if item - previous_item == 1 or item - previous_item == -1:
            new_list.append(item)
            if len(new_list) > lenght:
                lenght = len(new_list)
        else:
            new_list = [item]
        previous_item = item

    return lenght




if __name__ == "__main__": 
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
    my_list = [1,2]
    print(longest_series_of_neighbours(my_list))
    my_list = [0]
    print(longest_series_of_neighbours(my_list))