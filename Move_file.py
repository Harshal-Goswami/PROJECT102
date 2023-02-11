import os
import shutil

from_dir = "C:\Users\DELL"
to_dir = ""

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)

if extension = "":
    continue
if extension in ['.gif', '.png', '.jpg', '.jpeg'. '.jfif']:
    path1 = fromdir + '/' + file_name
    path2 = todir + '/' + "Image_Files"
    path3 = todir + '/' + "Image_files" '/' + file_name
    print("Path1" , path1)
    print("Part3" , path3) 

if os.path.exists(path2):
    print("Moving " + file_name + "..........")

    shutil.move(path1, path3)   

else:
    os.mkdirs(path2)
    print("Moving " + file_name + "...........")
    shutil.move(path1, path3)