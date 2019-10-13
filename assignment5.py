#pull up the urllib2 package and a csv file
import urllib2, csv
#import BeautifulSoup
from bs4 import BeautifulSoup
#create a csv named jaildata to store the information 
outfile = open('jaildata.csv', 'w')
#define writer
writer = csv.writer(outfile)
#define url as the jail's website
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
#go the the jail's website and read the data
html = urllib2.urlopen(url).read()
#define soup
soup = BeautifulSoup(html, "html.parser")
#define tbody
tbody = soup.find('tbody', {'class': 'stripe'})
#define rows
rows = tbody.find_all('tr')
# for every "row" in the variable "rows"
for row in rows:
#find all the information and put them in the variable "cells"
    cells = row.find_all('td')
#create an empty list called data
    data = []
    #for every "cell" in the variable "cells"
    for cell in cells:
    	#append the information ihe list named data
        data.append(cell.text.encode('utf-8'))

    writer.writerow(data)