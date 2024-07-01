import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

def get_weather(city):
    api_key = "ca1c293c61b639a3844df5e1ad3d1e32"  
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None

    weather = res.json()
    icon = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']
    icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"
    
    return icon_url, temperature, description, city, country

def search():
    city = city_entry.get()
    result = get_weather(city)
    
    if result is None:
        return
    
    icon_url, temperature, description_text, city_name, country = result
    location.configure(text=f"{city_name}, {country}")
    
    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon_img = ImageTk.PhotoImage(image)
    
    icon.configure(image=icon_img)
    icon.image = icon_img
    
    temp.configure(text=f"Temperature: {temperature:.2f}°C")
    description.configure(text=f"Description: {description_text}")

root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")
root.geometry("400x400")

city_entry = ttkbootstrap.Entry(root, font=("Helvetica", 18))
city_entry.pack(pady=10)

search_button = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

location = tk.Label(root, font=("Helvetica", 25))
location.pack(pady=20)

icon = tk.Label(root)
icon.pack()

temp = tk.Label(root, font=("Helvetica", 20))
temp.pack()

description = tk.Label(root, font=("Helvetica", 20))
description.pack()

root.mainloop()