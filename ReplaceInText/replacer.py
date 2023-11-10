#This script changes all "kek1" variables found in "input.txt"
#to "newVariableName" and writes result to "output.txt"

replace = "kek1"
replace_with = "newVariableName"

f = open("input.txt", "r")
output = open("output.txt", "w")

for line in f.readlines():
    line = line.replace(replace, replace_with)
    #line = line.replace("kek2", "newVariableName2")
    output.write(line)

output.close()
f.close()
