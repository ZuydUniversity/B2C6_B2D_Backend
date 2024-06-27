# niet bedoelt om met docker te runnen

# load env vars before running webserver
from dotenv import load_dotenv
import os

load_dotenv(".env.local")

print(f"[*] using db: {os.getenv('DB_URL')}")

# start webserver
from App import initializeApp

app = initializeApp()


