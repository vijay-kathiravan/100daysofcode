student_scores = {
    'Vijay' : 99,
    'Gayu' : 86,
    'Aarthan' : 75,
    'Hari' : 71,
    'Rio' : 59
}
student_grades={}
for i in student_scores:
    if 91 <= student_scores[i] <= 100:
        student_grades[i] = 'Outstanding'
    elif 81 <= student_scores[i] <= 90:
        student_grades[i] = 'Exceeds Expectations'
    elif 71 <= student_scores[i] <= 80:
        student_grades[i] = 'Acceptable'
    else:
        student_grades[i] = 'Fail'
print(student_grades.keys())
print(student_grades.values())