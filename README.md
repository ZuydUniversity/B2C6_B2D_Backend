GROEP 5-Backend

# Inleiding
Dit project bevat de backend voor het verwerken van patiënteninformatie, gebruikmakend van een MySQL database. De backend biedt CRUD-functionaliteiten (Create, Read, Update, Delete). De backend is via een API gekoppeld aan de frontend van Groep 5.

Zorg ervoor dat je de volgende software hebt geïnstalleerd:
Python 3.7+
MySQL
Pip (Python package installer)


### Installeer de vereiste Python-pakketten:
pip install -r requirements.txt


### Configureer de MySQL database:
Zorg ervoor dat je een MySQL server hebt draaien.
Maak een database aan voor dit project.
Pas de DATABASE_URL aan in je configuratiebestand of als omgevingsvariabele om te verwijzen naar je MySQL database:

`DATABASE_URL=mysql+pymysql://<username>:<password>@<host>:<port>/<database_name>`


### Run:
dev mode:
fastapi dev main.py

prod mode:
fastapi run main.py
