
w = 3
c = w-1
print('sun mon tue wed thu fri sat')
print(' ' * ((w-1) * 4), end='')

for var in range(1,32):
    print(f'{var:<3}', end = ' ')
    c+=1
    if(c==7):
        c=0
        print()