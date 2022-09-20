"""
Write a python script to print all Prime numbers between 
two given numbers (both values inclusive) 
"""

x, y = 1, 20
for i in range(x, y + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
