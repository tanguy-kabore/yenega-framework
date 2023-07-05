import os
# Get the absolute path of the project root directory
project_root = os.path.dirname(os.path.abspath(__file__))

# Specify the relative path to the file from the project root
relative_path = 'path/to/your/file.txt'

# Get the absolute path of the file
def path(relative_path):
    return os.path.join(project_root, relative_path)
