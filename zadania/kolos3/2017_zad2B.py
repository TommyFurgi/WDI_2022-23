'''Zbiór liczb naturalnych jest reprezentowany jako jednokierunkowa lista. Y-lista to struktura
reprezentująca dwa zbiory liczb naturalnych (rysunek).

Proszę napisać funkcję, która dwa zbiory A,B reprezentowane jako Y-lista przekształca w dwa
zbiory reprezentowane jako niezależne listy. Do funkcji należy przekazać wskaźniki do dwóch
list, funkcja powinna zwrócić liczbę elementów części wspólnej zbiorów A,B.'''

from Node import pokaz,stworz
class Node():
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def zad(a,b):
    cnt=0
    g=Node(None,a)
    prev=g
    w=a

    while w is not None:
        q=b
        while q is not None:
            if q is w:
                while q is not None:
                    cnt+=1
                    new=Node(q.val,None)
                    prev.next=new
                    prev=new
                    q=q.next 
                a=g.next
                g.next=None
                return cnt
            else:
                q=q.next
        w=w.next
        prev=prev.next
    
    return 0

d=Node(2,None)
c=Node(3,d)
b=Node(11,c)
a=Node(5,b)

x=Node(17,c)
y=Node(7,x)
z=Node(13,y)

print(zad(a,z))