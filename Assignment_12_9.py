# Write a python script to calculate LCM of two numbers

x, y = 4, 6
l = max(4, 6)
while l <= x * y:
    if l % x == 0 and l % y == 0:
        print("Lcm is:",l)
        break
    l += 1
