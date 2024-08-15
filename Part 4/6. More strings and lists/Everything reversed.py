def everything_reversed(my_list):
    reversed_list = []

    for item in my_list:
        string = item
        string = item[::-1]
        reversed_list.append(string)
        
    reversed_list = reversed_list[::-1]

    return reversed_list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)