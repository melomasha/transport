__author__ = 'maria'
from http.client import HTTPConnection
from urllib.parse import urlencode
from lxml import html
from lxml import etree
from io import StringIO, BytesIO
import copy
from urllib.request import urlopen

parser = etree.HTMLParser(encoding='utf-8')
mimi = html.parse(urlopen("http://online.ettu.ru/stations/1"))
page = mimi.getroot()
#page.tohtml()
hrefs = page.iterlinks()
#l = hrefs.len()
#hh = hrefs.copy.copy()
hr = list()
names = list()
stations = dict()
#k = 0
"""
for i in hrefs:
    t= i[2]
    hr.append(i[2])
    r = str(i[0].text).encode('utf-8')
    stations[r] = t
"""
for i in hrefs:
    hr.append(i[2])
    r = str(i[0].text).encode('utf-8')
    names.append(r)
names = names[2:-1]
hr = hr[2:-1]
n = len(hr)
for i in range(n):
    stations[names[i]] = hr[i]

for t in stations:
    print(bytes(t).decode('utf-8'))


"""
url = "http://online.ettu.ru"
tram = "/stations/4"
mimi = html.parse(urlopen(url + tram))
page = mimi.getroot()
hrefs = page.iterlinks()
#l = hrefs.len()
#hh = hrefs.copy.copy()
hr = list()
stations = dict()
#k = 0
for i in hrefs:
    t= i[2]
    hr.append(i[2])
    r = str(i[0].text).encode()
    stations[r] = t

    #k+=1

#links = page.xpath("\\a")
hr = hr[2:-1]
for t in stations:
    print(t.decode("cp1251"))
#print(type(hrefs))
"""

