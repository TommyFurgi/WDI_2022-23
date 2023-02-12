def pom(suma,i):
    a,b=1,1
    while True:
        if suma==i:
            return False
        elif suma<i:
            return True
        else:
            suma-=a
            a,b=b,a+b
def fun(n):
    a,b=1,1
    suma=2
    i=n+1
    while True:
        while suma<i:
            suma+=a+b
            a,b=b,a+b
        if pom(suma,i):
            return i
        i+=1
        
print(fun(9))