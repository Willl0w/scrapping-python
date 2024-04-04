import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.scrapethissite.com/pages/forms/"
base_url = "https://www.scrapethissite.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
datas = []
def scrapping ():
    for row in soup.select('table.table tr.team'):
        team = row.find('td', class_='name').get_text().strip()
        year = row.find('td', class_='year').get_text().strip()
        wins = row.find('td', class_='wins').get_text().strip()
        losses = row.find('td', class_='losses').get_text().strip()
        ot_losses = row.find('td', class_='ot-losses').get_text().strip()
        success = row.find('td', class_='pct').get_text().strip()
        gf = row.find('td', class_='gf').get_text().strip()
        ga = row.find('td', class_='ga').get_text().strip()
        diff = row.find('td', class_='diff').get_text().strip()
        datas.append([team, year, wins, losses, ot_losses, success+'%', gf, ga, diff]) 
for page in soup.select('ul.pagination li'):
    scrapping()
    href = page.find('a').get('href')
    response = requests.get(base_url + href)
    soup = BeautifulSoup(response.content, 'html.parser')
df = pd.DataFrame(datas, columns=['Team Name', 'Year', 'Wins', 'Losses', 'OT Losses', 'Win %', 'Goals For', 'Goals Against', '+/-' ])
df.to_csv('data.csv', index=False)