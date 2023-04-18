from typing import List

from openai import OpenAIAPI

from auth import Auth

def generate_prompt(code: str) -> str:
    return f"Review the following code and suggest improvements:\n\n```python\n{code}\n```\n\nSuggestions:\n"

def get_suggestions(gpt_client: OpenAIAPI, prompt: str) -> str:
    response = gpt_client.create_completion(
        engine="text-davinci-codex",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def analyze_code(gpt_client: OpenAIAPI, code_files: List[str]) -> List[str]:
    suggestions = []
    for code in code_files:
        prompt = generate_prompt(code)
        suggestion = get_suggestions(gpt_client, prompt)
        suggestions.append(suggestion)
    return suggestions

if __name__ == "__main__":
    auth = Auth()
    gpt_client = auth.get_gpt_client()

    sample_code_files = [
        """
def add(a, b):
    return a + b
""",
        """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
""",
    ]

    suggestions = analyze_code(gpt_client, sample_code_files)
    for i, suggestion in enumerate(suggestions, start=1):
        print(f"Suggestions for code file {i}:\n{suggestion}\n")
