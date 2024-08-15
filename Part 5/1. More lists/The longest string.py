def longest(my_list: list):
    longest = my_list[0] 
    
    for i in my_list:
        if len(i) > len(longest):
            longest = i
    return longest


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]

    print(longest(strings))
