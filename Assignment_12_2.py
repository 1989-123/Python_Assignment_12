# Write a python script to check whether a given number is Prime or not

x = 9
for i in range(2, x):
    if x % i == 0:
        print("Not a prime")
        break
else:
    print("Number is prime")
