from flask import Flask

# Erstellen Sie eine Instanz der Flask-Anwendung
app = Flask(__name__)

# Importieren Sie die Routen/Endpunkte der Anwendung
from app import routes
