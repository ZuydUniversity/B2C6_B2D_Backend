import mysql.connector

class DAL:
    connection_string = "database"

    #Aanmaken lijst voor zorgverleners
    zorgverleners = []

    #Aanmaken van zorgverlener
    @staticmethod
    def create_zorgverlener(zorgverlener):
        connection = mysql.connector.connect()
        cursor = connection.cursor()
        qry = """
        INSERT INTO Zorgverlener (name, lastname, email, password)
        VALUES (%s, %s, %s, %s)
        """
        