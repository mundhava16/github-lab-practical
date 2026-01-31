import random

s = int(input("enter starting number"))
e = int(input("enter ending number"))

for i in range(s,e):
    print(random.randint(s,e))
