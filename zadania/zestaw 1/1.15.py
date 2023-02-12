import math
product = math.sqrt(0.5)
next=product
for _ in range(1000):
    next = math.sqrt(0.5 + 0.5*next)
    product *= next

pi = 2/product
print(pi)