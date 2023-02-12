a = int(input())
b = int(input())
c = int(input())
dzielnik = 1
i = 2
while i<=a:
    if a%i == 0 and b%i == 0:
        dzielnik = i 
    i += 1
wielokrotnosc = int(a*b/dzielnik)
i=2
dzielnik = 1
while i <= c:
    if c%i == 0 and wielokrotnosc%i == 0:
        dzielnik = i 
    i+=1
print(int(c*wielokrotnosc/dzielnik))