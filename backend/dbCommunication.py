import dbConnection
import evaluateData
from sqlite3 import Connection, Error

# CREATE TABLE suppliers (
#     supplier_id   INTEGER PRIMARY KEY,
#     supplier_name TEXT    NOT NULL,
#     group_id      INTEGER NOT NULL,
#     FOREIGN KEY (group_id)
#        REFERENCES supplier_groups (group_id));
# YYYY-MM-DD HH:MM:SS.SSS

createStatus = "CREATE TABLE Status (id_status_pk integer PRIMARY KEY, beschreibung varchar(30) NOT NULL)"
createAbwesenheitsgrund = "CREATE TABLE Abwesenheitsgrund (id_abwesenheitsgrund_pk char(1) PRIMARY KEY, beschreibung varchar(80) NOT NULL)"
createKlasse = "CREATE TABLE Klasse (id_klasse_pk integer PRIMARY KEY, beschreibung varchar(10) NOT NULL)"
createStudent = "CREATE TABLE Student (id_student_pk varchar(50) PRIMARY KEY, nachname varchar(30) NOT NULL, vorname varchar(30) NOT NULL, id_klasse_fk int, FOREIGN KEY (id_klasse_fk) REFERENCES Klasse (id_klasse_pk))"
createAbwesenheiten = "CREATE TABLE Abwesenheiten (id_abwesenheit_pk integer PRIMARY KEY, id_student_fk varchar(50) NOT NULL, beginn varchar(16) NOT NULL, ende varchar(16) NOT NULL, id_abwesenheitsgrund_fk char(1), id_status_fk int NOT NULL, FOREIGN KEY (id_student_fk) REFERENCES Student (id_student_pk), FOREIGN KEY (id_abwesenheitsgrund_fk) REFERENCES Abwesenheitsgrund (id_abwesenheitsgrund_pk), FOREIGN KEY (id_status_fk) REFERENCES Status (id_status_pk))"

tables = ["Status", "Abwesenheitsgrund", "Klasse", "Student", "Abwesenheiten"]
querys = [createStatus, createAbwesenheitsgrund, createKlasse, createStudent, createAbwesenheiten]

rTables = ["Klasse", "Student", "Abwesenheiten"]
rQuerys = [createKlasse, createStudent, createAbwesenheiten]

def createTable(query=""):
    # conn = dbConnection.connect("backend/bin/studentDB.db")
    conn = dbConnection.connect(dbConnection.file)
    try:
        c = conn.cursor()
        for table in tables:
            # TODO - table exist abfragen, wenn ja, Tabelle dropen, wenn nein, next 
            c.execute("DROP TABLE " + table + ";")
            pass
        for query in querys:
            c.execute(query)
    except Error as e:
        print(e)
    dbConnection.disconnect(conn)

def resetDB():
    conn = dbConnection.connect("backend/bin/studentDB.db")
    try:
        c = conn.cursor()
        for table in rTables:
            c.execute("DROP TABLE " + table + ";")
        for query in rQuerys:
            c.execute(query)
    except Error as e:
        print(e)
    dbConnection.disconnect(conn)

resetDB()

def insertValue(db:str, col:str, val:str):
    return "INSERT INTO " + db + "(" + col + ") VALUES (" + val + ");"

def fillStatus(conn:Connection):
    status = evaluateData.getStatus()
    c = conn.cursor()
    # c.execute(insertValue("Status", "id_status_pk, beschreibung", "NULL, '" + status[0] + "'"))
    # c.execute(insertValue("Status", "id_status_pk, beschreibung", "NULL, '" + status[1] + "'"))
    c.execute("INSERT INTO Status (id_status_pk, beschreibung) VALUES (NULL, '" + status[0] + "');")
    c.execute("INSERT INTO Status (id_status_pk, beschreibung) VALUES (NULL, '" + status[1] + "');")
    # conn.commit()
    print("done")
    conn.commit()
    print("Status geladen...")


def fillAbwesenheitsgrund(conn:Connection):
    grunde = evaluateData.getAbwesenheitsgrund()
    c = conn.cursor()
    for g in grunde:
        c.execute(insertValue("Abwesenheitsgrund", "id_abwesenheitsgrund_pk, beschreibung", "'" + g[0] + "', '" + g[1] + "'"))
    # conn.commit()
    conn.commit()
    print("Abwesenheitsgrund geladen...")

klassen = evaluateData.getClasses()
# print(klassen)

def fillKlasse(conn:Connection):
    c = conn.cursor()
    # print(klassen)
    for klasse in klassen:
        c.execute(insertValue("Klasse", "id_klasse_pk, beschreibung", "NULL, '" + klasse + "'"))
    conn.commit()
    print("Klasse geladen...")

contents = []

def fillStudent(conn:Connection):
    global contents
    global klassen
    # print(klassen)

    for klasse in klassen:
        contents.append(evaluateData.getNamesOfClass(klasse))
    
    # print(contents[0][2][0])

    for klasse in contents:
        klasse_ = klasse[0]
        studentNamen_ = klasse[1]
        content_ = klasse[2]
    
        print(studentNamen_[0])

        for student in studentNamen_:
            print(student)

        




    print("Student geladen...")
    pass
    # c = conn.cursor()

    # for klasse in contents:
    #     studentNames = klasse[1]

    #     print(klasse_)
    #     # print(studentNames)
    #     # print(content)
    #     for students in studentNames:
    #         splitName = str(students[1]).split(" - ")
    #         print(splitName)
    #         c.execute(insertValue("Student", "id_student_pk, nachname, vorname, id_klasse_fk", "'" + students[0] + "', '" + splitName[0] + "', '" + splitName[1] + "', '" + klasse_ + "'"))
    #         conn.commit()

    #     # ZHN 02
    #     # "CREATE TABLE Student (id_student_pk, nachname, vorname, id_klasse_fk"
    #     # ['Pferd_philip', 'Pferd - Philip', 'ZHN 02', '13.11.2023', '08:00', '13.11.2023', '17:00', 'K', 'entsch.']
    #     # ['Pferd_philip', 'Pferd - Philip', 'ZHN 02', '14.11.2023', '08:00', '14.11.2023', '17:00', 'N', 'nicht entsch.']
    #     # [['haase_mike', 'Haase - Mike'], 'ZHN 02', ['30.08.2023', '08:00', '30.08.2023', '17:00'], ['K', 'entsch.']]
    #     # for student in studenten:
    #     #     c.execute(insertValue("Student", "id_student_pk, nachname, vorname, id_klasse_fk", ))
    #     #     print(student)

def test():
    conn = dbConnection.connect("backend/bin/studentDB.db")
    fillKlasse(conn)
    fillStudent(conn)

test()

def fillAbwesenheiten(conn:Connection):
    conn.commit()

def fillDB():
    conn = dbConnection.connect("backend/bin/studentDB.db")
    c = conn.cursor()
    createTable()
    fillStatus(conn)
    fillAbwesenheitsgrund(conn)
    fillKlasse(conn)
    # TODO
    fillStudent(conn)
    # TODO
    # fillAbwesenheiten(conn)
    dbConnection.disconnect(conn)

# fillDB()





    # res = c.execute()
    # res.fetchone()
#     data = [
#     ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
#     ("Monty Python's The Meaning of Life", 1983, 7.5),
#     ("Monty Python's Life of Brian", 1979, 8.0),
# ]
# cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
# con.commit()