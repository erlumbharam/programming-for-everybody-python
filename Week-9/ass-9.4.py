# Assignment 9.4 - Guilherme Ferreira

name = raw_input("Enter file: ")

try:
    handle = open(name)
except:
    print "File not found!"

mailDict = dict()

for line in handle:
    if line.startswith("From: "):
        lineSplit = line.split()
        mailDict[lineSplit[1]] = mailDict.get(lineSplit[1], 0) + 1


maximum = None
key = None

for mail in mailDict:
    if mailDict[mail] > maximum:
        maximum = mailDict[mail]
        key = mail
        
print key,mailDict[key]

