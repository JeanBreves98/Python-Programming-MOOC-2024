def add_student(students, name):
    students[name] = [] # Add student to the database with an empty course list


def add_course(students, name, course):
    course_name = course[0]
    grade = course[1]
    course_count = len(students[name])
    student_courses = students[name]

    if grade == 0: # Course is ignored if the grade is equal to 0
        return
    
    for existing_course in student_courses: # Checks if there is a another added course with the same name as the one currently being added.
        if existing_course[0] == course_name:
            if grade > existing_course[1]:  # If the new course has a bigger grade, it removes the old one and add another in its place
                student_courses.remove(existing_course)
                student_courses.append((course_name, grade))
            return

    students[name].append((course_name, grade))   # Adds a course to a student


def summary(students):
    student_count = 0
    most_courses = 0
    top_student_courses  = None
    top_student_averages = None
    highest_average = 0
    student_count = len(students)

    for student, courses in students.items():
        course_count = len(courses)
        if course_count > most_courses:
            most_courses = course_count
            top_student_courses = student
        if course_count > 0:
            total_grades = sum(course[1] for course in courses)
            average = total_grades / course_count
            if average > highest_average:
                highest_average = average
                top_student_averages = student

    print(f"students {student_count}")
    print(f"most courses completed {most_courses} {top_student_courses}")
    print(f"best average grade {highest_average} {top_student_averages} ")


def print_student(students, name):
    if name not in students: # If name not in database an error message is printed and the function ends
        print(f"{name}: no such person in the database")
        return 
    else: 
        print(name + ":")

    if students[name] == []:    # If course list is empty it prints a message stating that there aren't any completed courses just yet
        print(" no completed courses")
    else:  
        course_count = len(students[name])

        print(f" {course_count} completed courses:")
        
        for course in students[name]:
            print(f"  {course[0]} {course[1]}")
        
        total_grades = sum(course[1] for course in students[name])
        average = total_grades / course_count

        print(f" average grade {average:.1f}")


if __name__ == "__main__":  
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 4))
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")
    summary(students)