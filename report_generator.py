import os
from typing import Dict, List

def generate_report(repo_name: str, suggestions: List[str], output_dir: str = "reports"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    report_file_path = os.path.join(output_dir, f"{repo_name}_efficiency_report.txt")

    with open(report_file_path, "w") as report_file:
        report_file.write(f"Efficiency Improvement Suggestions for {repo_name}\n")
        report_file.write("=" * 80 + "\n\n")

        for i, suggestion in enumerate(suggestions, start=1):
            report_file.write(f"Suggestion {i}:\n{suggestion}\n\n")

    print(f"Generated report for {repo_name} at {report_file_path}")

if __name__ == "__main__":
    sample_repo_name = "example-repo"
    sample_suggestions = [
        "You can improve the performance of the add function by using the built-in sum function.",
        "Consider using a loop instead of recursion for the factorial function to reduce memory overhead.",
    ]

    generate_report(sample_repo_name, sample_suggestions)
