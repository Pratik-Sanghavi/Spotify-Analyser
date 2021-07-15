from flask import Flask
import os
from dotenv import load_dotenv

app=Flask(__name__)
app.secret_key = "344730e6c0962d4f3ede56f9"
app.config['SESSION_COOKIE_NAME'] = 'Pratik'
load_dotenv()

clientid = os.getenv('CLIENT_ID')
clientsecret = os.getenv('CLIENT_SECRET')
TOKEN_INFO = "token_info"

# Keep this at end of __init__.py. Veryyy important!
from spotify_app import routes