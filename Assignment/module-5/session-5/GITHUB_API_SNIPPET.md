# GitHub API - Standalone Python GET-Request Snippet

Below is the standalone Python snippet using the `requests` library to fetch public repositories for a GitHub user. This logic is directly adapted into the Django REST Framework `GitHubReposView` endpoint (`/api/github-repos/<username>/`).

```python
import requests

# Step 1: Define GitHub API endpoint and target username
username = "octocat"
url = f"https://api.github.com/users/{username}/repos"

# Step 2: Include User-Agent header (required by GitHub API)
headers = {
    "User-Agent": "Python-Requests-Script"
}

try:
    # Step 3: Perform HTTP GET request
    response = requests.get(url, headers=headers, timeout=10)

    # Step 4: Handle response status codes
    if response.status_code == 200:
        repos_data = response.json()
        if not repos_data:
            print(f"User '{username}' has no public repositories.")
        else:
            # Extract only the repository names
            repo_names = [repo["name"] for repo in repos_data if "name" in repo]
            print(f"Public Repositories for '{username}':")
            for name in repo_names:
                print(f" - {name}")

    elif response.status_code == 404:
        print(f"Error: GitHub user '{username}' was not found.")

    else:
        print(f"Error {response.status_code}: Failed to fetch repositories.")

except requests.RequestException as e:
    print(f"Request failed due to network error: {e}")
```

## Adaptation into DRF View (`api/views.py`)

In DRF, this GET request logic is wrapped inside an `APIView` subclass:

```python
class GitHubReposView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, username):
        url = f"https://api.github.com/users/{username}/repos"
        headers = {"User-Agent": "Django-DRF-App"}

        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                repos_data = response.json()
                if not repos_data:
                    return Response({
                        "repositories": [],
                        "message": f"User '{username}' has no public repositories."
                    }, status=status.HTTP_200_OK)

                repo_names = [repo["name"] for repo in repos_data if "name" in repo]
                return Response({
                    "repositories": repo_names
                }, status=status.HTTP_200_OK)

            elif response.status_code == 404:
                return Response({
                    "error": f"GitHub user '{username}' not found."
                }, status=status.HTTP_404_NOT_FOUND)

            else:
                return Response({
                    "error": "Failed to fetch repositories from GitHub API.",
                    "status_code": response.status_code
                }, status=response.status_code)

        except requests.RequestException as e:
            return Response({
                "error": f"API request failed: {str(e)}"
            }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
```
