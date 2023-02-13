def nwd(a,b):
    while b:
        a,b=b,a%b
    return a

def trojki(T):
    cnt=0
    n=len(T)
    for i in range(n):
        pierwsza=T[i]
        for a,b in [(1,2),(1,3),(2,3),(2,4)]:
            if i+b<n:
                druga=T[i+a]
                trzecia=T[i+b]
                if nwd(nwd(pierwsza,druga),trzecia)==1:
                    cnt+=1
            else:
                break
    return cnt
T=[2,4,3,2]
print(trojki(T))