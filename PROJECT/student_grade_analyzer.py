import numpy as np

students = np.array([
    ["Kushagra","80","98","94"],
    ["hehe", "89","35","75"],
    ["haha","89","76","56"]
])

names = students[:,0]
marks = students[:,1:].astype(float)

total = np.sum(marks,axis = 1)
average = np.round(np.mean(marks, axis = 1),2)

print(total, " ", average)

for i in range(len(names)):
    print(names[i],total[i],average[i])

def assign_grades(avg):
    if avg >= 90:
        grade = 'A+'
    elif avg >= 80:
        grade = 'A'
    elif avg >= 70:
        grade = 'B+'
    elif avg >= 60:
        grade = 'B'
    elif avg >= 50:
        grade = 'C+'
    else :
        grade = 'F'

    return grade

grades = [assign_grades(avg) for avg in average]

topper_index = np.argmax(average)
print("Topper :", names[topper_index])

class_average = np.round(np.mean(marks))
print("class average :", class_average)

print("GRADES --> ")
for i in range(len(names)):
    print(names[i], ":", grades[i])