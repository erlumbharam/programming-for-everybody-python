# Assignment 8.5 - Guilherme Ferreira

fname = raw_input("Enter file name: ")

try:
    fh = open(fname)
except:
    print "Error: file not found!"
    exit()

count = 0
for line in fh:
    if line.startswith('From: '):
        lineSplit = line.split()
        print lineSplit[1]
        count = count + 1
        
print "There were", count, "lines in the file with From as the first word"