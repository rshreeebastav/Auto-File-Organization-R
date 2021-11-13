

import os
import shutil

# Reading the folders file
folderpath=r"D:\Study material\Semester 3\Python-I\Python Project\All files"
os.chdir(folderpath)
os.getcwd()


# CHeck the files
os.listdir()


# get extension
list_extension=[]
for fl in os.listdir():
    extension=fl.split(".")[-1]
    list_extension.append(extension)

list_extension=set(list_extension)
print(list_extension)
print(len(list_extension))

# Create a folder on the desktop
path = os.environ["Userprofile"]+"\\"+"Desktop"+"\\"+"Rahul"
print(path)
os.mkdir(path)
try:
    shutil.rmtree(path)
    os.mkdir(path)
except:
    os.mkdir(path)

# We can transfer the file with specified folder
for ex in list_extension:
    print(ex,end=",")
    os.mkdir(path+"\\"+ex)
    for fl in os.listdir():
        if ex in fl:
            shutil.copy(fl,path+"\\"+ex)
