from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("DATABASE_URL")

print(database_url)