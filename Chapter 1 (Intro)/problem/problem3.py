import os

def print_directory_contents(path="."):
    try:
        contents = os.listdir(path)
        print(f"Contents of '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Directory '{path}' not found.")
    except PermissionError:
        print(f"Permission denied for '{path}'.")


print_directory_contents()
