def run(program):
    variables_dict = {}
    results = []
    
    def validate(check):
        if check in variables_dict:
            check = variables_dict[check]
        return check

    def add(x, y):
        print(f"{parts[1]}({x}) + {parts[2]}({y}) = {x + y}")
        return x + y

    def subtract(x, y):
        print(f"{parts[1]}({x}) - {parts[2]}({y}) = {x - y}")
        return x - y

    def multiply(x, y):
        print(f"{parts[1]}({x}) * {parts[2]}({y}) = {x * y}")
        return x * y

    for i in range(len(program)):
        parts = program[i].split(" ")
        command = parts[0]

        if command == "PRINT":
            print_value = int(variables_dict[parts[1]])
            results.append(print_value)
            print(f"{parts[1]} = {print_value}")

        if command == "MOV":
            variable = parts[1]
            value = parts[2]
            variables_dict[variable] = value

        if command == "ADD":
            x = int(variables_dict[parts[1]])
            y = int(validate(parts[2]))
            variables_dict[parts[1]] = add(x,y)
            continue

        if command == "SUB":
            x = int(variables_dict[parts[1]])
            y = int(validate(parts[2]))
            variables_dict[parts[1]] = add(x,y)
            continue

        if command == "MUL":
            x = int(variables_dict[parts[1]])
            y = int(validate(parts[2]))
            variables_dict[parts[1]] = add(x,y)
            continue



'''        if command == "JUMP":




        if command == "IF":




        if command == "END":
            return results



        if command == "MOV":




        if command == "MOV":
'''