def isPrime(num):
    if num<=1:
        return False
    if num==2:
        return True
    if num>2:
        for i in range(2,num):
            if (num%i) == 0:
                return False
                break
    return True

n = int(input('Enter a number: '))
l = []
for i in range(n, n+100):
    l.append(i)
pl = []
for i in l:
    if(isPrime(i)):
        pl.append(i)
    else:
        pl.append(0)

print(pl)

count = 0
lc = 0
for i in pl:
    if(i == 0):
        count+=1
        if(count > lc):
            lc = count
    else:
        count=0

print('Longest consecutive 0s count is: ', lc)
