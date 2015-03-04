# Assignment 4.6 - Guilherme Ferreira

def computepay(h,r):
    if h > 40:
        total = 40 * r + (h - 40) * (1.5 * r)
    else:
        total = h * r
    return total

hrs = raw_input("Enter Hours: ")
rate = raw_input("Enter Rate: ")

hrs = int(hrs)
rate = float(rate)

p = computepay(hrs, rate)
print p