import requests

class WeatherFetcher:
    CITIES = {"Johannesburg": (-26.2041, 28.0456), "Cape Town": (-33.9249, 18.4241), "Durban": (-29.8591, 31.0215), "Port Elizabeth": (-33.9682, 25.6154), "Pretoria": (-25.7479, 28.2293), "Bloemfontein": (-29.0852, 26.1596), "East London": (-33.0153, 27.9116), "Kimberley": (-28.7281, 24.7498), "Polokwane": (-23.8965, 29.4486), "Nelspruit": (-25.4658, 30.9853)    }

    def __init__(self,settings,timeout=10):
        self.settings = settings
        self.timeout = timeout

    def update_settings(self, new_settings):
        self.settings.update(new_settings)

    def list_cities(self):
        return list(self.CITIES.keys())

    def get_coordinates(self, city):
        if city not in self.CITIES:
            print(f"City '{city}' not found. Available cities: {', '.join(self.CITIES.keys())}")
            return None
        return self.CITIES.get(city, None)

    def fetch_weather(self, lat, lon,days=1):
        if days == 1:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        else:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,windspeed_10m_max,winddirection_10m_dominant&timezone=auto"
        try:
            response = requests.get(url,self.timeout)
            response.raise_for_status()
            data = response.json()
            return data['current_weather'] if days == 1 else data['daily']
        except requests.RequestException as e:
            print(f"Error fetching weather for {lat}, {lon}: {e}")
            return None
        except requests.Timeout:
            print(f"Request timed out for {lat}, {lon}")
            return None
        except requests.HTTPError as e:
            print(f"HTTP error for {lat}, {lon}: {e}")
            return None
        
    def format_weather_data(self, weather_data,mode=1):
        if not weather_data:
            return None
        if mode == 1:
            print(f"Temperature: {weather_data['temperature']}°{self.settings['Temperature_Measurement']} \nWindSpeed: {weather_data['windspeed']} m/s \nWind Direction: {weather_data['winddirection']}°\nWeather Code: {weather_data['weathercode']}")
        else:
            for i ,day in enumerate(weather_data['time']):
                print(f"Day {i+1} ({day}):)\n  Maximum Temperature: {weather_data['temperature_2m_max'][i]}°{self.settings['Temperature_Measurement']}\n  Minimum Temperature: {weather_data['temperature_2m_min'][i]}°{self.settings['Temperature_Measurement']}\n  Precipitation: {weather_data['precipitation_sum'][i]} mm\n  Maximum Wind Speed: {weather_data['windspeed_10m_max'][i]} m/s\n  Dominant Wind Direction: {weather_data['winddirection_10m_dominant'][i]}°\n")