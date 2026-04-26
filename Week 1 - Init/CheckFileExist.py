import os

print(os.path.curdir)
# Join paths safely (uses the right separator for the OS)
path = os.path.join("folder", "file.txt")
print(path)   # "folder/file.txt" on Mac/Linux

# Check if a file or folder exists
if os.path.exists("data.txt"):
    print("File found!")
else:
    print("File not found")

#with open("data.txt", "a") as f:
#    f.write("This is new line \n")\
print('How are you?')