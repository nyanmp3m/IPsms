from flask import Flask
from db import db_session
from routes import register_routes

app = Flask(__name__)
app.config.from_object('config.Config')

db_session.global_init(app.config['DATABASE_PATH'])

register_routes(app)