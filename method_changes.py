import subprocess

commit_hash = "da7578974d44c302762dfc2e951e85f9adb4fd13"

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
        method_lines = [line for line in file_diff_lines if 'def' in line or line.startswith('async def ')]

        # Extract the method name from each line and add it to the set of changed methods
        for line in method_lines:
            method_name = line.split(' ')[2].split('(')[0]
            changed_methods.add(method_name)

    return changed_methods
print(get_changed_methods(commit_hash))