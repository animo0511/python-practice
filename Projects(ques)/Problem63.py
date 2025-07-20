# Python program to rename a file to 'renamed_by_python.txt'

import os

old_name = "file.txt"
new_name = "renamed_by_python.txt"


if os.path.exists(old_name) and old_name != new_name:
    os.rename("file.txt", "renamed_by_python.txt")
    print(f"File is renamed successfully to {new_name} !")
else:
    print(f"{old_name} doesn't exists")
    print(f"OR {new_name} aready exists")