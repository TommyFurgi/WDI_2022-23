import math 
def czy_pierwsza(liczba): 
    if liczba == 2 or liczba == 3:
        return True
    if liczba %2 == 0 or liczba%3==0 or liczba<=1:
        return False
    i=5
    while int(math.sqrt(liczba))+1>i:
        if liczba%i == 0:
            return False
        i+=2
        if liczba%i == 0:
            return False
        i+=4
    return True

def zadanie(T):
    s=-1
    def rek(T,pos=0,skoki=0):
        if pos==len(T):
            nonlocal s
            s=skoki
            return True

        for i in range(2,T[pos]):
            if czy_pierwsza(i) and pos+i<=len(T):
                    if rek(T,pos+i,skoki+1):
                        return True
        return False
    
    rek(T)
    return s

t=[12,5,1,6,1,3]
print(zadanie(t))