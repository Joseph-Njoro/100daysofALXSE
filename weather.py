mport tkineras tk
mport requets
lass WeatheApp
   def __int__(self,root):
       selfroot = roo
       selfroot.title("Weather App)
       selfroot.geometry("400x200")
       selfcity_label = tk.Label(root, text="Enter City:"
       selfcity_label.grid(row=0, column=0, padx=10, pady=10)
       selfcity_entry = tk.Entry(root
       selfcity_entry.grid(row=0, column=1, padx=10, pady=10)
       selfget_weather_button = tk.Button(root, text="Get Weather", commnd=self.get_weather)
       selfget_weather_button.grid(row=1, columnspan=2, padx=10, pady=10)
       selfweather_info_label = tk.Label(root, text=""
       selfweather_info_label.grid(row=2, columnspan=2, padx=10, pady=10)
   def get_eather(self)
       city= self.city_etry.get()
       api_ey = "YOUR_APIKEY"  # Replace with your OpenWeatherMap API key
       url  f"http://api.oenweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
       respnse = requests.gt(url)
       data= response.json()
       if dta["cod"] == 200
           eather_description  data["weather"][0]["description"].capitalize()
           emperature = data["min"]["temp"]
           umidity = data["main"["humidity"]
           ind_speed = data["wind]["speed"]
           ity_name = data["name"]
       weater_info = f"City: {city_name}\nWeather: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"
       selfweather_info_label.config(text=weather_info)
       else           self.eather_info_label.config(text="City not found")
f __name__ == __ain__":
   root = tk.Tk)   app = Weatherp(root)
   root.mainloop(