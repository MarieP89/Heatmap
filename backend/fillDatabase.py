import dbConnection as dbCon
import evaluateData
from sqlite3 import Connection, Error

def getAllTableNames(db) -> list: 
    allTables = "SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';"
    conn = dbCon.connect(db)
    c = conn.cursor()

    try:
        c.execute(allTables)
        results = c.fetchall()
    except Error as e:
        print(e)

    dbCon.disconnect(conn)

    tables = []
    for result in results:
        tables.append(result[0])

    return tables

#region variablen
tables = ["AllData", "Status", "Abwesenheitsgrund", "Klasse", "Student", "Abwesenheiten"]
statusEntries = evaluateData.getStatus()
absenceReasonEntries = evaluateData.getAbwesenheitsgrund()
classEntries = evaluateData.getClasses()
content = evaluateData.provideData()
# dbFile = "D:\\Schule\\LF12\\ls12_Projekt_Heatmap\\HEAT-9\\Heatmap\\backup\\studentDB.db"
db = "backend/bin/studentDB.db"
#getAllTableNames(db)
#endregion

#region table Queries
createCSVcopyTbl = "CREATE TABLE AllData (id integer NOT NULL, lastname varchar(30) NOT NULL, firstname varchar(30) NOT NULL, className varchar(10) NOT NULL, start varchar(16) NOT NULL, end varchar(16) NOT NULL, absenceReason char(2), status varchar(30) NOT NULL)"
createStatusTbl = "CREATE TABLE Status (id_status_pk integer PRIMARY KEY, beschreibung varchar(30) NOT NULL)"
createAbsenceReasonsTbl = "CREATE TABLE Abwesenheitsgrund (id_abwesenheitsgrund_pk char(1) PRIMARY KEY, beschreibung varchar(80) NOT NULL)"
createClassesTbl = "CREATE TABLE Klasse (id_klasse_pk integer PRIMARY KEY, beschreibung varchar(10) NOT NULL)"
createStudentsTbl = "CREATE TABLE Student (id_student_pk varchar(50) PRIMARY KEY, nachname varchar(30) NOT NULL, vorname varchar(30) NOT NULL, id_klasse_fk integer, FOREIGN KEY (id_klasse_fk) REFERENCES Klasse (id_klasse_pk))"
createAbsenceTimesTbl = "CREATE TABLE Abwesenheiten (id_abwesenheit_pk integer PRIMARY KEY, id_student_fk varchar(50) NOT NULL, beginn varchar(16) NOT NULL, ende varchar(16) NOT NULL, id_abwesenheitsgrund_fk char(2) NOT NULL, id_status_fk integer NOT NULL, FOREIGN KEY (id_student_fk) REFERENCES Student (id_student_pk), FOREIGN KEY (id_abwesenheitsgrund_fk) REFERENCES Abwesenheitsgrund (id_abwesenheitsgrund_pk), FOREIGN KEY (id_status_fk) REFERENCES Status (id_status_pk))"

createQueries = [createCSVcopyTbl,createStatusTbl,createAbsenceReasonsTbl,createClassesTbl,createStudentsTbl,createAbsenceTimesTbl]
#endregion

def createTables():
    conn = dbCon.connect(db)
    c = conn.cursor()
    for query in createQueries:
        try:
            c.execute(query)
        except Error as e:
            print(e)
    conn.commit()
    dbCon.disconnect(conn)

#region table getter und helper
def getTbl(tableName: int):
    query = "SELECT * FROM " + tables[tableName] + ";"
    conn = dbCon.connect(db)
    c = conn.cursor()
    try:
        c.execute(query)
        results = c.fetchall()
    except Error as e:
        print(e)
    dbCon.disconnect(conn)
    table = []
    for result in results:
        dataset = []
        for data in result:
            dataset.append(data)
        table.append(dataset)
    return table

def getClassId(className:str):
    classes = getTbl(3)
    for cl in classes:
        if cl[1] == className:
            return cl[0]
    return None

def getStatusId(statusName:str):
    status = getTbl(1)
    for stat in status:
        if stat[1] == statusName:
            return stat[0]
    return None

def insertValue(db:str, col:str, val:str):
    return "INSERT INTO " + db + "(" + col + ") VALUES (" + val + ");"
#endregion

#region populate DB
def populateAllDataTbl():
    conn = dbCon.connect(db)
    for line in content:
        try:
            s = "'" + line[0] + "', '" + line[1] + "', '" + line[2] + "', '" + line[3] + "', '" + line[4] + "', '" + line[5] + "', '" + line[6] + "', '" + line[7] + "'"
            c = conn.cursor()
            c.execute(insertValue(tables[0], "id, lastname, firstname, className, start, end, absenceReason, status", s))
        except Error as e:
            print(e)
    conn.commit()
    dbCon.disconnect(conn)

def populateStatus():
    conn = dbCon.connect(db)
    for entry in statusEntries:
        try:
            c = conn.cursor()
            c.execute(insertValue(tables[1], "id_status_pk, beschreibung", "NULL, '" + entry + "'"))
        except Error as e:
            print(e)
    conn.commit()
    dbCon.disconnect(conn)
    
def populateAbsenceReason():
    conn = dbCon.connect(db)
    for entry in absenceReasonEntries:
        try:
            c = conn.cursor()
            c.execute(insertValue(tables[2], "id_abwesenheitsgrund_pk, beschreibung", "'" + entry[0] + "', '" + entry[1] + "'"))
        except Error as e:
            print(e)
    conn.commit()
    dbCon.disconnect(conn)

def populateClass():
    conn = dbCon.connect(db)
    for entry in classEntries:
        try:
            c = conn.cursor()
            c.execute(insertValue(tables[3], "id_klasse_pk, beschreibung", "NULL , '" + entry + "'"))
        except Error as e:
            print(e)
    conn.commit()
    dbCon.disconnect(conn)

def populateStudent():
    studentID = []
    conn = dbCon.connect(db)
    for entry in content:
        if studentID.__contains__(entry[0]):
            next
        else:
            cl = getClassId(entry[3])
            try:
                s = ""
                print(cl)
                if cl == None:
                    next
                else:
                    s = "'" + entry[0] + "' , '" + entry[1] + "' , '" + entry[2] + "' , " + str(cl)
                c = conn.cursor()
                c.execute(insertValue(tables[4], "id_student_pk, nachname, vorname, id_klasse_fk", s))
                studentID.append(entry[0])
            except Error as e:
                print(e)
    conn.commit()
    dbCon.disconnect(conn)

def populateAbsenceReason():
    conn = dbCon.connect(db)
    for entry in content:
        status = getStatusId(entry[7])
        print(status)
        try:
            c = conn.cursor()
            s = "NULL, '" + entry[0] + "', '" + entry[4] + "', '" + entry[5] + "', '" + entry[6] + "', '" + str(status) + "'"
            c.execute(insertValue(tables[5], "id_abwesenheit_pk, id_student_fk, beginn, ende, id_abwesenheitsgrund_fk, id_status_fk", s))
        except Error as e:
            print(e)
    conn.commit()
    dbCon.disconnect(conn)
#endregion

#region table drop
def sendQuery(query):
    conn = dbCon.connect(db)
    try:
        c = conn.cursor()
        c.execute(query)
    except Error as e:
        print(e)
    conn.commit()
    dbCon.disconnect(conn)

# for table in tables:
#     sendQuery("DROP TABLE " + table + ";")
# sendQuery(createCSVcopyTbl)

#endregion

def createAndfillDatabase():
    createTables()
    populateAllDataTbl()
    populateStatus()
    populateAbsenceReason()
    populateClass()
    populateStudent()
    populateAbsenceReason()

# createAndfillDatabase()