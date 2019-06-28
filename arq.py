import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from time import sleep


for i in range(4,10):
    html = 'file:///home/jozemaria/Documentos/Scraping/html/201'
    html = f'{html}{i}.html'
    array = urlopen(html)


    bsObj = bs(array)
    table = bsObj.find("table",{"class":"dataTable"})
    rows = table.find_all("tr")

    csvFile = open("editors.csv", 'a')
    writer = csv.writer(csvFile)

    try:
        for row in rows:
            csvRow = []
            for cell in row.find_all(['th', 'td']):
                csvRow.append(cell.get_text())
                if 'Detalhar' in csvRow:
                    csvRow.remove('Detalhar')
                # csvRow = [csv.replace('"', ',') for csv in csvRow]
            writer.writerow(csvRow)
    finally:
        csvFile.close()

