import os
import re
from urllib.parse import urlparse
import socket 

array = []
text_file = open('register.txt', encoding='utf-8')
print("Opening file: ", text_file)
lines = text_file.readlines()
for i in range(1, len(lines)):
    first = lines[i].strip().split(';')
    array.extend(first) # list of stuff

url = input("Enter the url you want to find: ") #url

print(url)

if url in array:
    indu = array.index(url)
    print("index of url in array:", indu)
else:
    print("URL insnt bloked in russian federation")


parsed = urlparse(url)
domain = parsed.netloc.split(".")[0:]
host = ".".join(domain)
match = re.search('www',host)
if (match):
    host = re.sub("www.","", host) #domain.subdomain
print(host)

if host in array:
    indd = array.index(host)
    print("index of domain in array:", indd)
else:
    print("Domain isnt blocked in russian federation")


ip_array = array[indd+1].strip().split(',')

#print("array of ip in the list: ", ip_array)

myip = socket.gethostbyname(host)
print("Ip of a domain: ", myip)


if myip in ip_array:
    indip = ip_array.index(myip)
    print("index of ip in array:", indip)
else:
    print("IP isnt blocked in russian federation")

