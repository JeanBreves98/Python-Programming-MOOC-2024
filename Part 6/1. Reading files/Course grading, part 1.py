student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
students = {}
grades = {}

with open(student_info) as student_file:    # Reads the student file
    for line in student_file:
        parts = line.strip().split(";")
        if parts[0] == "id": # Skips header
            continue
        students[parts[0]] = f"{parts[1]} {parts[2]}"

with open(exercise_data) as exercise_file:  # Reads the exercise file
    for line in exercise_file:
        parts = line.strip().split(";")
        if parts[0] == "id": # Skips header
            continue
        grades[parts[0]] = list(map(int, parts[1:]))

for id, name in students.items(): # Gets the sum of the grades
    if id in grades:
        grade_list = grades[id]
        print(f"{name} {sum(grade_list)}")