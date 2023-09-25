import requests

def fetch_contributors(owner, repo, auth_token=None):
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
        headers = {"Accept": "application/vnd.github.v3+json"}

        if auth_token:
            headers["Authorization"] = f"token {auth_token}"

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"Failed to fetch contributors for {owner}/{repo} due to: {e}")
        return []

def get_contributor_details(username, auth_token=None):
    try:
        url = f"https://api.github.com/users/{username}"
        headers = {"Accept": "application/vnd.github.v3+json"}

        if auth_token:
            headers["Authorization"] = f"token {auth_token}"

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"Failed to fetch details for user {username} due to: {e}")
        return {}

def get_repo_topics(owner, repo, auth_token=None):
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/topics"
        headers = {"Accept": "application/vnd.github.mercy-preview+json"}

        if auth_token:
            headers["Authorization"] = f"token {auth_token}"

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.json().get('names', [])
    except requests.exceptions.HTTPError as e:
        print(f"Failed to fetch topics for {owner}/{repo} due to: {e}")
        return []

def enrich_contributor_data(contributors, auth_token=None):
    data = []
    for contributor in contributors:
        user_details = get_contributor_details(contributor['login'], auth_token)
        location = user_details.get('location', 'N/A')

        user_repos_response = requests.get(user_details['repos_url'], headers={"Accept": "application/vnd.github.v3+json"})
        user_repos = user_repos_response.json()

        all_topics = []
        for repo in user_repos:
            if 'owner' in repo and 'login' in repo['owner']:
                topics = get_repo_topics(repo['owner']['login'], repo['name'], auth_token)
                all_topics.extend(topics)

        unique_topics = list(set(all_topics))

        data.append([
            contributor['login'],
            contributor['contributions'],
            contributor['html_url'],
            contributor['followers_url'],
            user_details['public_repos'],
            user_details['followers'],
            user_details['following'],
            user_details['public_gists'],
            ", ".join(unique_topics),
            location
        ])

    return data
