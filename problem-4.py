import os

def print_directory_contents(path):
    """
    /
    """
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")

# Example usage
print_directory_contents('.')  # Print contents of the current directory
