import requests
import json
import argparse
from bs4 import BeautifulSoup

url = "https://ucsol.ru/tamozhennoe-oformlenie/v-aeroportakh-uslugi-tamozhennogo-brokera/kody-vsekh-aeroportov-mira-iata"
alpha =['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
data = {}

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    main_table = soup.find('table', {'class': 'tablesorter btab w100p'})
    for row in main_table.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) >= 3:
            airport_iata_code = columns[0].text.strip()
            airport_icao_code = columns[1].text.strip()
            airport_name = columns[2].text.strip()
            airport_location = columns[3].text.strip()
            data[airport_iata_code] = {
                'IATA': airport_iata_code,
                'ICAO': airport_icao_code,
                'Name': airport_name,
                'Location': airport_location
            }
else:
    print(f"Ошибка при запросе к {url}")

for letter in alpha:
    url = f'https://ucsol.ru/tamozhennoe-oformlenie/v-aeroportakh-uslugi-tamozhennogo-brokera/airport-codes-{letter}a-{letter}z'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        main_table = soup.find('table', {'class': 'tablesorter btab w100p'})

        for row in main_table.find_all('tr'):
            columns = row.find_all('td')
            if len(columns) >= 3:
                airport_iata_code = columns[0].text.strip()
                airport_icao_code = columns[1].text.strip()
                airport_name = columns[2].text.strip()
                airport_location = columns[3].text.strip()
                data[airport_iata_code] = {
                    'IATA': airport_iata_code,
                    'ICAO': airport_icao_code,

                                        'Name': airport_name,
                    'Location': airport_location
                }
    else:
        print(f"Ошибка при запросе к {url}")

with open('airports.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)














# for iata, icao, name, location in data:
#     print(f"IATA код:",iata, "ICAO код:",icao, "Аэропорт:",name, "Местоположение:",location)
