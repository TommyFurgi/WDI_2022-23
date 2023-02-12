a = int(input())
b = int(input())
c = int(input())
dzielnik = 1
i=a
while i>=2:
    if(a%i==0 and b%i==0 and c%i==0):
        dzielnik = i
    i-=1
print(dzielnik)