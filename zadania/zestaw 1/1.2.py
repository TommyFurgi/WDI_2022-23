def fibonacci(a,b):
   if a+b == 2022:
        return True
   elif a+b<2022:
        return fibonacci(b,a+b)  

for a in range(2,100):
    for b in range(2,100):
        if a<=b:
            if fibonacci(a,b)==True: 
                print(a, b)