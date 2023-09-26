from src.data_processing import process_repositories, save_data_to_excel
from app import app  # Importieren Sie die Flask-App-Instanz

if __name__ == '__main__':
    repo_links = [
        # Hier können Sie die Repository-Links aus einer Excel-Datei lesen
    ]

    auth_token = input("Enter your GitHub Personal Access Token (press Enter to skip): ")

    repositories_data = process_repositories(repo_links, auth_token)

    # Daten in Excel-Dateien speichern
    save_data_to_excel(repositories_data)

    # Flask-Anwendung starten
    app.run(debug=True)

