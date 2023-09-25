import os

# Basispfad für das Projekt
base_path = "repo_contributors"

# Liste der zu erstellenden Verzeichnisse und Unterverzeichnisse
dirs = [
    "app",
    "app/templates",
    "app/static",
    "data",
    "src",
    "tests",
]

# Liste der zu erstellenden Dateien
files = [
    ".gitignore",
    "README.md",
    "requirements.txt",
    "main.py",
    "app/__init__.py",
    "app/routes.py",
    "app/templates/index.html",
    "app/static/style.css",
    "src/github_api.py",
    "src/data_processing.py",
    "tests/test_github_api.py",
    "tests/test_data_processing.py",
    "data/input.xlsx",
]

# Verzeichnisse erstellen
for dir in dirs:
    os.makedirs(os.path.join(base_path, dir), exist_ok=True)

# Dateien erstellen
for file in files:
    open(os.path.join(base_path, file), 'a').close()

print(f"Projektstruktur unter {base_path} erfolgreich erstellt!")
