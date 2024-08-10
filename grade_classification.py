# Grade can be Decimal or integer
student_grade = input("Please enter student's grade")

# Typecast it
student_grade = float(student_grade)

# 90 - 100  Excellent
# 75 - 89   Very Good
# 60 - 74   Good
# 50 - 59   Fair
# 0 - 49    Fail

if (student_grade >= 90 and student_grade <= 100):
    print("Excellent result!")
    
elif (student_grade >= 75 and student_grade <= 89):
    print("very Good result!")
    
elif (student_grade >= 60 and student_grade <= 74):
    print("Good result")
    
elif (student_grade >= 50 and student_grade <= 59):
    print("Fair result")
    
elif (student_grade >= 0 and student_grade <= 49):
    print("This is failure!")

else:
    print("Sorry, I cannot recognise your command!")
    