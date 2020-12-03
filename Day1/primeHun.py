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

print('Prime numbers between ', n, ' and ', n+100, ' are: ', end='')
for i in range(n,n+100):
    if(isPrime(i)):
        print(i, end=' ')