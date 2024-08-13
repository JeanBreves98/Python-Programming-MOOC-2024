def palindromes(string):
    list1 = list(string)
    reverse_list = [list1[len(list1) - i]
        for i in range(1, len(list1)+1)]
    if list1 == reverse_list:
        return True
    else:
        return False


while True:
    string = input("Please type in a palyndrome: ")
    if palindromes(string) == True:
        print(f"{string} is a palindrome!")
        break
    else: print("that wasn't a palindrome")