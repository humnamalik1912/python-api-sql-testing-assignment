import requests

# Three GitHub usernames
usernames = ["torvalds", "octocat", "kamranahmedse"]

for username in usernames:

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    # Verify status code before processing data
    if response.status_code == 200:

        data = response.json()

        print("Username:", data["login"])
        print("Public Repositories:", data["public_repos"])
        print("-------------------------")

    else:
        print("API request failed for:", username)
        print("Status Code:", response.status_code)