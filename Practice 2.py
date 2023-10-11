import requests
from bs4 import BeautifulSoup

# URL страницы с таблицей
url = "https://ucsol.ru/tamozhennoe-oformlenie/v-aeroportakh-uslugi-tamozhennogo-brokera/kody-vsekh-aeroportov-mira-iata"

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Найдите основную таблицу
    main_table = soup.find('table', {'class': 'tablesorter btab w100p'})

    # Создайте список для хранения данных
    data = []

    # Найдите все строки в таблице и извлеките данные
    for row in main_table.find_all('tr'):
        columns = row.find_all('td')

        # Проверьте, что есть хотя бы две ячейки в строке
        if len(columns) >= 3:
            airport_iata_code = columns[0].text.strip()  # Получить текст из первой ячейки и удалить лишние пробелы
            airport_icao_code = columns[1].text.strip()  # Получить текст из третьей ячейки и удалить лишние пробелы
            airport_name = columns[2].text.strip()
            airport_location = columns[3].text.strip()
            airport_country = columns[4].text.strip()
            data.append((airport_iata_code, airport_icao_code, airport_name, airport_location, airport_country))
    for iata, icao, name, location, country in data:
        print(f"IATA код:",iata, "ICAO код:",icao, "Аэропорт:",name, "Местоположение:",location, "Страна:", country)
else:
    print(f"Ошибка при запросе к {url}")





url = "https://ucsol.ru/tamozhennoe-oformlenie/v-aeroportakh-uslugi-tamozhennogo-brokera/airport-codes-ba-bz"

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Найдите основную таблицу
    main_table = soup.find('table', {'class': 'tablesorter btab w100p'})

    # Создайте список для хранения данных
    data = []

    # Найдите все строки в таблице и извлеките данные
    for row in main_table.find_all('tr'):
        columns = row.find_all('td')

        # Проверьте, что есть хотя бы две ячейки в строке
        if len(columns) >= 3:
            airport_iata_code = columns[0].text.strip()  # Получить текст из первой ячейки и удалить лишние пробелы
            airport_icao_code = columns[1].text.strip()  # Получить текст из третьей ячейки и удалить лишние пробелы
            airport_name = columns[2].text.strip()
            airport_location = columns[3].text.strip()
            data.append((airport_iata_code, airport_icao_code, airport_name, airport_location))
    for iata, icao, name, location in data:
        print(f"IATA код:",iata, "ICAO код:",icao, "Аэропорт:",name, "Местоположение:",location)
else:
    print(f"Ошибка при запросе к {url}")


