def exam_points(separate_inputs):
    p1 = int(separate_inputs[0])

    return p1


def exercise_points(separate_inputs):
    p2 = int(separate_inputs[1]) // 10
    
    return p2


def total_points(p1, p2):
    total = p1 + p2
    if p1 < 10:
        points.append(total)
        total = 0 
    else:
        points.append(total)

    return total


def grades(total):
    if total >= 0 and total <= 14:
        grade = 0
    elif total >= 15 and total <= 17:
        grade = 1
    elif total >= 18 and total <= 20:
        grade = 2
    elif total >= 21 and total <= 23:
        grade = 3
    elif total >= 24 and total <= 27:
        grade = 4
    elif total >= 28 and total <= 30:
        grade = 5

    return grade


def grade_counter(grade): #Can be improved.
    if grade == 0:
        grade_list.append(0)
    elif grade == 1:
        grade_list.append(1)
    elif grade == 2:
        grade_list.append(2)
    elif grade == 3:
        grade_list.append(3)
    elif grade == 4:
        grade_list.append(4)
    elif grade == 5:
        grade_list.append(5)

    return grade_list


def average_grades(points):
    average = sum(points) / len(points)

    return average


def pass_percentage(grade_list):
    percentage = (grade_list.count(1) + grade_list.count(2) + grade_list.count(3) + grade_list.count(4) + grade_list.count(5)) / len(grade_list) 
    percentage = percentage * 100

    return percentage


def statistics(average, percentage, grade_list):
    print("Statistics:")
    print(f"Points average: {average:.1f}")
    print(f"Pass percentage: {percentage:.1f}")
    print("Grade distribution:")
    print(f"5: {(grade_list.count(5)) * '*'}")
    print(f"4: {(grade_list.count(4)) * '*'}")
    print(f"3: {(grade_list.count(3)) * '*'}")
    print(f"2: {(grade_list.count(2)) * '*'}")
    print(f"1: {(grade_list.count(1)) * '*'}")
    print(f"0: {(grade_list.count(0)) * '*'}")


def input_separator(inputs):
    separate_inputs = inputs.split()

    return separate_inputs


grade_list = []
points = []

while True:
    inputs = input("Exam points and exercises completed: ")
    if inputs == "":
        break
    separate_inputs = input_separator(inputs)
    p1 = exam_points(separate_inputs)
    p2 = exercise_points(separate_inputs)
    total = total_points(p1, p2)
    grade = grades(total)
    grade_list = grade_counter(grade)

average = average_grades(points)
percentage = pass_percentage(grade_list)

statistics(average, percentage, grade_list)