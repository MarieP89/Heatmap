# import dbConnection
# import evaluateData
# from sqlite3 import Connection, Error

# # CREATE TABLE suppliers (
# #     supplier_id   INTEGER PRIMARY KEY,
# #     supplier_name TEXT    NOT NULL,
# #     group_id      INTEGER NOT NULL,
# #     FOREIGN KEY (group_id)
# #        REFERENCES supplier_groups (group_id));
# # YYYY-MM-DD HH:MM:SS.SSS

# createStatus = "CREATE TABLE Status (id_status_pk integer PRIMARY KEY, beschreibung varchar(30) NOT NULL)"
# createAbwesenheitsgrund = "CREATE TABLE Abwesenheitsgrund (id_abwesenheitsgrund_pk char(1) PRIMARY KEY, beschreibung varchar(80) NOT NULL)"
# createKlasse = "CREATE TABLE Klasse (id_klasse_pk integer PRIMARY KEY, beschreibung varchar(10) NOT NULL)"
# createStudent = "CREATE TABLE Student (id_student_pk varchar(50) PRIMARY KEY, nachname varchar(30) NOT NULL, vorname varchar(30) NOT NULL, id_klasse_fk int, FOREIGN KEY (id_klasse_fk) REFERENCES Klasse (id_klasse_pk))"
# createAbwesenheiten = "CREATE TABLE Abwesenheiten (id_abwesenheit_pk integer PRIMARY KEY, id_student_fk varchar(50) NOT NULL, beginn varchar(16) NOT NULL, ende varchar(16) NOT NULL, id_abwesenheitsgrund_fk char(1), id_status_fk int NOT NULL, FOREIGN KEY (id_student_fk) REFERENCES Student (id_student_pk), FOREIGN KEY (id_abwesenheitsgrund_fk) REFERENCES Abwesenheitsgrund (id_abwesenheitsgrund_pk), FOREIGN KEY (id_status_fk) REFERENCES Status (id_status_pk))"



# SELECT 
#     name
# FROM 
#     sqlite_schema
# WHERE 
#     type ='table' AND 
#     name NOT LIKE 'sqlite_%';





# tables = ["Status", "Abwesenheitsgrund", "Klasse", "Student", "Abwesenheiten"]
# querys = [createStatus, createAbwesenheitsgrund, createKlasse, createStudent, createAbwesenheiten]

# rTables = ["Klasse", "Student", "Abwesenheiten"]
# rQuerys = [createKlasse, createStudent, createAbwesenheiten]

# def createTable(query=""):
#     # conn = dbConnection.connect("backend/bin/studentDB.db")
#     conn = dbConnection.connect(dbConnection.file)
#     try:
#         c = conn.cursor()
#         for table in tables:
#             c.execute("DROP TABLE " + table + ";")
#             pass
#         for query in querys:
#             c.execute(query)
#     except Error as e:
#         print(e)
#     dbConnection.disconnect(conn)

# def resetDB():
#     conn = dbConnection.connect("backend/bin/studentDB.db")
#     try:
#         c = conn.cursor()
#         for table in tables:
#             c.execute("DROP TABLE " + table + ";")
# #         for query in rQuerys:
# #             c.execute(query)
#         conn.commit()
#     except Error as e:
#         print(e)
#     dbConnection.disconnect(conn)

# def insertValue(db:str, col:str, val:str):
#     return "INSERT INTO " + db + "(" + col + ") VALUES (" + val + ");"

# def fillStatus(conn:Connection):
#     status = evaluateData.getStatus()
#     c = conn.cursor()
#     # c.execute(insertValue("Status", "id_status_pk, beschreibung", "NULL, '" + status[0] + "'"))
#     # c.execute(insertValue("Status", "id_status_pk, beschreibung", "NULL, '" + status[1] + "'"))
#     c.execute("INSERT INTO Status (id_status_pk, beschreibung) VALUES (NULL, '" + status[0] + "');")
#     c.execute("INSERT INTO Status (id_status_pk, beschreibung) VALUES (NULL, '" + status[1] + "');")
#     # conn.commit()
#     print("done")
#     conn.commit()

# def fillAbwesenheitsgrund(conn:Connection):
#     grunde = evaluateData.getAbwesenheitsgrund()
#     c = conn.cursor()
#     for g in grunde:
#         c.execute(insertValue("Abwesenheitsgrund", "id_abwesenheitsgrund_pk, beschreibung", "'" + g[0] + "', '" + g[1] + "'"))
#     conn.commit()

# klassen = evaluateData.getClasses()
# # print(klassen)

# def fillKlasse(conn:Connection):
#     c = conn.cursor()
#     # print(klassen)
#     for klasse in klassen:
#         c.execute(insertValue("Klasse", "id_klasse_pk, beschreibung", "NULL, '" + klasse + "'"))
#     conn.commit()

# contents = []

# def getKlasseId(bezeichnung: str):
#     for i in range(len(klassen)):
#         if bezeichnung == klassen[i]:
#             return i + 1
        
# def getStudentId(studentId: str):
#     for i in range(1):
#         pass

# def fillStudent(conn:Connection):
#     global contents
#     global klassen
#     c = conn.cursor()
#     for klasse in klassen:
#         contents.append(evaluateData.getNamesOfClass(klasse))

#     # print(content)

#     for klasse in contents:
#         klasse_ = getKlasseId(klasse[0])
#         studentNames = klasse[1]
#         content = klasse[2]

#         # print(klasse_)
#         # print(studentNames)
#         # print(content)
#         for students in studentNames:
#             splitName = str(students[1]).split(" - ")
#             print(splitName)
#             c.execute(insertValue("Student", "id_student_pk, nachname, vorname, id_klasse_fk", "'" + students[0] + "', '" + splitName[0] + "', '" + splitName[1] + "', '" + str(klasse_) + "'"))
#             conn.commit()

# def fillAbwesenheiten(conn:Connection):
#     print(contents)
#     conn.commit()

# def fillDB():
#     resetDB()

#     conn = dbConnection.connect("backend/bin/studentDB.db")
#     c = conn.cursor()
#     fillStatus(conn)
#     fillAbwesenheitsgrund(conn)
#     fillKlasse(conn)
#     # TODO
#     fillStudent(conn)
#     # TODO
#     fillAbwesenheiten(conn)
#     dbConnection.disconnect(conn)

# fillDB()





#     # res = c.execute()
#     # res.fetchone()
# #     data = [
# #     ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
# #     ("Monty Python's The Meaning of Life", 1983, 7.5),
# #     ("Monty Python's Life of Brian", 1979, 8.0),
# # ]
# # cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
# # con.commit()