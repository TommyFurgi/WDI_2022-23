'''Lista zawierała wartości stanowiące kolejne wyrazy ciągu geometrycznego. Z wnętrza listy usunięto
pewną liczbę elementów. Proszę napisać funkcję repair(p), (p wskazuje na pierwszy element listy),
która uzupełnia listę elementami, tak aby ponownie zawierała kolejne wyrazy ciągu geometrycznego.
Funkcja powinna zwrócić liczbę wstawionych elementów. Na przykład poniższa lista zostanie prze-
kształcona:
4 -32 -128 -2048 −→ 4 -8 16 -32 64 -128 256 -512 1024 -2048 (zostanie zwrócona wartość 6)
Można założyć, że lista wejściowa liczy więcej niż 2 elementy i każdy element listy jest liczbą całko-
witą rózną od 0 (iloraz ciągu nie musi być całkowity)
'''
from Node import stworz,pokaz
class Node():
    def __init__(self,val):
        self.val=val
        self.next=None

def repair(a): 
    prev=a
    r=a.next
    roz=nwd(prev.val,a.val)
    # while r is not None:   NIE DZIALA 
    #     k=nwd(r.val,prev.val)
    #     if abs(k)<abs(roz):
    #         roz=k
    #     r=r.next
    #     prev=prev.next
    # print(roz)
    roz=-2
    r=a.next
    prev=a
    cnt=0
    while r is not None:
        if prev.val*roz!=r.val:
            cnt+=1
            k=prev.val*roz
            new=Node(k)
            new.next=r
            prev.next=new
            prev=new
        else:
            prev=prev.next
            r=r.next
    return cnt

def nwd(a,b):
    while b:
        a,b=b,a%b
    return a

a=stworz([4, -32, -128, -2048])
pokaz(a)
print(repair(a))
pokaz(a)

