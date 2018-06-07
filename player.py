#import the libraries
import urllib2
import math
import UNCSeason 
from bs4 import BeautifulSoup
import csv


#specify the URL, this is the initial URL search page, and specify starting 'soup'
starter_link = 'https://www.sports-reference.com/cbb/schools/north-carolina/'
soup = BeautifulSoup(urllib2.urlopen(starter_link),'html.parser')

#arrays to hold data
seasons=[]
statistics = []
tuples = []
for i in range(0, 107):
	parsed = soup.find_all('tr', class_='valign_top')

for i in range(0,len(parsed)):
	website = str(parsed[i].find('a').attrs['href'].encode("utf-8"))
	website = 'https://www.sports-reference.com' + website
	seasons.append(website)
	if website == 'https://www.sports-reference.com/cbb/schools/north-carolina/1949.html':
		break
# grab year to have something to join on other table 
for i in range(0,len(seasons)):
	seasonSoup = BeautifulSoup(urllib2.urlopen(seasons[i]),'html.parser')
	seasonSoupTable = seasonSoup.find_all('div', class_='table_outer_container')
	if len(seasonSoupTable) < 3:
		break
	perGame = seasonSoupTable[2]
	tBody = perGame.find('tbody').find_all('tr')
	for items in tBody:
		year=seasonSoup.find('h1').find_all('span')

		yearPlaying = year[0].text
		yearPlaying = yearPlaying[0:4]
		team = year[1].text
		statistics.append(yearPlaying)
		statistics.append(team)
		playerName = str(items.find('a').text.encode("utf-8"))
		stats = items.find_all('td')
		i = 0
		for stat in stats:
			if i < 2:
				statistics.append(stat.text.encode("utf-8"))
			else:
				if stat.text.encode("utf-8") == "":
					statistics.append(0)
				else:
					statistics.append(float(stat.text.encode("utf-8")))
			i = i+1
		tuples.append(statistics)
		statistics = []
		
		

with open('playerStats.csv','w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerows(tuples)



#last thing, figure out how to convert into floats.... 

#for i in range(0,len(seasons)):
	#if len(tuples[i]) == 24:
		#with open('playerStats.csv','w') as resultFile:
			#[resultFile.write('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},{21},{22},{23}\n'.format(tuples[i][0],tuples[i][1],tuples[i][2],tuples[i][3],tuples[i][4],tuples[i][5],tuples[i][6],tuples[i][7],tuples[i][8],tuples[i][9],tuples[i][10],tuples[i][11],tuples[i][12],tuples[i][13],tuples[i][14],tuples[i][15],tuples[i][16],tuples[i][17],tuples[i][18],tuples[i][19],tuples[i][20],tuples[i][21],tuples[i][22],tuples[i][23]))]
				


			#[resultFile.write('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},{21},{22},{23}\n'.format(tuples[i][0],player[1],player[2],player[3],player[4],player[5],player[6],player[7],player[8],player[9],player[10],player[11],player[12],player[13],player[14],player[15],player[16],player[17],player[18],player[19],player[20],player[21],player[22],player[23]))]
				







	