#lista przechowuje jakas liczbe binarna (jaka?)

from Node import pokaz,stworz

class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = None


def decimal(a):
    r=a
    w=0
    while r is not None:
        w=w*10+r.val
        r=r.next
    
    p=0
    dec=0
    while w>0:
        dec=dec+(w%10)*2**p
        p+=1
        w//=10
    return dec

a=stworz([1,0,1,1,0])
pokaz(a)
print(decimal(a))