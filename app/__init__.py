from flask import Flask
import os

# Erstellen Sie eine Instanz der Flask-Anwendung
app = Flask(__name__)

# Setzen Sie die geheime Schlüssel
app.config['SECRET_KEY'] = '123457891111'

output_folder = os.path.join(app.root_path, 'output')
os.makedirs(output_folder, exist_ok=True)
# Importieren Sie die Routen/Endpunkte der Anwendung
from app import routes

