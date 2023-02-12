liczba=int(input())
liczba2=0
t=liczba
while liczba>0: #odwrócenie - revers
    liczba2 = liczba2*10+liczba%10
    liczba= liczba//10

if liczba2 == t:
    print("Jest palindronem w dzisisiatkowym")
    
#binarny
liczba=t
liczba2=0
t=liczba
while liczba>0:
    liczba2= liczba2*2+ liczba%2
    liczba = liczba//2

if liczba2 == t:
    print("Jest palindronem w binarnym")

