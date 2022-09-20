# Write a python script to print first N terms of a Fibonacci series

n = int(input("Enter a number: "))
a, b, c = -1, 1, 0
while n:
    c = a + b
    a = b
    b = c
    print(c, end=" ")
    n -= 1
