import mysql.connector
from ..Models.Zorgverlener import Zorgverlener

class ZorgverlenerRepo:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    # Functie voor het toevoegen van een nieuwe zorgverlener aan de MariaDB database
    def create_zorgverlener(self, zorgverlener):
        connection = mysql.connector.connect()
        cursor = connection.cursor()

        query = ("INSERT INTO Zorgverlener (id, name, lastname, email, password) "
                 "VALUES (%s, %s, %s, %s, %s)")
        data = (zorgverlener.get_id(), zorgverlener.get_name(), zorgverlener.get_lastname(), zorgverlener.get_email(), zorgverlener.get_password())
        
        cursor.execute(query, data)
        connection.commit()
        
        cursor.close()
        connection.close()

    # Functie voor het ophalen van alle zorgverleners uit de MariaDB database
    def read_zorgverleners(self):
        connection = mysql.connector.connect()
        cursor = connection.cursor()

        query = "SELECT id, name, lastname, email, password FROM Zorgverlener"
        cursor.execute(query)

        zorgverleners = []
        for (id, name, lastname, email, password) in cursor:
            zorgverlener = Zorgverlener(id, name, lastname, email, password)
            zorgverleners.append(zorgverlener)

        cursor.close()
        connection.close()
        return zorgverleners

    # Functie voor het bijwerken van een bestaande zorgverlener in de MariaDB database
    def update_zorgverlener(self, zorgverlener):
        connection = mysql.connector.connect()
        cursor = connection.cursor()

        query = ("UPDATE Zorgverlener SET name = %s, lastname = %s, email = %s, password = %s "
                 "WHERE id = %s")
        data = (zorgverlener.get_name(), zorgverlener.get_lastname(), zorgverlener.get_email(), zorgverlener.get_password(), zorgverlener.get_id())

        cursor.execute(query, data)
        connection.commit()

        cursor.close()
        connection.close()

    # Functie voor het verwijderen van een zorgverlener uit de MariaDB database
    def delete_zorgverlener(self, zorgverlener):
        connection = mysql.connector.connect()
        cursor = connection.cursor()

        query = "DELETE FROM Zorgverlener WHERE id = %s"
        data = (zorgverlener.get_id(),)

        cursor.execute(query, data)
        connection.commit()

        cursor.close()
        connection.close()
