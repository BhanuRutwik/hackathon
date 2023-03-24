# import os
# import subprocess



# def get_code_changes(commit_sha):
#      # Get the changed files in the commit
#     changed_files = subprocess.check_output(["git", "show", "--name-only", "--pretty=format:", commit_sha]).split()



#      # Filter for Python files
#     python_files = [f.decode("utf-8") for f in changed_files if f.decode("utf-8").endswith(".py")]



#      # Get the lines of code that were added or removed for each method in each file
#     code_changes = {}
#     for file in python_files:
#         code_changes[file] = {}
#         git_diff = subprocess.check_output(["git", "diff", "--unified=0", commit_sha, "--", file]).decode("utf-8")



#         # Split the diff into individual hunks
#         hunks = git_diff.split("\n@@")[1:]

        

#         for hunk in hunks:
#             print(hunk)
#             # Extract the starting line number of the hunk
#             start_line = int(hunk.split("\n")[0].split("+")[1].split(",")[0])



#             # Extract the lines of code that were added or removed
#             added_lines = [l[1:] for l in hunk.split("\n")[1:] if l.startswith("+")]
#             removed_lines = [l[1:] for l in hunk.split("\n")[1:] if l.startswith("-")]



#              # Find the method that the hunk belongs to
#             method_name = None
#             with open(file) as f:
#                 for i, line in enumerate(f, start_line):
#                     if line.startswith("def "):
#                         method_name = line.split("(")[0][4:]
#                     if i >= start_line+len(added_lines):
#                         break



#              # Store the added and removed lines for the method
#             if method_name is not None:
#                 if method_name not in code_changes[file]:
#                     code_changes[file][method_name] = {"added": [], "removed": []}
#                 code_changes[file][method_name]["added"].extend(added_lines)
#                 code_changes[file][method_name]["removed"].extend(removed_lines)



#     return code_changes


# from ast import *
# import ast
# import git
# import difflib

# from pytest import Parser

# def ast_diff(before, after):
#     """
#     Returns a list of AST nodes that represent the differences between two Python code strings.
#     """
#     before_ast = ast.parse(before)
#     after_ast = ast.parse(after)
#     return list(difflib.SequenceMatcher(None, ast.dump(before_ast), ast.dump(after_ast)).get_opcodes())

# def get_code(contents, node):
#     """
#     Returns the code associated with an AST node in a Python code string.
#     """
#     lines = contents.split('\n')
#     start_lineno, end_lineno = node.lineno, node.end_lineno
#     start_col_offset, end_col_offset = node.col_offset, node.end_col_offset
#     if start_lineno == end_lineno:
#         code = lines[start_lineno-1][start_col_offset:end_col_offset]
#     else:
#         code = lines[start_lineno-1][start_col_offset:]
#         for lineno in range(start_lineno+1, end_lineno-1):
#             code += '\n' + lines[lineno-1]
#         code += '\n' + lines[end_lineno-2][:end_col_offset]
#     return code

# # Path to the Git repository
# repo_path = 'C:/Users/sbulusu/OneDrive - Informatica/Desktop/HackathonProject/hackathon/.git'

# # Initialize a GitPython Repo object
# repo = git.Repo(repo_path)

# # Get the latest commit object
# latest_commit = repo.head.commit

# # Get the current commit object
# # current_commit = repo.active_branch.
# current_commit = repo.active_branch.commit

# # Get the diff between the latest and current commits
# diff = latest_commit.diff(current_commit)
# print(diff)
# # Iterate over the diff to get the code changes and method names
# for file_diff in diff:

#     # Check if the file is a Python file
#     if file_diff.a_path.endswith('.py'):
#         # Get the file contents before and after the changes
#         before_contents = file_diff.a_blob.data_stream.read().decode('utf-8')
#         after_contents = file_diff.b_blob.data_stream.read().decode('utf-8')
        
#         # Parse the code changes to get the method names and changes
#         parser = Parser()
#         before_ast = parser.parse(before_contents)
#         after_ast = parser.parse(after_contents)
#         diff = ast_diff(before_ast, after_ast)
        
#         # Get the method names that changed and their associated code changes
#         for node in diff:
#             if isinstance(node, ast.FunctionDef):
#                 method_name = node.name
#                 method_before = get_code(before_contents, node)
#                 method_after = get_code(after_contents, node)
#                 print(f"Method {method_name} changed in file {file_diff.a_path}:")
#                 print(f"Before:\n{method_before}")
#                 print(f"After:\n{method_after}")



import git
import difflib

# Path to the Git repository
repo_path = "C:/Users/sbulusu/OneDrive - Informatica/Desktop/HackathonProject/hackathon/.git"

# Initialize the Git repository object
repo = git.Repo(repo_path)

# Get the previous and current commit objects
prev_commit = repo.head.commit.parents[0]
current_commit = repo.head.commit

# Get the diff between the previous and current commits
d = prev_commit.diff(current_commit)
print(d)
# Loop through the diff and extract method changes
for change in d.iter_change_type('M'):
    # print(change)
    # Get the file path and diff content
    file_path = change.b_path
    print(file_path)
    diff_content = change.diff
    print(diff_content)
    
    # Use difflib to extract the changed lines
    changed_lines = [line for line in diff_content.split('\n') if line.startswith('+') or line.startswith('-')]
    
    # Loop through the changed lines and extract method changes
    for line in changed_lines:
        if line.startswith('+ def') or line.startswith('- def'):
            # Extract the method name and code
            method_name = line.split()[1]
            method_code = difflib.unified_diff([], [line], lineterm='', n=0)
            method_code = '\n'.join(list(method_code)[2:])
            
            # Print the method name and code
            print(f"Method: {method_name}\nCode:\n{method_code}")
