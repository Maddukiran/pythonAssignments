
v = {}
a = {}
current = v
with open('Roget.net') as myFile:
    fileContent = myFile.read().splitlines()
    for line in fileContent:
        cl = line.split(' ', 1)

        if(cl[0] == '*Vertices'):
            current = v

        elif(cl[0] == '*Arcslist'):
            current = a

        else:
            current[int(cl[0])] = cl[1]

n = int(input('Enter a number: '))

print(f'Vertices --> {v[n]} \n ArcString --> {a[n]}')