n = int(input("Enter number of students: ").strip())
print(f"Enter {n} rows of names and scores seperated by space:")
score_dict = {}
grade_dict = {'A': [], 'B': [], 'C': [], 'D': [], 'F': []}
for _ in range(n):
    name, score = input().strip().split()
    score_dict[name] = int(score)
for key, value in score_dict.items():
    if 90 <= value <= 100:
        grade_dict['A'].append(key)
    elif 80 <= value <= 89:
        grade_dict['B'].append(key)
    elif 70 <= value <= 79:
        grade_dict['C'].append(key)
    elif 60 <= value <= 69:
        grade_dict['D'].append(key)
    else:
        grade_dict['F'].append(key)
print(grade_dict)
