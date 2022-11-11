from random import random
print("Number of iterations: ")
n = int(input())
print("Display step:")
m = int(input())

ile = 0
wew = 0

for i in range(0,n):
    x = random()
    y = random()
    ile += 1
    if x*x+y*y <= 1:
        wew += 1
    if (i+1) % m == 0:
        print(f" {i+1}: {4*wew/ile}")
