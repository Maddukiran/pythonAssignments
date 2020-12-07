import re

file_one = open('myexample.html', 'r')
f = file_one.read()

f2 = re.sub('<.*?>','',f)
file_two = open('myexample.txt', 'x')
file_two.write(f2)

file_one.close()
file_two.close()