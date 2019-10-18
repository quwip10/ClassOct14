import os


for content in os.walk("c:\\class"):
    directory_path, dir_names, file_names = content
    if ".git" in directory_path:
        continue

    print("--------------------")
    print(content)
    print("--------------------")
    print()

    for f in file_names:
        if f.endswith(".txt"):
            print(f)
