n=int(input('Enter a number: '))

res = n%2==0

if(res):
    print('Even:', end=' ')
    for i in range(n,n+10,2):
        print(i, end=' ')
    print()
    print('Odd: ', end=' ')
    for i in range(n+1,n+10,2):
        print(i, end=' ')
else:
    print('Odd: ', end=' ')
    for i in range(n,n+10,2):
        print(i, end=' ')
    print()
    print('Even:', end=' ')
    for i in range(n+1,n+10,2):
        print(i, end=' ')