import glob
import os

def delCSV():
    targetPattern = r"backend/bin/*.csv"
    datei = glob.glob(targetPattern)
    os.remove(datei[0])