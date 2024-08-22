def sudoku_grid_correct(sudoku: list):
    row_bolean = row_correct(sudoku)

    if row_bolean == False:
        return False
    column_bolean = column_correct(sudoku)
    if column_bolean == False:
        return False
    block_bolean = block_correct(sudoku)
    if block_bolean == False:
        return False
    
    return True


def row_correct(sudoku: list):
    index = 0
    row_list = []
    
    while index < 9:
        for item in sudoku[index]:
            if item != 0:
                if item in row_list:
                    return False
                else:
                    row_list.append(item)
        index += 1
        row_list.clear()

    return True


def column_correct(sudoku: list):
    column_list = []
    column_no = 0

    while column_no < 9:
        for row in sudoku:
            item = row[column_no]
            if item != 0:
                if item in column_list:
                    return False
                else:
                    column_list.append(item)
        column_no += 1
        column_list.clear()
    return True


def block_correct(sudoku: list):
    block_list = []
    row_no = 0

    while row_no < 9:
        column_no = 0
        while column_no < 9:
            block_list.clear()
            for row in range(row_no, row_no + 3):
                for column in range(column_no, column_no + 3):
                    item = sudoku[row][column]
                    if item != 0:
                        if item in block_list:
                            return False
                        block_list.append(item)
            column_no += 3
        row_no += 3 
        
    
    return True


if __name__ == "__main__":
    sudoku1 = [
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

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))

    sudoku3 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 6, 0, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]
    print(sudoku_grid_correct(sudoku3))  # Should print False (duplicate 6 in third block)