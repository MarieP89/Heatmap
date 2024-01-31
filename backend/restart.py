# originDoc = "backend/bin/AbsenceList_20231115_1157.csv"
# dataDoc = "backend/bin/data.txt"
import codecs
import glob

line = []
dataDoc = "backend/bin/data/data.txt"

def extractData():
    targetPattern = r"backend/bin/upload/*.csv"
    datei = glob.glob(targetPattern)

    originDoc = datei[0]

    lines = [line.strip() for line in codecs.open(originDoc, "r", 'utf-8').readlines()]
    for l in lines:
        line.append(l.split("\t"))
    
def usedData(x:list):
    name = [x[0] + " - " + x[1]]
    return(x[2], name[0], x[3], x[4], x[5], x[6], x[7], x[9], x[12])

def saveConDoc(path, line):
    doc = codecs.open(path, 'w', encoding='utf-8')
    for x in line:
        string = ""
        for s in usedData(x):
            string += "," + s
        doc.write(string[1:])
        doc.write('\n')
    doc.close()

def writeTXT(path, liste):
    doc = codecs.open(path, 'w', encoding='utf-8')
    for x in liste:
        string = ""
        for y in x:
            string += ", " + y
        doc.write(string[1:] + "\n")
    doc.close()  

extractData()
saveConDoc(dataDoc, line)