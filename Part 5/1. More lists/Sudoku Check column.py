def column_correct(sudoku: list, column_no: int):
    column_list = []

    for row in sudoku:
        item = row[column_no]
        if item != 0:
            if item in column_list:
                return False
            else:
                column_list.append(item)

    return True


if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(column_correct(sudoku, 0)) #False
    print(column_correct(sudoku, 1))  
    print(column_correct(sudoku, 2))
    print(column_correct(sudoku, 3))
    print(column_correct(sudoku, 4))
    print(column_correct(sudoku, 5))
    print(column_correct(sudoku, 6))
    print(column_correct(sudoku, 7))
    print(column_correct(sudoku, 8))