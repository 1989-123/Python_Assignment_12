# Write a python script to calculate HCF of two numbers

x, y = 24, 36
h = min(x, y)
while h >= 1:
    if x % h == 0 and y % h == 0:
        print("HCF is:",h)
        break
    h -= 1
