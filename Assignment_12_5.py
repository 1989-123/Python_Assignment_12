# Write a python script to find next prime number of a given number

x = 13
while True:
    n = x + 1
    for i in range(2, n):
        if n % i == 0:
            n += 1
    else:
        print()
        print("Next prime is:",n)
        print()
        break
