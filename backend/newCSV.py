import codecs
import glob
import os

line = []
dataDoc = r"/Users/mpotgeter/WebstormProjects/heatmap/backend/bin/data/data.txt"
csvPatternPath = r"/Users/mpotgeter/WebstormProjects/heatmap/backend/bin/*.csv"

def delCSV():
    datei = glob.glob(csvPatternPath)
    print("Found files:", datei)  # Add this line to see which files are found

    if not datei:
        print("No CSV files found to delete.")
        return

    print("Deleting file:", datei[0])  # Add this line to log which file is being deleted
    os.remove(datei[0])

def getPath():
    return csvPatternPath

def extractData():
    datei = glob.glob(csvPatternPath)
    if not datei:  # Check if the list is empty
        print("No CSV files found in the directory.")
        return  # Exit the function if no files are found

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

def restart():
    extractData()
    saveConDoc(dataDoc, line)

# restart()
