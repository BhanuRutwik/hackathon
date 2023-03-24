import os

def list_files():
    files = os.listdir('.')
    return [f for f in files if os.path.isfile(f)]
print("Files present in current directory:", list_files())