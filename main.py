__author__ = 'maria'
from parserHTML import ParserHTML

parser = ParserHTML()
letters = parser.parseLetters()
for t in letters:
    print(t, letters[t])
stations = parser.parseStations("/stations/4")
for s in stations:
    print(s, stations[s])