'''Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
class Node:
..def init(self,val,next=None):
....self.val = val
....self.next = next
Lista zawierała wartości stanowiące kolejne wyrazy ciągu arytmetycznego. Z wnętrza listy usunięto
pewną liczbę elementów. Proszę napisać funkcję repair(p), (p wskazuje na pierwszy element listy) która
uzupełnia listę elementami, tak aby ponownie zawierała kolejne wyrazy ciągu arytmetycznego. Funkcja
powinna zwrócić liczbę wstawionych elementów.
Komentarz: Można założyć, że lista wejściowa liczy więcej niż 2 elementy
'''
from Node import pokaz,stworz
class Node():
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def roznica(a,b):
    if a>b:
        minus=True
    
    i=2
    while i<=a and i<=b:
        if abs(a-b)%i==0:
            break
        i+=1
    if minus==True:
        i*=-1
    return i

def repair(p):
    a=p.val
    b=p.next.val
    
    r=roznica(p.val,p.next.val)

    cnt=0
    prev=p
    p=p.next
    while p is not None:
        if prev.val+r!=p.val:
            cnt+=1
            new=Node(prev.val+r,p)
            prev.next=new
            prev=new
        else:
            prev=prev.next
            p=p.next
    return cnt


a=stworz([17,5,2])
pokaz(a)
print(repair(a))
pokaz(a)