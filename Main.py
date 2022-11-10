student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total = 0  
print(student_heights)
for x in student_heights:
    total +=  x

nbr_of_student = 0
for student in student_heights:
    nbr_of_student +=  1

average = total / nbr_of_student
print(round(average))
