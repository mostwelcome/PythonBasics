student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

# This is the scoring criteria:

# Scores 91 - 100: Grade = "Outstanding"

# Scores 81 - 90: Grade = "Exceeds Expectations"

# Scores 71 - 80: Grade = "Acceptable"

# Scores 70 or lower: Grade = "Fail"

for key in student_scores.keys():
    if student_scores[key] >= 91 and student_scores[key] < 101:
        student_grades[key] = 'Outstanding'
    elif student_scores[key] >= 81:
        student_grades[key] = 'Exceeds Expectation'
    elif student_scores[key] >= 71:
        student_grades[key] = 'Acceptable'
    else:
        student_grades[key] = 'Fail'

# 🚨 Don't change the code below 👇
print(student_grades)
