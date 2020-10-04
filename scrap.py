from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://anitrendz.net/"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'lxml')
sum = 0
konten = {"tipe": "Chart Leaders", "content" : []}
count = 0
for tag in soup.find_all(class_="at-clb-details"):
    count+=1
    if count > 3 : break
    konten["content"].append({"chart-name": re.findall('[A-Z].*',tag.find(class_="at-cl-chart-name").contents[0].rstrip())[0], 
        "chart-week": re.findall('[A-Z].*',tag.find(class_="at-cl-chart-week").contents[0].rstrip())[0],
        "cl-name": re.findall('[A-Z].*',tag.find(class_="at-cl-name").contents[0].rstrip())[0], 
        "cl-detail": re.findall('[A-Z].*',tag.find(class_="at-cl-detail").contents[0].rstrip())[0]})
print(konten)

