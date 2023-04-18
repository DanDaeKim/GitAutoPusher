from auth import Auth
from repo_scanner import RepoScanner
from file_processor import process_files
from gpt_analyzer import analyze_code
from efficiency_evaluator import filter_efficiency_suggestions
from report_generator import generate_report

def main(username: str):
    # Initialize GitHub and GPT API clients
    auth = Auth()
    github_client = auth.get_github_client()
    gpt_client = auth.get_gpt_client()

    # Scan repositories
    repo_scanner = RepoScanner(github_client)
    repositories = repo_scanner.get_user_repositories(username)

    # Process and analyze code files, filter efficiency suggestions, and generate reports
    for repo in repositories:
        print(f"Processing repository: {repo.name}")

        # Extract code from files
        code_files = process_files(repo)

        # Get suggestions from GPT API
        suggestions = analyze_code(gpt_client, code_files)

        # Filter efficiency-related suggestions
        efficiency_suggestions = filter_efficiency_suggestions(suggestions)

        # Generate report
        generate_report(repo.name, efficiency_suggestions)

if __name__ == "__main__":
    username = "your-github-username"
    main(username)
