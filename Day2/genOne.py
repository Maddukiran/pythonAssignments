myList = [
    [213, 'aaaA', 100.12, 'f'],
    [121, 'aaAa', 123.44, 'm'],
    [111, 'aAaa', 111.54, 'm'],
    [130, 'AaaA', 185.98 , 'f']
]

l = len(myList)

#sorting

for i in range(l):
    for j in range(3):
        if(myList[j][0] > myList[j+1][0]):
            myList[j][0], myList[j+1][0] = myList[j+1][0], myList[j][0]
#prefixing
#add 10% increment
for i in range(l):
    if(myList[i][3] == 'm'):
        myList[i][1] = 'Mr.' + myList[i][1]
    elif(myList[i][3] == 'f'):
        myList[i][1] = 'Ms.' + myList[i][1]
    myList[i][2] = myList[i][2] + (myList[i][2] * 0.1)

print(myList)