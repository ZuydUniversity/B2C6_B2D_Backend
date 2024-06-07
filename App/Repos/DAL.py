# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "root@localhost:3306"

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


config = {
    'user': 'root',              
    'password': 'password',     
    'host': 'localhost',       
    'port': 3306,               
    'database': 'Groep6DB',      
    'raise_on_warnings': True    
}

try:

    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    
    create_table_query = """
    CREATE TABLE Patient (
        id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        surname VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age INT,
        address VARCHAR(255),
        housenumber VARCHAR(10),
        city VARCHAR(100),
        telephonenumber VARCHAR(20)
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    print("Tabel 'Patient' succesvol aangemaakt met de opgegeven attributen")

    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"Fout: {err}")
