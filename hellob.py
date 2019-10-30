import urllib2, csv
from bs4 import BeautifulSoup

outfile = open('jaildata.csv', 'w')
writer = csv.writer(outfile)

