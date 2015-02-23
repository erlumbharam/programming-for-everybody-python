# Assignment 3.3 - Guilherme Ferreira

score = raw_input("Enter the score: ")

score = float(score)

if(score > 1.0):
    print "Error: Value out of the range ( more than 1.0 )"
    exit()
elif(score < 0.0):
	print "Error: Value out of the range ( less than 0.0 )"
	exit()

if(score >= 0.9):
    print "A"
elif(score >= 0.8):
    print "B"
elif(score >= 0.7):
    print "C"
elif(score >= 0.6):
    print "D"
elif(score < 0.6):
    print "F"