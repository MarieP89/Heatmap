import codecs

originDoc = "backend/bin/AbsenceList_20231115_1157.csv"
dataDoc = "backend/bin/data.txt"

lines = [line.strip() for line in codecs.open(originDoc, "r", 'utf-8').readlines()]
line = []

for l in lines:
    line.append(l.split("\t"))

def usedData(x:list):
    return(x[0], x[1], x[4], x[5], x[6], x[7], x[9])

def saveConDoc(line):
    doc = codecs.open(dataDoc, 'w', encoding='utf-8')
    for x in line:
        string = ""
        for s in usedData(x):
            string += ", " + s
        doc.write(string[2:])
        doc.write('\n')
    doc.close()

saveConDoc(line)
