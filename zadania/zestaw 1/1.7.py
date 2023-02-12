liczba = int(input("Podaj liczbe: "))
prev=0
curr=1
while True:
    if prev*curr==liczba:
        print("Jest iloczynem") 
    if prev*curr >= liczba:
        break
    prev, curr = curr, prev+curr