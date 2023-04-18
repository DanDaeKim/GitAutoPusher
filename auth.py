import os
from github import Github

from openai import OpenAIAPI

class Auth:
    def __init__(self):
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.gpt_api_key = os.getenv("GPT_API_KEY")

    def get_github_client(self) -> Github:
        if not self.github_token:
            raise ValueError("GitHub token not found. Please set the GITHUB_TOKEN environment variable.")
        return Github(self.github_token)

    def get_gpt_client(self) -> OpenAIAPI:
        if not self.gpt_api_key:
            raise ValueError("GPT API key not found. Please set the GPT_API_KEY environment variable.")
        return OpenAIAPI(api_key=self.gpt_api_key)

if __name__ == "__main__":
    auth = Auth()
    github_client = auth.get_github_client()
    gpt_client = auth.get_gpt_client()

    print("Authentication successful.")
