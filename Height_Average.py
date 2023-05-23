# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])  
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# total = sum(student_heights)
# print(total)

sum_of_height = 0
# sum of the heights using for loop (not using sum())
for height in student_heights:
    sum_of_height += height


# count = len(student_heights)
# print(count)

# counting number of students using for loop (not using len())
numberOfStudents = 0
for count in student_heights:
    numberOfStudents += 1

# Calculating Average
Average = sum_of_height / numberOfStudents

# Rounding the floating point number into integer
Avg = round(Average)
print(Avg)