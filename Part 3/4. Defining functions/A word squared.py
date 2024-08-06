def squared(string, square):
    size = square
    long_string = string * 10000 # Creates a long string that then can be cut into smaller pieces
    start = 0
    end = size 

    while square > 0:
        word_squared = long_string[start:end]
        print(word_squared)
        start = end
        end = start + size
        square -= 1


if __name__ == "__main__":
    squared("ab", 3)