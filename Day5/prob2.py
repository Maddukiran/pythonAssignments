import re

con = ''

with open('sample.html', 'r') as htmFile:
    con = htmFile.read()

con = re.sub('>', ' ', con)
links = re.findall('(https?://[^\s]+)', con)
for link in links:
    print(link)