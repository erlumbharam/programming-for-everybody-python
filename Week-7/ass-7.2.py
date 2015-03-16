# Assignment 7.2 - Guilherme Ferreira
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")

try:
    fh = open(fname)
except:
    print "Error: Name of the file invalid!"
    exit()

count = 0
values = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
        
    count = count + 1
    
    zdigit = line.find("0")
    
    values = values + float(line[zdigit:])
    

print "Average spam confidence:", (values/count)
