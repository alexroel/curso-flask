from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Configuración de la APP
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

from webpersonal.views import base
from webpersonal.project.views import project

app.register_blueprint(base)
app.register_blueprint(project)
# import webpersonal.views

#Ejecutar todas la consultas 
db.create_all()