import re
import git

def map_changes_to_methods(repo_path, file_path):
    """Map code changes to method names in the given file of the given Git repository."""
    # Clone the repository and retrieve the commits that changed the file
    repo = git.Repo(repo_path)
    file_commits = list(repo.iter_commits(paths=file_path))

    # Define regular expressions for the beginning and end of a method
    method_start = re.compile(r'^\s*def\s+(\w+)\(.*\):\s*$')
    method_end = re.compile(r'^\s*(return|\s*$|\s*#.*)')

    # Iterate over the commits and find the lines that belong to each method
    method_lines_by_commit = {}
    for commit in file_commits:
        # Get the code of the commit
        code = commit.tree[file_path].data_stream.read().decode()

        # Iterate over the lines of code and find the lines that belong to each method
        method_lines = []
        in_method = False
        for line in code.split('\n'):
            if method_start.match(line):
                # This line starts a new method
                in_method = True
                method_name = method_start.search(line).group(1)
                method_lines = [line]
            elif in_method:
                # We're inside a method, so check if this line ends it
                if method_end.match(line):
                    in_method = False
                    method_lines_by_commit.setdefault(commit.hexsha, {}).setdefault(method_name, []).extend(method_lines)
                    method_lines = []
                else:
                    method_lines.append(line)

    # Remove the temporary repository
    # repo.close()
    # git.util.rmtree('temp_repo')

    return method_lines_by_commit
