import codecs
import newCSV

dataDoc = r"/Users/mpotgeter/WebstormProjects/heatmap/backend/bin/data/data.txt"
classesPath = "backend/bin/data/classes/"

# data = [line.strip().split(",") for line in codecs.open(dataDoc, "r", 'utf-8').readlines()]
# data.pop(0)
# data = file.split(",")
# print(data[0])
# print(data[1])

# for c in getClasses():
#     print(getNamesOfClass(c))

# print(getClasses())
try:
    with codecs.open(dataDoc, "r", 'utf-8') as file:
        data = [line.strip().split(",") for line in file.readlines()]

    # Prüfen, ob data nicht leer ist, bevor pop verwendet wird
    if data:
        data.pop(0)
    else:
        print("Die Datei ist leer.")
        data = []  # Setze data auf eine leere Liste, falls erforderlich

except FileNotFoundError:
    print(f"Die Datei {dataDoc} wurde nicht gefunden.")
    data = []  # Setze data auf eine leere Liste, falls erforderlich

def reverseDate(date:str):
    splitDate = date.split(".")
    return splitDate[2] + "." + splitDate[1] + "." + splitDate[0]

def provideData() -> list:
    dataForTbl = []
    for line in data:
        name = line[1].split(" - ")
        # YYYY-MM-DD HH:MM
        start = reverseDate(line[3]) + " " + line[4]
        end = reverseDate(line[5]) + " " + line[6]
        dataForTbl.append([line[0], name[0], name[1], line[2], start, end, line[7], line[8]])
    return dataForTbl

def getStatus():
    s0 = "nicht entsch."
    s1 = "entsch."
    return [s0, s1]

def getAbwesenheitsgrund():
    a = ("A", "Krank mit Attest")
    k = ("K", "Krank - ohne Attest")
    n = ("N", "Unentschuldigt")
    o = ("O", "Online")
    p = ("P", "Private Gründe")
    s = ("S", "schulische Abwesendheit")
    v = ("V", "Verspätung")
    return [a, k, n, o, p, s, v]

def getClasses():
    classes = []
    [classes.append(data[i][2]) for i in range(1, len(data)) if data[i][2] not in classes]
    classes.sort()
    return classes

def getNamesOfClass(classes: str):
    students = []
    for line in data:
        if line[2] == classes:
            students.append(line)
    path = classesPath + classes + ".txt"
    # newCSV.writeTXT(path, students)
    
    studentNames = []
    content = []

    for student in students:
        names = [student[0], student[1]]
        klasse = student[2]
        zeiten = [student[3], student[4], student[5], student[6]]
        abwesend = [student[7], student[8]]
        # ['Pferd_philip', 'Pferd - Philip', 'ZHN 02', '13.11.2023', '08:00', '13.11.2023', '17:00', 'K', 'entsch.']
        # ['Pferd_philip', 'Pferd - Philip', 'ZHN 02', '14.11.2023', '08:00', '14.11.2023', '17:00', 'N', 'nicht entsch.']
        [studentNames.append(names) for i in range(1, len(students)) if names not in studentNames]
        [content.append([names, klasse, zeiten, abwesend]) for i in range(1, len(students))]
    return classes, studentNames, content

# getNamesOfClass("ZHN 02")
# print(getNamesOfClass("ZHN 02"))