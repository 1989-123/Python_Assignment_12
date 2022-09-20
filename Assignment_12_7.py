"""
Write a python script to check whether a given pair of 
numbers are co-Prime numbers or not.
"""

x, y = 5, 8
h = min(x, y)
while h >= 1:
    if x % h == 0 and y % h == 0:
        if h == 1:
            print("Co-prime Numbers")
            break
        else:
            print("Not a Co-prime")
            break
    h -= 1
