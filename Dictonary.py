student_scores = {

"Harry" : 81,
"Ros" : 78,
"Hermione": 99,
"Draco" : 74,
"Neville" : 62, 
}


# TODO-1 : Create an empty dictonary called student_grades.
student_grades = {}


# TODO-2 : Convert scores into grades.
for student in student_scores:
    score = student_scores[student]

    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceed Expectation"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"            

print(student_grades)
