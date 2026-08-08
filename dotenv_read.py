from dotenv import load_dotenv
import os

load_dotenv()

port, host = os.getenv('PORT'), os.getenv('HOST')