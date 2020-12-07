import re

class LinkClass:
    def __init__(myObj, name, link, time):
        myObj.name = name
        myObj.link = link
        myObj.time = time

urls = []
names = []
times = []
with open('links.txt', 'r') as txt_file:
    data = txt_file.read()
    urls = re.findall("(https?://[^\s]+)", data)
    names = re.findall("(?<=from )(.*)(?=to)", data)
    times = re.findall("[0-1][0-2]:[0-5][0-9] AM|[0-1][0-2]:[0-5][0-9] PM", data)


list_links = []

for (a,b,c) in zip(names, urls, times):
    l = LinkClass(a,b,c)
    list_links.append(l)

for link in list_links:
    print(f'Link: {link.link} \t Sent By: {link.name} \t At: {link.time}')