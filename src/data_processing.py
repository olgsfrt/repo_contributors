import pandas as pd
from .github_api import fetch_contributors, enrich_contributor_data
#from app import output_folder  # Importieren Sie output_folder aus __init__.py
import os


def process_repositories(repo_links, auth_token=None):
    from app import output_folder  # Importieren Sie output_folder hier
    all_data = {}
    for repo_url in repo_links:
        # Extract owner and repo name from the URL
        parts = repo_url.split("/")
        owner, repo = parts[-2], parts[-1]

        contributors = fetch_contributors(owner, repo, auth_token)
        enriched_data = enrich_contributor_data(contributors, auth_token)

        # Save to dictionary
        all_data[repo] = enriched_data

        # Generieren und speichern der Datei im output_folder
        output_filename = f'contributors_{repo}.xlsx'
        filepath = os.path.join(output_folder, output_filename)
        df = pd.DataFrame(enriched_data, columns=["Username", "Contributions", "Profile Link", "Followers Link", "Public Repos", "Followers", "Following", "Public Gists", "Repo Topics", "Location"])
        df.to_excel(filepath)
        print(f"Data for {repo} exported to {filepath}")

    return all_data


def save_data_to_excel(repositories_data):
    from app import output_folder
    for repo, data in repositories_data.items():
        output_filename = f'contributors_{repo}.xlsx'
        filepath = os.path.join(output_folder, output_filename)  # Verwenden Sie output_folder für den Dateipfad
        df = pd.DataFrame(data, columns=["Username", "Contributions", "Profile Link", "Followers Link", "Public Repos", "Followers", "Following", "Public Gists", "Repo Topics", "Location"])

        with pd.ExcelWriter(filepath) as writer:  # Verwenden Sie den vollständigen Dateipfad beim Speichern
            df.to_excel(writer, sheet_name=repo)

        print(f"Data for {repo} exported to {filepath}")  # Drucken Sie den vollständigen Dateipfad
