import WeatherClient
import json

def main():
    with open("settings.json", "r") as json_file:
        s = json.load(json_file)
    global WEATHER_FETCHER 
    WEATHER_FETCHER = WeatherClient.WeatherFetcher(s["Settings"])

    print_menu()

    while True:
        choice = input("Please select an option (1, 2, 3, 4, or 5): ")
        if not choice in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
        elif choice == '1':            
            get_weather_for_city(days=1)
        elif choice == '2':
            get_weather_for_city(days=7)
        elif choice == '3':
            list_cities()
        elif choice == '4':
            settings()
        elif choice == '5':
            print("Exiting the Weather App. Goodbye!")
            break

def print_menu():
    print(f"Welcome to the Weather App!")
    print(f"Options")
    print(f"1. Weather for one day")
    print(f"2. Weather for 7 days")
    print(f"3. List Cities")
    print(f"4. Settings")
    print(f"5. Exit")

def get_weather_for_city(days=1):
    city = input("Enter the city name: ")
    coordinates = WEATHER_FETCHER.get_coordinates(city)
    if not coordinates:
        print(f"City '{city}' not found. Please try again.")
        return None
    weather_data = WEATHER_FETCHER.fetch_weather(coordinates[0], coordinates[1], days)
    if not weather_data:
        print(f"Could not fetch weather data for '{city}'. Please try again.")
        return None
    WEATHER_FETCHER.format_weather_data(weather_data, mode=2 if days != 1 else 1)

def list_cities():
    cities = WEATHER_FETCHER.list_cities()
    print(f"Available cities: {', '.join(cities)}")

def settings():
    with open("settings.json", "r") as json_file:
        data = json.load(json_file)
        data["Settings"]["Temperature_Measurement"] = input("Enter temperature measurement (C or F): ")

    with open("settings.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    WEATHER_FETCHER.update_settings(data["Settings"])

if __name__ == "__main__":
    main()          