from os import listdir
from os.path import isdir
#print(listdir(r"D:"))
from time import sleep
"""while True:
        inp = input()
        if (inp == "go"):
            sleep(5)
            break"""
disk1=r"D:"
disk2=r""
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
