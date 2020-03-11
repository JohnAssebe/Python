"#Yohannes Assebe (Reading Practice)
"
import os
for main_folder,sub_folder,file_name in os.walk(r"C:\Users\User1\Desktop\PythonPractice"):
    print("The current folder is"+main_folder)
    for subs in sub_folder:
        print("Subfolders:"+subs)
    for files in file_name:
        print("files in the folders:"+files)
