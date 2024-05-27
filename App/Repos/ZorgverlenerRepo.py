import mysql.connector

class DAL:
    connection_string = "database"

    #Aanmaken lijst voor zorgverleners
    zorgverleners = []

    @staticmethod
    def create_zorgverlener(zorgverlener):
        connection = mysql.connector.connect()
        cursor = connection.cursor()
        qry = """
        INSERT INTO Zorgverlener (naam, achternaam, email, wachtwoord)
        VALUES (%s, %s, %s, %s)
        """
        