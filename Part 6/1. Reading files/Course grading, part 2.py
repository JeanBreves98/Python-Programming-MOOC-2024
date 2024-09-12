student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")
students = {}
grades = {}
exam_grades = {}

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

with open(exam_points) as exam_file:    # Reads the exam file
    for line in exam_file:
        parts = line.strip().split(";")
        if parts[0] == "id": # Skips header
            continue
        exam_grades[parts[0]] = list(map(int, parts[1:]))

for id, name in students.items():
    if id in grades and id in exam_grades:
        completed_exercises = sum(grades[id])
        exercise_grade = int((completed_exercises / 40) * 10)   # Calculates percentage of exercises completed and then attributes a grade
        exam_total = sum(exam_grades[id])
        total_grade = exercise_grade + exam_total
        if total_grade <= 14:
            print(f"{name} 0 (fail)")
        elif total_grade <= 17:
            print(f"{name} 1")
        elif total_grade <= 20:
            print(f"{name} 2")
        elif total_grade <= 23:
            print(f"{name} 3")
        elif total_grade <= 27:
            print(f"{name} 4")
        elif total_grade >= 28:
            print(f"{name} 5")