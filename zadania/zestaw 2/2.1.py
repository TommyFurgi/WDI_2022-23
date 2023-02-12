import math
liczba = int(input())
curr=1
prev=1
flaga=0
while curr<=int(math.sqrt(liczba)):
    if liczba%curr==0:
        liczba2=int(liczba/curr)
        curr2=1
        prev2=1
        while curr2<=liczba:
            if curr * curr2 == liczba:
                flaga=1
                break
            prev2, curr2 = curr2, curr2+prev2
    if flaga==1:
        print("jest iloczynem",curr, (curr2))
        break
    curr, prev = curr + prev, curr

