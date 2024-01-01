from tkinter import *
import requests
from datetime import datetime
import json


#tkinter ui window definiton 
root =Tk()
root.geometry("400x400") 
root.resizable(0,0) 
root.title("Weather App - AskPython.com")

city_value = StringVar()
 
 
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
 
 
city_value = StringVar()
 
def showWeather():
    api_key = #your API key pasted as a string
 
    #input city name from user
    city_name=city_value.get()
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
 
    # Fetch from url
    response = requests.get(weather_url)
 
    #make json object 
    weather_info = response.json()
 
    #clear text field after each op
    tfield.delete("1.0", "end")   
 
#Documentaion: If the cod is 200,data was successfully fetched
 
 
    if weather_info['cod'] == 200:
        kelvin = 273

        #storage
        temp = int(weather_info['main']['temp'] - kelvin)                                     
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
 
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n   '{city_name}' seems to be an invalid city name.\n   Please enter a valid city and try again"
 
 
 
    tfield.insert(INSERT, weather) #getting input
 
 
#ui
city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10) #to generate label heading
 
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold').pack()
 
 
Button(root, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
#to show output
 
weather_now = Label(root, text = "The Weather is:", font = 'arial 12 bold').pack(pady=10)
 
tfield = Text(root, width=46, height=10)
tfield.pack()
 
root.mainloop()