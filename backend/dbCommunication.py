from sqlite3 import Connection, Error
import dbConnection as dbCon

# SELECT 
#     name
# FROM 
#     sqlite_schema
# WHERE 
#     type ='table' AND 
#     name NOT LIKE 'sqlite_%';

# tables = ["Status", "Abwesenheitsgrund", "Klasse", "Student", "Abwesenheiten"]


tables = ["AllData", "Status", "Abwesenheitsgrund", "Klasse", "Student", "Abwesenheiten"]
db = "backend/bin/studentDB.db"

# getClassNames -> Klasse.beschreibung
def getClassNames():
    query = "SELECT * FROM " + tables[3] + ";"
    conn = dbCon.connect(db)
    c = conn.cursor()
    try:
        c.execute(query)
        results = c.fetchall()
    except Error as e:
        print(e)
    dbCon.disconnect(conn)
    table = [["ID", "Bezeichnung"]]
    for result in results:
        dataset = []
        for data in result:
            dataset.append(data)
        table.append(dataset)
    return table

# getStudentNames -> Student.id_student-pk, Student.nachname, Student.vorname 
def getStudentNames(classID:int):
    query = "SELECT id_student_pk, nachname, vorname FROM " + tables[4] + " WHERE id_klasse_fk = " + str(classID) + ";"
    conn = dbCon.connect(db)
    c = conn.cursor()
    try:
        c.execute(query)
        results = c.fetchall()
    except Error as e:
        print(e)
    dbCon.disconnect(conn)
    table = [["ID", "Nachname", "Vorname"]]
    for result in results:
        dataset = []
        for data in result:
            dataset.append(data)
        table.append(dataset)
    return table

# getAbsenceOfStudent(studentID) ->  beginn, ende, id_abwesenheit_fk, id_status_fk WHERE 
def getAbsenceOfStudent(studentID:str):
    query = "SELECT id_student_fk, beginn, ende, id_abwesenheitsgrund_fk, id_status_fk FROM " + tables[5] + " WHERE id_student_fk = '" + studentID + "';"
    conn = dbCon.connect(db)
    c = conn.cursor()
    try:
        c.execute(query)
        results = c.fetchall()
    except Error as e:
        print(e)
    dbCon.disconnect(conn)
    table = [["beginn", "ende", "abwesenheit", "status"]]
    for result in results:
        dataset = []
        for data in result:
            dataset.append(data)
        table.append(dataset)
    return table

print(getAbsenceOfStudent("loewe_lisa"))
