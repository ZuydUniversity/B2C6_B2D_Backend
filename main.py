# niet bedoelt om met docker te runnen

# load env vars before running webserver
from dotenv import load_dotenv
import os

# if env vars are not loaded by default, fetch them from .env
if os.getenv('DB_URL') is None:
    load_dotenv(".env.local")

    print(f"[*] using db: {os.getenv('DB_URL')}")

# start webserver
from App import initializeApp

app = initializeApp()


