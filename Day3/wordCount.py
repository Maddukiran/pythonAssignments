with open('hello.txt', 'r') as myFile:

    fileContent = myFile.read()

    w = 0
    l = 0
    c = 0

    for i in fileContent:
        if(i == ' '):
            w = w + 1
        elif(i == '\n'):
            l = l + 1
        else:
            c = c + 1

    if(c > 0):
        print(f'charecter count = {c}')
        if(l>0):
            print(f'line count = {l+1}')
            print(f'word count = {w+1}')
    else:
        print('The file is empty')