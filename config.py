import os
from dotenv import load_dotenv

load_dotenv()
SERVICE_KEY = os.getenv("SERVICE_KEY")
OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")