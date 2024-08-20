def who_won(game_board: list):
    player1 = 0
    player2 = 0
    
    for row in game_board:
        for piece in row:
            if piece == 1:
                player1 += 1
            elif piece == 2:
                player2 += 1

    if player1 > player2:
        return 1
    elif player1 < player2:
        return 2
    else: 
        return 0    


if __name__ == "__main__":
    board1 = [
    [1, 0, 2],
    [1, 2, 0],
    [1, 1, 0]
]
    board2 = [
    [2, 2, 0, 0],
    [1, 2, 2, 0],
    [0, 1, 2, 2],
    [0, 0, 1, 2]
]
    board3 = [
    [1, 0, 2, 1, 2], 
    [2, 1, 1, 2, 0],
    [0, 1, 0, 2, 0], 
    [1, 2, 0, 1, 2], 
    [2, 1, 0, 2, 1] 
]
    print(who_won(board1))
    print(who_won(board2))
    print(who_won(board3))