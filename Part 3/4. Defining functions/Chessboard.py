def chessboard(size):
    rows = size // 2
    board = rows

    if size == 1:
        print("1")
    elif size % 2 == 0:
        while board > 0:
            print("10" * rows)
            print("01" * rows)
            board -= 1
    elif size % 2 == 1:
        while size > 0:
            print("10" * rows + "1")
            size -= 1
            if size == 0:
                break
            print("01" * rows + "0")
            size -= 1
    
    
if __name__ == "__main__":
    chessboard(11)