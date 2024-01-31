import codecs
import restart

dataDoc = "backend/bin/data/data.txt"
classesPath = "backend/bin/data/classes/"

data = [line.strip().split(",") for line in codecs.open(dataDoc, "r", 'utf-8').readlines()]
print(data[0])
print(data[1])

def getClasses():
    classes = []
    [classes.append(data[i][2]) for i in range(1, len(data)) if data[i][2] not in classes]
    return classes

def getNamesOfClass(classes: str):
    students = []
    for line in data:
        if line[2] == classes:
            students.append(line)
    path = classesPath + classes + ".txt"
    restart.writeTXT(path, students)
    
    studentNames = []
    for student in students:
        [studentNames.append(student[0] + ", " + student[1]) for i in range(1, len(students)) if student[0] not in studentNames]

    return studentNames

for c in getClasses():
    print(getNamesOfClass(c))

print(getClasses())
