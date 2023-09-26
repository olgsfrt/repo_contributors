from flask import Flask

# Erstellen Sie eine Instanz der Flask-Anwendung
app = Flask(__name__)

# Setzen Sie die geheime Schlüssel
app.config['SECRET_KEY'] = '123457891111'

# Importieren Sie die Routen/Endpunkte der Anwendung
from app import routes

