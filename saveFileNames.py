#This script saves the names of files on specific disk or in specific folder

path="C:\\"

import os
from os import listdir

for folder in listdir(path):
    startpath=path+folder
    f = open(folder+'.txt', 'w', encoding="utf-8");
    for root, dirs, files in os.walk(startpath):
        for file1 in files:
            f.write(root+"\\"+file1+"\n")
    f.close()        
