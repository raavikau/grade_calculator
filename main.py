
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

sub1 = 44
sub2 = 67
sub3 = 76
sub4 = 99
sub5 = 58

total = sub1 + sub2 + sub3 + sub4 + sub5
average = total / 5
check_grade(average)
