import re
from typing import List

def efficiency_keywords_present(suggestion: str) -> bool:
    efficiency_keywords = [
        "efficiency",
        "performance",
        "optimization",
        "memory",
        "speed",
        "improve",
        "faster",
        "reduce",
        "overhead",
    ]
    return any(keyword in suggestion.lower() for keyword in efficiency_keywords)

def filter_efficiency_suggestions(suggestions: List[str]) -> List[str]:
    efficiency_suggestions = []
    for suggestion in suggestions:
        if efficiency_keywords_present(suggestion):
            efficiency_suggestions.append(suggestion)
    return efficiency_suggestions

if __name__ == "__main__":
    sample_suggestions = [
        "You can improve the performance of the add function by using the built-in sum function.",
        "Consider using a loop instead of recursion for the factorial function to reduce memory overhead.",
        "You can use list comprehension instead of a for loop to make the code more readable.",
    ]

    efficiency_suggestions = filter_efficiency_suggestions(sample_suggestions)
    for i, suggestion in enumerate(efficiency_suggestions, start=1):
        print(f"Efficiency suggestion {i}:\n{suggestion}\n")
