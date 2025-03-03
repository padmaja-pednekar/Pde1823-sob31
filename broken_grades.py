# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) #padma-pednekar edited and added int() function

exam_three = int(input("Input exam grade three: ")) #padma-pednekar replaced str() with int(); the variable exam_3 is changed to exam_three to match the item in the list.

grades = [exam_one, exam_two, exam_three] #padma-pednekar added commas (,) to separate items in the list
sum = 0
for grade in grades: #for grade in grade to for grade in grades
  sum = sum + grade

avg = sum / len(grades) #padma-pednekar changed variable name from grdes to grades

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: #padma-pednekar added colon (:) at the end of the elif statement
    letter_grade = "B"
elif avg > 70 and avg < 80: #padma_pednekar changed 69 to 70
    letter_grade = "C" #padma-pednekar changed "C' to "C"
elif avg <= 70 and avg >= 60: #padma_pednekar changed the range values from 60-70.
    letter_grade = "D"
else: #padma-pednekar changed from elif to else
    letter_grade = "F"

#padma-pednekar removed the statement "for grade in grades:"
print(f"Exam: {grades[0]},{grades[1]},{grades[2]}") #padma-pednekar removed the indentation; changed format to get all grades.

print("Average: " + str(avg)) #padma-pednekar removed the indentation

print("Grade: " + letter_grade) #padma-pednekar removed the indentation


if letter_grade == "F": #padma-pednekar changed the variable name from letter-grade to letter_grade; 'is' is changed to '=='
    print("Student is failing.") #padma-pednekar added missing paranthesis () for the print statement
else:
    print("Student is passing.") #padma-pednekar added missing paranthesis () for the print statement
