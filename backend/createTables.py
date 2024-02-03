import dbConnection
from sqlite3 import Error



# CREATE TABLE suppliers (
#     supplier_id   INTEGER PRIMARY KEY,
#     supplier_name TEXT    NOT NULL,
#     group_id      INTEGER NOT NULL,
#     FOREIGN KEY (group_id)
#        REFERENCES supplier_groups (group_id)
# );
# YYYY-MM-DD HH:MM:SS.SSS


createStatus = "CREATE TABLE Status (id_status_pk int PRIMARY KEY, beschreibung varchar(30) NOT NULL)"
createAbwesenheitsgrund = "CREATE TABLE Abwesenheitsgrund (id_abwesenheitsgrund_pk char(1) PRIMARY KEY, beschreibung varchar(80) NOT NULL)"
createKlasse = "CREATE TABLE Klasse (id_klasse_pk int PRIMARY KEY, beschreibung varchar(10) NOT NULL)"
createStudent = "CREATE TABLE Student (id_student_pk varchar(50) PRIMARY KEY, nachname varchar(30) NOT NULL, vorname varchar(30) NOT NULL, id_klasse_fk int, FOREIGN KEY (id_klasse_fk) REFERENCES Klasse (id_klasse_pk))"
createAbwesenheit = "CREATE TABLE Abwesenheiten (id_abwesenheit_pk int PRIMARY KEY, id_student_fk varchar(50) NOT NULL, beginn varchar(16) NOT NULL, ende varchar(16) NOT NULL, id_abwesenheitsgrund_fk char(1), id_status_fk int NOT NULL, FOREIGN KEY (id_student_fk) REFERENCES Student (id_student_pk), FOREIGN KEY (id_abwesenheitsgrund_fk) REFERENCES Abwesenheitsgrund (id_abwesenheitsgrund_pk), FOREIGN KEY (id_status_fk) REFERENCES Status (id_status_pk))"

tables = ["Status", "Abwesenheitsgrund", "Klasse", "Student", "Abwesenheiten"]
querys = [createStatus, createAbwesenheitsgrund, createKlasse, createStudent, createAbwesenheit]

rTables = ["Klasse", "Student", "Abwesenheiten"]
rQuerys = [createKlasse, createStudent, createAbwesenheit]

# TODO Tabellen erstellen mit Primary Keys und dann altern mit Foreign keys?
def createTable(query=""):
    conn = dbConnection.connect("backend/bin/studentDB.db")

    try:
        c = conn.cursor()
        for table in tables:
            c.execute("DROP TABLE " + table + ";")

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
