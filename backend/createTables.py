import dbConnection
from sqlite3 import Error

conn = dbConnection.connect("backend/bin/studentDB.db")


# CREATE TABLE suppliers (
#     supplier_id   INTEGER PRIMARY KEY,
#     supplier_name TEXT    NOT NULL,
#     group_id      INTEGER NOT NULL,
#     FOREIGN KEY (group_id)
#        REFERENCES supplier_groups (group_id)
# );


# table 1 - Status - X
# 1 - "nicht entsch."
# 2 - "entsch."

createStatus = "CREATE TABLE Status (id_status_pk int PRIMARY KEY, beschreibung varchar(30) NOT NULL)"

# table 2 - Abwesenheitsgrund - X
# A - Krank mit Attest
# K - Krank - ohne Attest
# N - Unentschuldigt
# O - Online
# P - Private Gründe
# S - schulische Abwesendheit
# V - Verspätung

createAbwesenheitsgrund = "CREATE TABLE Abwesenheitsgrund (id_abwesenheitsgrund_pk char(1) PRIMARY KEY, beschreibung varchar(80) NOT NULL)"

# table 3 - Klasse - X
# 1 - ZHN 02
# 2 - FIA 14

createKlasse = "CREATE TABLE Klasse (id_klasse_pk int PRIMARY KEY, beschreibung varchar(10) NOT NULL)"

# table 4 - Student
# ID - Nachname - Vorname - Klasse
# haase_mike - Haase - Mike - 1
# loewe_lisa - Löwe - Lisa - 2

createStudent = "CREATE TABLE Student (id_student_pk varchar(50) PRIMARY KEY, nachname varchar(30) NOT NULL, vorname varchar(30) NOT NULL, id_klasse_fk int, FOREIGN KEY (id_klasse_fk) REFERENCES Klasse (id_klasse_pk))"

# table 5 - Abwesenheit
# id - student_ID - Beginndatum + Beginnzeit - Enddatum + Endzeit - Abwesenheitsgrund_ID - Status_ID
# 1 - haase_mike - 2023-08-30 08:00 - 2023-08-30 17:00 - K - 1
# 2 - haase_mike - 2023-10-12 08:00 - 2023-10-12 08:06 - V - 0
# YYYY-MM-DD HH:MM:SS.SSS

createAbwesenheit = "CREATE TABLE Abwesenheit (id_abwesenheit_pk int PRIMARY KEY, id_student_pk varchar(50) NOT NULL, beginn varchar(16) NOT NULL, ende varchar(16) NOT NULL, id_abwesenheitsgrund_pk char(1), id_status_pk int NOT NULL), FOREIGN KEY (id_student_fk) REFERENCES Student (id_student_pk), FOREIGN KEY (id_abwesenheitsgrund_fk) REFERENCES Abwesenheitsgrund (id_abwesenheitsgrund_pk), FOREIGN KEY (id_status_fk) REFERENCES Status (id_status_pk)"

# TODO Tabellen erstellen mit Primary Keys und dann altern mit Foreign keys?
def createTable(query=""):
    try:
        c = conn.cursor()
        c.execute("DROP TABLE Status;")
        c.execute("DROP TABLE Abwesenheitsgrund")
        c.execute("DROP TABLE Klasse")
        c.execute("DROP TABLE Student")
        c.execute("DROP TABLE Abwesenheit")
        c.execute(createStatus)
        c.execute(createAbwesenheitsgrund)
        c.execute(createKlasse)
        c.execute(createStudent)
        c.execute(createAbwesenheit)
    except Error as e:
        print(e)


createTable()
dbConnection.disconnect(conn)
