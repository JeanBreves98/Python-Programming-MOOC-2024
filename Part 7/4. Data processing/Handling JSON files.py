import json

def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()

    students = json.loads(data)

    for student in students:
        hobbies = ''
        for hobby in student["hobbies"]:
            hobbies += hobby + ', '
        hobbies = hobbies[:-2]
        print(f"{student["name"]} {student["age"]} years ({hobbies})")

if __name__ == "__main__":
    print_persons("file1.json")
    print_persons("file2.json")
    print_persons("file3.json")
    print_persons("file4.json")