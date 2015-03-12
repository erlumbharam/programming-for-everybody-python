# Assignment 6.5 - Guilherme Ferreira

largest = None
text = "X-DSPAM-Confidence:    0.8475"

first_zero = text.find("0")
print float(text[first_zero:])