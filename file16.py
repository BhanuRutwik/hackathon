import os

def list_files():
    print("finding the list")
    files = os.listdir('.')
    return [f for f in files if os.path.isfile(f)]

print("Files that are in current directory:", list_files())
print("file16")