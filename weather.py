import tkinter as tk
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("400x200")

        self.city_label = tk.Label(root, text="Enter City:")
        self.city_label.grid(row=0, column=0, padx=10, pady=10)

        self.city_entry = tk.Entry(root)
        self.city_entry.grid(row=0, column=1, padx=10, pady=10)

        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.grid(row=1, columnspan=2, padx=10, pady=10)

        self.weather_info_label = tk.Label(root, text="")
        self.weather_info_label.grid(row=2, columnspan=2, padx=10, pady=10)

    def get_weather(self):
        city = self.city_entry.get()
        api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            weather_description  data["weather"][0]["description"].capitalize()
            temperature = data["min"]["temp"]
            humidity = data["main"["humidity"]
            wind_speed = data["wind]["speed"]
            city_name = data["name"]
        weather_info = f"City: {city_name}\nWeather: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"
        self.weather_info_label.config(text=weather_info)
        else
            self.weather_info_label.config(text="City not found")
if __name__ == __main__":
    root = tk.Tk)
    app = Weatherpp(root)
    root.mainloop(