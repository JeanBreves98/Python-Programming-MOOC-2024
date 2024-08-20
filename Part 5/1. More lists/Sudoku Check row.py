def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    row_list = []
    
    for item in row:
        if item != 0:
            if item in row_list:
                return False
            else:
                row_list.append(item)

    return True


if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0], #True 
    [2, 0, 0, 2, 5, 0, 7, 0, 0], #False
    [0, 2, 0, 3, 0, 0, 0, 0, 4], #True
    [2, 9, 4, 0, 0, 0, 0, 0, 0], #True
    [0, 0, 0, 7, 3, 0, 5, 6, 0], #True
    [7, 0, 5, 0, 6, 0, 4, 0, 0], #True
    [0, 0, 7, 8, 0, 3, 9, 0, 0], #True
    [0, 0, 1, 0, 0, 0, 0, 0, 3], #True
    [3, 0, 0, 0, 0, 0, 0, 0, 2] #True
    ]

    print(row_correct(sudoku, 0))    
    print(row_correct(sudoku, 1))
    print(row_correct(sudoku, 2))
    print(row_correct(sudoku, 3))
    print(row_correct(sudoku, 4))
    print(row_correct(sudoku, 5))
    print(row_correct(sudoku, 6))
    print(row_correct(sudoku, 7))
    print(row_correct(sudoku, 8))
