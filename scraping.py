import requests, mechanize
from bs4 import BeautifulSoup

url = "https://www.mshp.dps.missouri.gov/HP68/SearchAction?searchDate=10/31/2017"
br = mechanize.Browser()
br.open(url)
html = br.response().read()

soup = BeautifulSoup(html, "html.parser")

main_table = soup.find("table", {"class": "accidentOutput"})
row_list = main_table.find_all("tr")


#test_row = row_list[0]
#table_cells = test_row.find_all("td")

for row in row_list:
	table_cells = row.find_all("td")
for cell in table_cells:
	print (cell.text)


