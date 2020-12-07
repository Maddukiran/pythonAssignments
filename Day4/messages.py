import re

urls = []
with open('links.txt', 'r') as txt_file:
    data = txt_file.read()
    urls = re.findall("(https?://[^\s]+)", data)

for url in urls:
    print(url)