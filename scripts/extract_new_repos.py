import requests
import json
from datetime import datetime, timedelta

# Function for querying the GitHub API
def search_github_repositories(query, sort="stars", order="desc", per_page=10, page=1):
    url = "https://api.github.com/search/repositories"
    headers = {"Accept": "application/vnd.github.v3+json"}
    params = {
        "q": query,
        "sort": sort,
        "order": order,
        "per_page": per_page,
        "page": page
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# Main function for extracting and saving recent repositories
def extract_and_save_new_repositories():
    # Calculate date 7 days ago
    last_week = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    query = f"cybersecurity stars:>10 created:>{last_week}"
    
    repositories_data = search_github_repositories(query=query, per_page=20)

    if repositories_data:
        repositories = []
        for repo in repositories_data['items']:
            repositories.append({
                "name": repo["name"],
                "url": repo["html_url"],
                "description": repo["description"],
                "stars": repo["stargazers_count"],
                "language": repo["language"],
                "created_at": repo["created_at"],
                "updated_at": repo["updated_at"]
            })

        # Save results in a JSON file
        with open('new_cybersecurity_repos.json', 'w') as json_file:
            json.dump(repositories, json_file, indent=4)
        print("Les nouveaux dépôts ont été sauvegardés dans 'new_cybersecurity_repos.json'.")
    else:
        print("Aucun dépôt trouvé ou une erreur est survenue.")

# Script execution
if __name__ == "__main__":
    extract_and_save_new_repositories()
