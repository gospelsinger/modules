import os

# 1
current_dir = os.getcwd()
os.mkdir("file_management")
os.chdir(os.path.join(current_dir, "file_management"))

with open("file1.txt", "w", encoding="utf-8") as file:
    file.write("This is some text in file 1\n")
with open("file2.txt", "w", encoding="utf-8") as file:
    file.write("This is some text in file 2\n")

print(os.listdir())

# 2
os.remove("file1.txt")
os.mkdir("one_more_folder")
os.rename("./file2.txt", "./one_more_folder/file2.txt")
os.remove(os.path.join(current_dir, "file_management", "one_more_folder", "file2.txt"))
os.rmdir(os.path.join(current_dir, "file_management", "one_more_folder"))

os.chdir(current_dir)
os.rmdir("file_management")
