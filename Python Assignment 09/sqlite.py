import sqlite3

peopleValues = ('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak\'not','Mangalore',-5)

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS Roster")
    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO Roster VALUES(?,?,?)", peopleValues)
    c.execute("UPDATE Roster SET Species = 'Human' WHERE Name = 'Korben Dallas'")
    c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
    for row in c.fetchall():
        print(row)

