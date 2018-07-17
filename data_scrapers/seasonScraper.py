#import the libraries
import urllib2
import math
import UNCSeason 
from bs4 import BeautifulSoup



#specify the URL, this is the initial URL search page, and specify starting 'soup'

starter_link = 'https://www.sports-reference.com/cbb/schools/north-carolina/'
soup = BeautifulSoup(urllib2.urlopen(starter_link),'html.parser')

#arrays to hold data
seasons=[]

for i in range(0, 107):
	parsed = soup.find_all('tr', class_='valign_top')

for i in range(0,len(parsed)):

	yearConfCoach= parsed[i].find_all('a')
	year = yearConfCoach[0].text.encode("utf-8")
	conf = yearConfCoach[1].text.encode("utf-8")
	coach = yearConfCoach[2].text.encode("utf-8")

	rightJuxtaposed = parsed[i].find_all('td',class_='right')
	winPercent = rightJuxtaposed[2].text.encode("utf-8")
	averagePoints = rightJuxtaposed[8].text.encode("utf-8")
	if averagePoints =="" :
		#print "here"
		averagePoints = 0
	newSeason = (year[0:4], conf, coach, float(winPercent), float(averagePoints))
	seasons.append(tuple(newSeason))
with open('seasons.csv','w') as resultFile:
		[resultFile.write('{0},{1},{2},{3},{4}\n'.format(season[0],season[1],season[2],season[3],season[4])) for season in seasons]
	