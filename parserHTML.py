__author__ = 'maria'

from lxml import html
from lxml import etree
from io import StringIO, BytesIO
from urllib.request import urlopen


class ParserHTML:
    def __init__(self):
        self.url = "http://online.ettu.ru"

    def parseLetters(self): #парсит первые буквы остановок, возвращает словарь из буквы и ссылки
        mimi = html.parse(urlopen(self.url))
        page = mimi.getroot()
        hrefs = page.find_class("letter-link")
        letters = dict()
        for i in hrefs:
            t = str(i.text).encode('utf-8')
            href = i.get('href')
            letters[t] = href
        return letters

    def parseStations(self, tram): #парисит названия остановок, возвращает словарь из названия остановки и ссылки
        mimi = html.parse(urlopen(self.url + tram))
        page = mimi.getroot()
        hrefs = page.iterlinks()
        hr = list()
        names = list()
        stations = dict()
        for i in hrefs:
            hr.append(i[2])
            t = str(i[0].text).encode('utf-8')
            names.append(t)
        names = names[2:-1]
        hr = hr[2:-1]
        n = len(hr)
        for i in range(n):
            stations[names[i]] = hr[i]

        return stations