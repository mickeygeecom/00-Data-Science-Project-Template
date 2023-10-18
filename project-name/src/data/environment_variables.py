import os

from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()

# take environment variables from .env.
load_dotenv()  # take environment variables from .env.

API_KEY = os.getenv("API_KEY")
PASSWORD = os.getenv("PASSWORD")
