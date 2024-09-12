def write_correct(correct_solutions):
    with open("correct.csv", "w") as correct_file:
        for solution in correct_solutions:
            correct_file.write(f"{solution[0]};{solution[1]};{solution[2]}\n")


def write_incorrect(incorrect_solutions):
    with open("incorrect.csv", "w") as incorrect_file:
        for solution in incorrect_solutions:
            incorrect_file.write(f"{solution[0]};{solution[1]};{solution[2]}\n")


def filter_solutions():
    correct_solutions = []
    incorrect_solutions = []

    with open("solutions.csv") as file:
        for line in file:
            parts = line.strip().split(";")
            if len(parts) < 3:
                continue
            if '+' in parts[1]:
                problem = parts[1].split("+")
                num1 = int(problem[0])
                num2 = int(problem[1])
                result = num1 + num2
                if result == int(parts[2]):
                    correct_solutions.append(parts)
                else:
                    incorrect_solutions.append(parts)  
            elif '-' in parts[1]:
                problem = parts[1].split("-")
                num1 = int(problem[0])
                num2 = int(problem[1])
                result = num1 - num2
                if result == int(parts[2]):
                    correct_solutions.append(parts)
                else:
                    incorrect_solutions.append(parts)

    write_correct(correct_solutions)
    write_incorrect(incorrect_solutions)
    

if __name__ == "__main__":
    filter_solutions()