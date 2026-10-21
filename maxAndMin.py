n = 453443710

maxDigit = 0
minDigit = 9
while n >0:
    digit = n % 10
    if digit > maxDigit:
        maxDigit = digit
    if digit < minDigit:
        minDigit = digit
    n = n // 10
print("Maximum digit:", maxDigit)               
print("Minimum digit:", minDigit)