program = ""

while program != "visual studio code":
    program = input("Editor:")
    program = program.lower()
    if program == "visual studio code":
        print("an excellent choice")
    elif program == "word" or program == "notepad":
        print("awful")
    else:
        print("not good")
