# Assignment 7.1 - Guilherme Ferreira
# Use words.txt as the file name

fname = raw_input("Enter file name: ")

try:
    fh = open(fname)
except:
    print "Error: Name of the file invalid!"
    exit()

for line in fh:
    print line.rstrip().upper()