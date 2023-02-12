'''3. Kolejne (co najmniej dwa) elementy listy o identycznej wartości pola val nazywamy podlistą stałą. Proszę napisać
funkcję, która usuwa z listy wejściowej najkrótszą podlistę stałą. Warunkiem jej usunięcia jest istnienie w liście
dokładnie jednej najkrótszej podlisty stałej. Do funkcji należy przekazać wskaźnik na pierwszy element listy.
Funkcja powinna zwrócić liczbę usuniętych elementów.
Na przykład z listy [ 1 3 3 3 3 5 7 11 13 13 13 1 2 2 2 2 3 ] należy usunąć podlistę [13 13 13],
a z listy [1 3 3 3 3 5 7 11 13 13 13 1 2 2 2 3 ] nie należy nic usuwać.
'''
from Node import pokaz,stworz
class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = None

def zad(a):
    if a is None:
        return a
    first=None
    last=None
    guard=Node(None)
    guard.next=a
    prev=guard
    r=a    
    najdl=float('inf')
    while r is not None:
        dl=0
        if r.next is not None and r.next.val==r.val:
            tmp=prev
            k=r.val
            while r is not None and r.val==k:
                dl+=1
                prev=prev.next
                r=r.next
            else:
                if dl==najdl:
                    if dl==2:
                        return guard.next
                    first=None
                    last=None
                elif dl>1 and dl<najdl:
                    first=tmp
                    last=r
                    najdl=dl
        else:
            r=r.next
            prev=prev.next
    if first is not None:
        first.next=last
    return guard.next

a = stworz([3, 3, 3, 3, 5, 11, 13, 13, 2, 2, 2])
pokaz(a)
a=zad(a)
pokaz(a)