# Assignment 8.4 - Guilherme Ferreira

fname = raw_input("Enter file name: ")

try:
    fh = open(fname)
except:
    print "Error: file not found!"
    exit()

lst = list()
for line in fh:
    lineSplit = line.split()
    for word in lineSplit:
        if lst.count(word) < 1:
            lst.append(word)

lst.sort()
print lst
