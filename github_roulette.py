import requests
import random
import os

# GitHub API configuration
GITHUB_API_URL = "https://api.github.com/search/repositories"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def fetch_random_repos():
    # GitHub search API returns max 1000 results, so we'll use a random page number
    random_page = random.randint(1, 10)
    params = {
        "q": "stars:>1",  # Search for repos with at least 1 star
        "sort": "stars",
        "order": "desc",
        "per_page": 100,
        "page": random_page
    }
    
    response = requests.get(GITHUB_API_URL, headers=headers, params=params)
    response.raise_for_status()
    return response.json()["items"]

def select_random_repo(repos):
    return random.choice(repos)

def display_repo_info(repo):
    print(f"Name: {repo['name']}")
    print(f"URL: {repo['html_url']}")
    print(f"Stars: {repo['stargazers_count']}")

def main():
    try:
        repos = fetch_random_repos()
        selected_repo = select_random_repo(repos)
        display_repo_info(selected_repo)
    except requests.RequestException as e:
        print(f"An error occurred while fetching data from GitHub: {e}")
    except KeyError as e:
        print(f"Unexpected data format in GitHub response: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

