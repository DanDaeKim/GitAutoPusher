from typing import List
from github import Github, Repository

from auth import Auth
from file_processor import process_files

class RepoScanner:
    def __init__(self, github_client: Github):
        self.github_client = github_client

    def get_user_repositories(self, username: str) -> List[Repository]:
        user = self.github_client.get_user(username)
        return list(user.get_repos())

    def get_organization_repositories(self, organization: str) -> List[Repository]:
        org = self.github_client.get_organization(organization)
        return list(org.get_repos())

    def scan_repositories(self, repositories: List[Repository]):
        for repo in repositories:
            print(f"Scanning repository: {repo.name}")
            process_files(repo)

if __name__ == "__main__":
    auth = Auth()
    github_client = auth.get_github_client()
    repo_scanner = RepoScanner(github_client)

    username = "your-github-username"
    repositories = repo_scanner.get_user_repositories(username)
    repo_scanner.scan_repositories(repositories)
