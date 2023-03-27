import git
import pandas as pd
import subprocess
from run1 import *
from codeToMethodMapping import *

def get_changed_methods(commit_hash):
    # Use Git to get the diff of the current commit and its parent
    diff = subprocess.check_output(['git', 'diff', '--name-only', commit_hash + '^', commit_hash])

    # Split the diff output into individual file paths
    file_paths = diff.decode().split('\n')

    # Filter the file paths to include only Python files
    py_files = [path for path in file_paths if path.endswith('.py')]

    changed_methods = set()

    for py_file in py_files:
        # Use Git to get the diff of the current file
        file_diff = subprocess.check_output(['git', 'diff', commit_hash + '^', commit_hash, '--', py_file])

        # Split the file diff into individual lines
        file_diff_lines = file_diff.decode().split('\n')
        
        # Find lines starting with either 'def ' or 'async def '
        method_lines = [line.strip() for line in file_diff_lines if line.strip().startswith("def") or line.strip().startswith('async def ')]

        # Extract the method name from each line and add it to the set of changed methods
        for line in method_lines:
            method_name = line.split(' ')[1].split('(')[0]
            changed_methods.add(method_name)

    return changed_methods



# Path to the Git repository
repo_path = "C:/Users/adkhandelwal/Desktop/Hack_Code/.git"


# Create a Git repository object
repo = git.Repo(repo_path)

# Get the main branch
main_branch = repo.heads.main

# Get the latest commit on the main branch
latest_commit = main_branch.commit

methods_list = get_changed_methods(str(latest_commit))
print(methods_list)


# Get the previous commit on the main branch
previous_commit = latest_commit.parents[0]

# Get the list of files changed between the previous and latest commits
changed_files = repo.git.diff("--name-only", previous_commit, latest_commit).split()


# Initialize a pandas DataFrame to store the results
results_df = pd.DataFrame(columns=["file", "lines_added", "lines_removed" ,"Code_Changes", "Method_Names"])

# Iterate over each changed file and extract the lines added and removed
for file in changed_files:


     # Skip non-Python files
    if not file.endswith(".py"):
        continue

    # mapping = map_changes_to_methods(repo_path,file)
    # print(mapping)

     # Get the diff of the file between the previous and latest commits
    diff_text = repo.git.diff("-U0", previous_commit, latest_commit, file)

    # Parse the diff text into a list of lines
    diff_lines = diff_text.split("\n")

    # Extract the lines added and removed
    lines_added = 0
    lines_removed = 0
    code_changes = []
    
    for line in diff_lines:
        if line.startswith("+") and not line.startswith("+++"):
            lines_added += 1
            code_changes.append(line)
        elif line.startswith("-") and not line.startswith("---"):
            lines_removed += 1
            code_changes.append(line)
        
    # Add the file and lines added and removed to the DataFrame
    results_df = results_df.append({"file": file, "lines_added": lines_added, "lines_removed": lines_removed ,"Code_Changes": code_changes}, ignore_index=True)
    results_df['Method_Names']=methods_list
# Export the results to a CSV file
results_df.to_csv("code_changes.csv", index=False)