# Program calculates individual students averages and grades as well as the class average and overall grade for the class.
jack = {"name": "Jack Frost",
        "assignment": [80, 50, 40, 20],
        "test": [75, 75],
        "lab": [78.20, 77.20]
        }
james = {"name": "James Potter",
         "assignment": [82, 56, 44, 30],
         "test": [80, 80],
         "lab": [67.90, 78.72]
         }
dylan = {"name": "Dylan Rhodes",
         "assignment": [77, 82, 23, 39],
         "test": [78, 77],
         "lab": [80, 80]
         }
jess = {"name": "Jessica Stone",
        "assignment": [67, 55, 77, 21],
        "test": [40, 50],
        "lab": [69, 44.56]
        }
tom = {"name": "Tom Hanks",
       "assignment": [29, 89, 60, 56],
       "test": [65, 56],
       "lab": [50, 40.6]
       }

def get_marks_average(marks):
    total_sum = float(sum(marks))
    return total_sum/len(marks)

def marks_total_average(student_data):
    assignment_marks_average = get_marks_average(student_data["assignment"])
    test_marks_average = get_marks_average(student_data["test"])
    lab_marks_average = get_marks_average(student_data["lab"])
    # Return the result based on weightage supplied 10 % from assignments 70 % from test 20 % from lab-works
    return (0.1 * assignment_marks_average) + (0.7 * test_marks_average) + (0.2 * lab_marks_average)

def check_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "E"

def class_average(student_list):
    stu_data = []
    for stu in student_list:  # looping through the student list
        student_avg = marks_total_average(stu)  # calculate students individual weighted average
        stu_data.append(student_avg)
    return get_marks_average(stu_data)  # average of all students

students = [jack, james, dylan, jess, tom]
for student in students:  # take student name from list then access the data that's in dictionary respective variable name
    print(student["name"])
    student_average = marks_total_average(student)
    print("Total average of marks", student_average)
    print("Your Grade is", check_grade(student_average))
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
clas_average = class_average(students)
print("Class average is", clas_average)
print("Grade of the class is", check_grade(clas_average))
