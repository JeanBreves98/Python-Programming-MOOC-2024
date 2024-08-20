def sudoku_grid_correct(sudoku: list):
    row_bolean = row_correct(sudoku)
    column_bolean = column_correct(sudoku)
    block_bolean = block_correct(sudoku)

    if row_bolean == False or column_bolean == False or block_bolean == False:
        return False
    else: 
        return True


def row_correct(sudoku: list, row_no: int):
    row_list = []

    for row in sudoku:
        for item in row:
            item_list.append(item)
        if row_count == row_no:  
            break      
        row_count += 1
    
    for item in item_list:
        if item != 0:
            if item in row_list:
                return False
            else:
                row_list.append(item)

    return True


def column_correct(sudoku: list, column_no: int):
    item_list = []
    row_count = 0
    row_list = []

    for row in sudoku:
        for item in row:
            if item == row[column_no]:
                item_list.append(row[column_no])

    for item in item_list:
        if item != 0:
            if item in row_list:
                return False
            else:
                row_list.append(item)

    return True


def block_correct(sudoku: list, row_no: int, column_no: int):
    item_list = []

    for row in range(row_no, row_no + 3):
        for column in range(column_no, column_no + 3):
            item = sudoku[row][column]
            if item != 0:
                if item in item_list:
                    return False
                item_list.append(item)
    
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