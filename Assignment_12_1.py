# Write a python script to reverse a number

num, rev, rem = 342, 0, 0
while num:
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10
print()
print("Reverse is:",rev)
print()
