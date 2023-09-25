import pandas as pd
from .github_api import fetch_contributors, enrich_contributor_data

def process_repositories(repo_links, auth_token=None):
    all_data = {}
    for repo_url in repo_links:
        # Extract owner and repo name from the URL
        parts = repo_url.split("/")
        owner, repo = parts[-2], parts[-1]

        contributors = fetch_contributors(owner, repo, auth_token)
        enriched_data = enrich_contributor_data(contributors, auth_token)

        # Save to dictionary
        all_data[repo] = enriched_data

    return all_data

def save_data_to_excel(repositories_data):
    for repo, data in repositories_data.items():
        output_filename = f'data/contributors_{repo}.xlsx'
        df = pd.DataFrame(data, columns=["Username", "Contributions", "Profile Link", "Followers Link", "Public Repos", "Followers", "Following", "Public Gists", "Repo Topics", "Location"])

        with pd.ExcelWriter(output_filename) as writer:
            df.to_excel(writer, sheet_name=repo)

        print(f"Data for {repo} exported to {output_filename}")