def line(times, string):
    first_character = string[0]
    
    print(first_character * times)   


def shape(width, triangle_body, height, rectangle_body):
    maximum_size = width
    i = 1
    k = height

    while i <= maximum_size:
        line(i, triangle_body)
        i += 1
    while k > 0:
        line(width, rectangle_body)
        k -= 1


if __name__ == "__main__":
    width = 3
    triangle_body = "."
    height = 0
    rectangle_body = ""
    shape(width, triangle_body, height, rectangle_body)