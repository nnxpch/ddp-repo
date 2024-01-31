# practice grading system

def grading_system(score):
    
    grade = ["A", "B+", "B", "C+", "C" "D+", "D", "F"]
    if score >= 80 and score <= 100: return grade[0]
    elif score >= 75 and score < 80: return grade[1]
    elif score >= 70 and score < 75: return grade[2]
    elif score >= 65 and score < 70: return grade[3]
    elif score >= 60 and score < 65: return grade[4]
    elif score >= 55 and score < 60: return grade[5]
    elif score >= 50 and score < 55: return grade[6]
    elif score >= 0 and score < 50: return grade[7]

print(grading_system(99.25))
print(grading_system(87.25))
print(grading_system(69.95))
print(grading_system(101.01))
print(grading_system(120))





