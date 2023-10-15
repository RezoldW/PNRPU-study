import json
import argparse

def search_airport_by_name(name_query, airport_data):
    matching_airports = []
    name_query = name_query.lower()
    for iata, airport_info in airport_data.items():
        airport_name = airport_info['Name'].lower()
        if name_query in airport_name:
            matching_airports.append(airport_info)
    return matching_airports

def main():
    parser = argparse.ArgumentParser(description="Search airports by name or part of the name.")
    parser.add_argument("name_query", help="Name or part of the name to search for")
    
    args = parser.parse_args()


    with open('airports.json', 'r') as json_file:
        airport_data = json.load(json_file)

    name_query = args.name_query
    matching_airports = search_airport_by_name(name_query, airport_data)

    if matching_airports:
        print(f"Найденные аэропорты с частью названия '{name_query}':")
        for airport in matching_airports:
            print(f"IATA код: {airport['IATA']}, Название: {airport['Name']}, Местоположение: {airport['Location']}")
    else:
        print(f"Аэропорты с частью названия '{name_query}' не найдены.")

if __name__ == "__main__":
    main()