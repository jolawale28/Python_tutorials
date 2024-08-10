
student_grade = input("Please enter student's grade")

# We added this Exception check to catch the error that could
# come from typecasting the student_grade to a float if the 
# user enters an invalid input
try:
    student_grade = float(student_grade) # This will give an error
except TypeError:
    print("Student grade must be a number!") # The error will be caught here

if (student_grade >= 90 and student_grade <=100):
    print("Distinction")
elif(student_grade >= 80 and student_grade <=89):
    print ("Very Good")
elif (student_grade >= 65 and student_grade <-79):
    print ("Good")
elif (student_grade >=50 and student_grade <=64):
    print("Average")
elif(student_grade >=40 and student_grade <=49):
    print("Pass")
elif(student_grade <= 40):
    print ("ungraded")
else:
    print("Please enter a number between 0 and 100!")



    