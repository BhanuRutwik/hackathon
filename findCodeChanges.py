import git

# Clone or open the Git repository
repo = git.Repo("C:/Users/sbulusu/OneDrive - Informatica/Desktop/HackathonProject/hackathon/.git")
d = dict()
# Get the latest commit
latest_commit = repo.head.commit

# Get the list of files that were changed in the latest commit
changed_files = [item.a_path for item in latest_commit.diff(latest_commit.parents[0])]
print(changed_files)
# Iterate through the changed files and look for the methods that were changed
for file_path in changed_files:
    # Check if the file is a Python file
    if file_path.endswith(".py"):
        # Get the diff of the file
        file_diff = latest_commit.diff(None, paths=[file_path])
        # Iterate through the hunks in the diff
        for hunk in file_diff.iter_change_type('M'):
            print(hunk)
            print(hunk.diff)
            # Iterate through the lines in the hunk
            for line in hunk.diff.split('\n'):
                # Check if the line starts with a method definition
                if line.startswith("def "):
                    # Extract the method name
                    method_name = line[4:line.index("(")]
                    # add methods to files
                    d[file_path]=method_name
                    # Print the method name
                    print(f"Method {method_name} in file {file_path} was changed in the latest commit.")