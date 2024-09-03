def matrix_sum():
    matrix = []
    matrix_sum = 0

    with open("matrix.txt") as file:
        for line in file:
            row = []
            line = line.replace("\n", "")
            elements = line.split(",")
            for element in elements:
                if element: # Checks if the element is empty
                    element = int(element)
                    row.append(element)
            if row: # Checks if the row is empty
                matrix.append(row)

    for matrix_row in matrix:   # Gets the sum of each row of the matrix and then adds it to the matrix sum
        matrix_sum += sum(matrix_row)

    print(matrix_sum)
    
        
def matrix_max():
    matrix = []
    greatest = 0

    with open("matrix.txt") as file:
        for line in file:
            row = []
            line = line.replace("\n", "")
            elements = line.split(",")
            for element in elements:
                if element: # Checks if the element is empty
                    element = int(element)
                    row.append(element)
            if row: # Checks if the row is empty
                matrix.append(row)

    for matrix_row in matrix:
        row_max = max(matrix_row)
        if row_max > greatest:
            greatest = row_max


    print(greatest)


def row_sums():
    matrix = []
    row_sums = []

    with open("matrix.txt") as file:
        for line in file:
            row = []
            line = line.replace("\n", "")
            elements = line.split(",")
            for element in elements:
                if element: # Checks if the element is empty
                    element = int(element)
                    row.append(element)
            if row: # Checks if the row is empty
                matrix.append(row)

    for matrix_row in matrix:
        row_sum = sum(matrix_row)
        row_sums.append(row_sum)

    print(row_sums)


if __name__ == "__main__":
    matrix_sum()
    matrix_max()
    row_sums()