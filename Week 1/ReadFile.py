import os
from pathlib import Path

if os.name == "nt":  # Windows
    separator = "\\"
else:  # Linux/macOS
    separator = "/"


current_dir = os.path.dirname(os.path.realpath(__file__))
#print ("Current Directtory is :", current_dir)
#print (" Path.cwd():",  Path.cwd())
#print ("os.path.dirname(os.path.realpath(__file__)):", os.path.dirname(os.path.realpath(__file__)))
file_path = current_dir + separator + "data.txt"

print (file_path)

"""
with open(file_path, "r") as f:
    # 1. Read the whole file at once as one big string
    content = f.read()

    # 2. Read one line at a time (moves a "cursor" forward)
    line = f.readline()   # Returns "First line\n"

    # 3. Read all lines into a list
    lines = f.readlines()  # Returns ["First\n", "Second\n", ...]
"""

with open(file_path, "r") as f:
    for line in f:
        line = line.strip()  # Remove trailing newline
        print(line)
