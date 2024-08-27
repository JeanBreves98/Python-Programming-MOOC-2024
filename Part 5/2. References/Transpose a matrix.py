def transpose(matrix: list):
    copy = []

    for row in matrix:
        row_copy = []
        for item in row:
            row_copy.append(item)
        copy.append(row_copy)

    matrix.clear()

    for i in range(len(copy[0])):
        new_row = []
        for j in range(len(copy)):
            new_row.append(copy[j][i])
        matrix.append(new_row)

    return matrix

if __name__ == "__main__":
    m = [[1, 2], [3, 4], [5, 6]]
    
    print(transpose(m))