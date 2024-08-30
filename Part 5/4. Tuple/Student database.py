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
                student_courses.append((course_name, grade, existing_course[2]))
            return

    if course_count == 0:   # If course list is empty the average is equal to the grade
        average = grade
    else:   # If there is already a course on the list this line calculates what the average will be with the new course
        total_grades = sum(c[1] for c in student_courses) + grade
        average = total_grades / (course_count + 1)

    students[name].append((course_name, grade, average))   # Adds a course to a student


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
        
        print(f" average grade {course[2]:.1f}")


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