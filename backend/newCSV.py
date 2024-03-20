import codecs
import glob
import os
#"backend/bin/data/data.txt"

line = []
dataDoc = r"/Users/mpotgeter/WebstormProjects/heatmap/backend/bin/data/data.txt"
csvPatternPath = r"backend/bin/upload/*.csv"

def delCSV():
    datei = glob.glob(csvPatternPath)
    if datei:
        os.remove(datei[0])
    else:
        print("Keine CSV-Datei zum Löschen gefunden.")
    # os.remove(datei[0])


def getPath():
    return csvPatternPath

def extractData():
    datei = glob.glob(csvPatternPath)
    if datei:
        originDoc = datei[0]

        lines = [line.strip() for line in codecs.open(originDoc, "r", 'utf-8').readlines()]
        line_data = []
        for l in lines:
            line_data.append(l.split("\t"))
        return line_data
    else:
        print("Keine CSV-Datei zum Extrahieren von Daten gefunden.")
        return []
#     datei = glob.glob(csvPatternPath)
#     originDoc = datei[0]
#
#     lines = [line.strip() for line in codecs.open(originDoc, "r", 'utf-8').readlines()]
#     for l in lines:
#         line.append(l.split("\t"))
    
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

def restart():
    extractData()
    saveConDoc(dataDoc, line)

# restart()
