import base64
from typing import List
from github import Repository

def is_code_file(file_name: str) -> bool:
    file_extensions = (".py", ".js", ".java", ".cpp", ".c", ".rb", ".go", ".php", ".rs", ".swift")
    return file_name.endswith(file_extensions)

def extract_code_from_files(files: List[str]) -> List[str]:
    code_list = []
    for file_content in files:
        decoded_content = base64.b64decode(file_content).decode("utf-8")
        code_list.append(decoded_content)
    return code_list

def process_files(repo: Repository) -> List[str]:
    code_files = []
    for file in repo.get_contents(""):
        if is_code_file(file.name):
            code_files.append(file.content)
    return extract_code_from_files(code_files)

if __name__ == "__main__":
    from auth import Auth
    from repo_scanner import RepoScanner

    auth = Auth()
    github_client = auth.get_github_client()
    repo_scanner = RepoScanner(github_client)

    username = "your-github-username"
    repositories = repo_scanner.get_user_repositories(username)
    
    for repo in repositories:
        print(f"Processing files in repository: {repo.name}")
        code_files = process_files(repo)
        print(f"Found {len(code_files)} code files.")
