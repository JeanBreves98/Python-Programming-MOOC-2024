student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")
course = input("Course information: ")
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

with open(course) as course_file:
    course_information = []
    for line in course_file:
        parts = line.strip().split(':')
        course_information.append(parts[1])
    course_title = f"{course_information[0].strip()}, {course_information[1].strip()} credits\n"

with open("results.txt", "w") as results_file:
    results_file.write(course_title)
    results_file.write((len(course_title) - 1) * '=' + "\n")
    results_file.write(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n")
    for id, name in students.items():   # Calculates the grades 
        if id in grades and id in exam_grades:
            completed_exercises = sum(grades[id])
            exercise_grade = int((completed_exercises / 40) * 10)   # Calculates percentage of exercises completed and then attributes a grade
            exam_total = sum(exam_grades[id])
            total_grade = exercise_grade + exam_total
            if total_grade <= 14:
                grade = 0
            elif total_grade <= 17:
                grade = 1
            elif total_grade <= 20:
                grade = 2
            elif total_grade <= 23:
                grade = 3
            elif total_grade <= 27:
                grade = 4
            elif total_grade >= 28:
                grade = 5
            results_file.write(f"{name:30}{completed_exercises:<10}{exercise_grade:<10}{exam_total:<10}{total_grade:<10}{grade:<10}\n")

with open("results.csv", "w") as results_csv:
    for id, name in students.items():   # Calculates the grades 
        if id in grades and id in exam_grades:
            completed_exercises = sum(grades[id])
            exercise_grade = int((completed_exercises / 40) * 10)   # Calculates percentage of exercises completed and then attributes a grade
            exam_total = sum(exam_grades[id])
            total_grade = exercise_grade + exam_total
            if total_grade <= 14:
                grade = 0
            elif total_grade <= 17:
                grade = 1
            elif total_grade <= 20:
                grade = 2
            elif total_grade <= 23:
                grade = 3
            elif total_grade <= 27:
                grade = 4
            elif total_grade >= 28:
                grade = 5
            results_csv.write(f"{id};{name};{grade}\n")