# This script compares folders and files inside specified disk1 with folders and files inside specified disk2
# It compares only existance of files or folders not integrity
# You can compare folders (not disks) either, just specify location instead of disk letter. 
# Example: disk1=r"C:\myGames"

disk1=r"D:"
disk2=r"F:" 

from os import listdir
from os.path import isdir
from time import sleep
def checkFolder(addedPath):
    path1=disk1+addedPath
    path2=disk2+addedPath
    listDisk2 = listdir(path2)
    for i in listdir(path1):
        if isdir(path1+r'\\'+i) and i != "System Volume Information":
            if i not in listDisk2:
                print(path1+r'\\'+i)
            else:
                checkFolder(addedPath+r"\\"+i)
        else:
            if i not in listDisk2:
                print(path1+r'\\'+i)
checkFolder("")
