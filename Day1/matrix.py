m = int(input('Enter number of rows: '))
n = int(input('Enter number of columns: '))

ll = []
l = []
print('Enter elements one by one: ')
for i in range(m):
    for j in range(n):
        l.append(int(input()))
    ll.append(l)
    l = []
for i in ll:
    for j in i:
        print(j, end=' ')
    print()