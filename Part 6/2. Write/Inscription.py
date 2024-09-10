name = input("Whom should i sign this to: ")
filename = input("Where shall i save it: ")
text = f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team"

with open(filename, "w") as file:
    file.write(text)