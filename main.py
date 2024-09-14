
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
def get_average(marks):
    total_sum = float(sum(marks))
    return total_sum/len(marks)

def marks_total_average(student_data):
    assignment_marks_average = get_average(student_data["assignment"])
    test_marks_average = get_average(student["test"])
    lab_marks_average = get_average(student["lab"])

    return (0.1 * assignment_marks_average) + (0.7 * test_marks_average) + (0.2 * lab_marks_average)

def check_grade(avg):
    if avg >= 90:
        print("Your Grade is A")
    elif avg >= 80:
        print("Your Grade is B")
    elif avg >= 70:
        print("Your Grade is C")
    elif avg >= 60:
        print("Your Grade is D")
    elif avg >= 50:
        print("Your Grade is E")
    elif avg >= 40:
        print("You Grade is F")
    else:
        print("Invalid Input!")

students = [jack, james, dylan, jess, tom]
for student in students:
    print(student["name"])
    print("Total average of marks", marks_total_average(student))

