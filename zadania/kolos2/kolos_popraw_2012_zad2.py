'''
2. Napisz procedurę, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie co najmniej
dwucyfrowe liczby pierwsze, powstale poprzez wykreślenie z liczby pierwotnej co najmniej jednej cyfry.
'''

def rek(n,l=0,pos=0,flag=False):
    if n==0:
        if l>9 and flag==True:
            print(l)
    else:
        rek(n//10,l,pos,True)
        rek(n//10,l+(n%10)*10**pos,pos+1,flag)

rek(1234)
        