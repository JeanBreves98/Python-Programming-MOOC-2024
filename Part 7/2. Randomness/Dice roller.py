from random import *

def roll(die:str):
    a = [3, 3, 3, 3, 3, 6]
    b = [2, 2, 2, 5, 5, 5]
    c = [1, 4, 4, 4, 4, 4]

    if die == 'A':
        return choice(a)
    elif die == 'B':
        return choice(b)
    elif die == 'C':
        return choice(c)

def play(die1: str, die2: str, times: int):
    die1_list = []
    die2_list = []
    win1 = 0
    win2 = 0
    draw = 0

    for i in range(times):
        die1_list.append(roll(die1))

    for i in range(times):
        die2_list.append(roll(die2))

    for i in range(times):
        if die1_list[i] > die2_list[i]:
            win1 += 1
        elif die1_list[i] == die2_list[i]:
            win2 += 1
        else:
            draw += 1

    return (win1, win2, draw)

        
if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)