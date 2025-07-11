'''Write a function map_scores(scores) that:
Takes a list of integers scores (0 to 100)
Returns a list of strings, one for each score, based on the grade mapping'''


input_marks = list(map(int, input().split()))
output_grades = []
for x in input_marks:
    if (90 <= x <= 100):
        grade = 'A'
    elif x >= 80:
        grade = 'B'
    elif x >= 70:
        grade = 'C'
    elif x >= 60:
        grade = 'D'
    else:
        grade = 'F'
    output_grades.append(grade)
print(output_grades)
