# Assignment 3.1 - Guilherme Ferreira

hrs = raw_input("Enter Hours: ")
hrs = float(hrs)

rate = raw_input("Enter Rate: ")
rate = float(rate)

if hrs > 40:
    total = 40 * rate + (hrs - 40) * (1.5 * rate)
else:
    total = hrs * rate

print total