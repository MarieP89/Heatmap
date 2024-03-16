import dbConnection as dbCon
import evaluateData
from sqlite3 import Connection, Error

# TODO conn auf die richtige DB
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

dbFile = "D:\Schule\LF12\ls12_Projekt_Heatmap\HEAT-9\Heatmap\\backup\studentDB.db"
db = "backend/bin/studentDB.db"
#getAllTableNames(dbFile)

#region consts
tables = ["AllData", "Status", "Abwesenheitsgrund", "Klasse", "Student", "Abwesenheiten"]
statusEntries = evaluateData.getStatus()
absenceReasonEntries = evaluateData.getAbwesenheitsgrund()
#endregion

#region table Queries
createCSVcopyTbl = "CREATE TABLE AllData (id_pk integer NOT NULL, lastname varchar(30) NOT NULL, firstname varchar(30) NOT NULL, className varchar(10) NOT NULL, start varchar(16) NOT NULL, end varchar(16) NOT NULL, absenceReason char(2), status beschreibung varchar(30) NOT NULL)"
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

createTables()


# beginn und ende concaten 
# populate AllData

# populate Status -> evaluateData.getStatus()
# populate Abwesenheitsgrund -> evaluateData.getAbwesenheitsgrund()

# getClasses aus AllData (unique)
# populate Klasse

# getKlassenID -> id_klasse_fk
# populate Student

# getAbsenceReasonID -> id_abwesenheitsgrund_fk
# getStatusID -> id_status_fk
# populate Abwesenheiten







def shootQuery(query):
    conn = dbCon.connect(db)
    try:
        c = conn.cursor()
        c.execute(query)
    except Error as e:
        print(e)
    conn.commit()
    dbCon.disconnect(conn)

# shootQuery("DROP TABLE AllData;")
# shootQuery(createCSVcopyTbl)


# ID,   Langname - Vorname,     Klasse,     
# Beginndatum-Beginnzeit,    Enddatum-Endzeit,    # YYYY-MM-DD HH:MM
# Abwesenheitsgrund,    Status
