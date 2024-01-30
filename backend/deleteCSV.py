import glob
import os

def delCSV():
    targetPattern = r"backend/bin/upload/*.csv"
    datei = glob.glob(targetPattern)
    os.remove(datei[0])