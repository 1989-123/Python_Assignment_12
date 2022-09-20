# Write a python script to print first N prime numbers

x, n = 2, 15
while n:
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        print(x, end=" ")
        n -= 1
    x += 1
