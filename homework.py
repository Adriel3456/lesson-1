student_grades ={'john':85,'jane':90, 'jim':95}
john_grade = student_grades['john']
print(john_grade)
#Output:85

jane_grade = student_grades['jane']
print(jane_grade)
#Output:90

jim_grade = student_grades['jim']
print(jim_grade)
#Output:95

if john in student_grades:
    print(student_grades['john'])

 if jane in student_grades:
    print(student_grades['jane'])   

if jim in student_grades:
     print(student_grades['jim'])