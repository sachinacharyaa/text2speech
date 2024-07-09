# Label the program written in problem 4 with comments. 


import os

def print_directory_contents(path):
    try:
        contents = os.listdir(path)
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")

print_directory_contents('.')  
