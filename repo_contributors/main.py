from src.data_processing import process_repositories

if __name__ == '__main__':
    repo_links = [
        # Hier können Sie die Repository-Links aus einer Excel-Datei lesen
    ]

    auth_token = input("Enter your GitHub Personal Access Token (press Enter to skip): ")

    repositories_data = process_repositories(repo_links, auth_token)

    # Hier können Sie den Code zum Speichern der Daten in Excel-Dateien hinzufügen
