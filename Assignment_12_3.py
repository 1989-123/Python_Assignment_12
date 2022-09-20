# Write a python script to print all Prime numbers under 100

x = 100
for x in range(2, x):
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        print(x, end=" ")
