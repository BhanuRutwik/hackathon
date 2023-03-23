import git
import pandas as pd


# Path to the Git repository
repo_path = "C:/Users/sbulusu/OneDrive - Informatica/Desktop/HackathonProject/hackathon/.git"


# Create a Git repository object
repo = git.Repo(repo_path)

# Get the main branch
main_branch = repo.heads.main

# Get the latest commit on the main branch
latest_commit = main_branch.commit

# Get the previous commit on the main branch
previous_commit = latest_commit.parents[0]

# Get the list of files changed between the previous and latest commits
changed_files = repo.git.diff("--name-only", previous_commit, latest_commit).split()


# Initialize a pandas DataFrame to store the results
results_df = pd.DataFrame(columns=["file", "lines_added", "lines_removed" , "Code_Removed" , "Code_Added"])

# Iterate over each changed file and extract the lines added and removed
for file in changed_files:
     # Skip non-Python files
    if not file.endswith(".py"):
        continue

     # Get the diff of the file between the previous and latest commits
    diff_text = repo.git.diff("-U0", previous_commit, latest_commit, file)

    # Parse the diff text into a list of lines
    diff_lines = diff_text.split("\n")

    # Extract the lines added and removed
    lines_added = 0
    lines_removed = 0
    code_added = []
    code_removed = []
    for line in diff_lines:
        if line.startswith("+") and not line.startswith("+++"):
            lines_added += 1
            code_added.append(line)
        elif line.startswith("-") and not line.startswith("---"):
            lines_removed += 1
            code_removed.append(line)


    # Add the file and lines added and removed to the DataFrame
    results_df = results_df.append({"file": file, "lines_added": lines_added, "lines_removed": lines_removed ,"Code_Removed": code_removed ,"Code_Added": code_added}, ignore_index=True)

# Export the results to a CSV file
results_df.to_csv("code_changes.csv", index=False)