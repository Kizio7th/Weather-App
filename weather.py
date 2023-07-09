from cgitb import text
from tkinter import *
from tkinter import messagebox
from turtle import color
import requests
from configparser import *
from urllib.request import *
from PIL import Image, ImageTk
GUI = Tk()
GUI.geometry("650x500") 
GUI.resizable(0,0) 
GUI.title("Weather App")
GUI.iconbitmap('icon/weather.ico')
GUI.option_add("*Font", "Segoe 14")
window =  Canvas(GUI,width=650,height=500,bg='black')

def get_key():
    config = ConfigParser()
    config.read("key.ini")
    return config["openweather"]["api_key"]
city_value = StringVar()
def convert_date(date,weekdays,i):
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec' ]
    day = ['Mon','Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    weekdays = weekdays[:3]
    weekdays_index = day.index(weekdays)
    if(weekdays_index + i) > 6:
        i -= 7
    return day[weekdays_index + i] + ', ' + month[int(date[5:7]) -  1] + ' '  + date[8:10]
def showWeather():
    api_key = get_key()
    city_name=city_value.get()
    weather_url = 'http://api.openweathermap.org/data/2.5/forecast?q=' + city_name + '&appid='+api_key
    response1 = requests.get(weather_url)
    weather_info = response1.json()
    ##########################################################################
    info = []
    if weather_info['cod'] == '200':
        lon_value = str(weather_info['city']['coord']['lon'])
        lat_value = str(weather_info['city']['coord']['lat'])
        time_url = 'https://timeapi.io/api/Time/current/coordinate?latitude=' + lat_value + '&longitude=' + lon_value
        response2 = requests.get(time_url)
        time_info = response2.json()
        color = [2,4,5,6,7,8,9,10,12,13,14,15,17,18,19,20,22,23,24,25,27,28,29]
        if int(time_info['time'][:2]) > 12:
            day_night = 'n'
            for i in color:
                window.itemconfig(str(i), fill = 'white')
        else: 
            day_night = 'd'
            for i in color:
                window.itemconfig(str(i), fill = 'black')
        
        for i in weather_info['list']:
            if(i['dt_txt'][11::] == '12:00:00'):
                info.append(i)
        kelvin = 273
        # #today
        image = Image.open('background/' + info[0]['weather'][0]['icon'][:2] + day_night + '.png')
        image = image.resize((650,500), Image.ANTIALIAS)
        bg = ImageTk.PhotoImage(image)
        window.itemconfig(today_background, image = bg)
        window.itemconfig(today_temp,text = str(int(info[0]['main']['temp']) - kelvin) + '°c', font  = ('Segoe Bold', 70))
        photo0 = PhotoImage(file = 'icon/' + info[0]['weather'][0]['icon'][:2] + day_night + '.png')
        window.itemconfig(today_icon, image = photo0)
        window.itemconfig(today_description,text = info[0]['weather'][0]['description'].capitalize(), font = ('Segoe Bold', 24))
        window.itemconfig(today_day,text = convert_date(str(info[0]['dt_txt']),str(time_info['dayOfWeek']),0), font = ('Segoe Bold', 13))
        window.itemconfig(today_feels_like,text = 'Feels Like ' + str(int(info[0]['main']['feels_like']) - kelvin) + '°C', font = ('Segoe Bold', 11))
        window.itemconfig(today_humidity, text = "Humidity " + str(info[0]['main']['humidity']) + '%', font = ('Segoe Bold', 11))
        window.itemconfig(today_wind,text = 'Wind ' + str(info[0]['wind']['speed']) + 'm/s', font = ('Segoe Bold', 11))
        window.itemconfig(today_clouds,text = "Clouds " + str(info[0]['clouds']['all'])+ '%', font = ('Segoe Bold', 11))
        # #f1
        window.itemconfig(f1_day, text = convert_date(str(info[1]['dt_txt']),str(time_info['dayOfWeek']),1), font = ('Segoe Bold', 12))
        image = Image.open('icon/' + info[1]['weather'][0]['icon'][:2] + 'd.png')
        image = image.resize((50,50), Image.ANTIALIAS)
        photo1 = ImageTk.PhotoImage(image)
        window.itemconfig(f1_icon, image = photo1)
        window.itemconfig(f1_temp, text = str(int(info[1]['main']['temp']) - kelvin) + '°', font = ('Segoe Bold', 18))
        window.itemconfig(f1_feels_like, text = str(int(info[1]['main']['feels_like']) - kelvin) + '°', font = ('Segoe Bold', 11))
        window.itemconfig(f1_description, text = info[1]['weather'][0]['description'].capitalize(), font = ('Segoe Bold', 11))
        # #f2
        window.itemconfig(f2_day, text = convert_date(str(info[2]['dt_txt']),str(time_info['dayOfWeek']),2), font = ('Segoe Bold', 12))
        image = Image.open('icon/' + info[2]['weather'][0]['icon'][:2] + 'd.png')
        image = image.resize((50,50), Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(image)
        window.itemconfig(f2_icon, image = photo2)
        window.itemconfig(f2_temp, text = str(int(info[2]['main']['temp']) - kelvin) + '°', font = ('Segoe Bold', 18))
        window.itemconfig(f2_feels_like, text = str(int(info[2]['main']['feels_like']) - kelvin) + '°', font = ('Segoe Bold', 11))
        window.itemconfig(f2_description, text = info[2]['weather'][0]['description'].capitalize(), font = ('Segoe Bold', 11))
        # # #f3
        window.itemconfig(f3_day, text = convert_date(str(info[3]['dt_txt']),str(time_info['dayOfWeek']),3), font = ('Segoe Bold', 12))
        image = Image.open('icon/' + info[3]['weather'][0]['icon'][:2] + 'd.png')
        image = image.resize((50,50), Image.ANTIALIAS)
        photo3 = ImageTk.PhotoImage(image)
        window.itemconfig(f3_icon, image = photo3)
        window.itemconfig(f3_temp, text = str(int(info[3]['main']['temp']) - kelvin) + '°', font = ('Segoe Bold', 18))
        window.itemconfig(f3_feels_like, text = str(int(info[3]['main']['feels_like']) - kelvin) + '°', font = ('Segoe Bold', 11))
        window.itemconfig(f3_description, text = info[3]['weather'][0]['description'].capitalize(), font = ('Segoe Bold', 11))
        # # #f4
        window.itemconfig(f4_day, text = convert_date(str(info[4]['dt_txt']),str(time_info['dayOfWeek']),4), font = ('Segoe Bold', 12))
        image = Image.open('icon/' + info[4]['weather'][0]['icon'][:2] + 'd.png')
        image = image.resize((50,50), Image.ANTIALIAS)
        photo4 = ImageTk.PhotoImage(image)
        window.itemconfig(f4_icon, image = photo4)
        window.itemconfig(f4_temp, text = str(int(info[4]['main']['temp']) - kelvin) + '°', font = ('Segoe Bold', 18))
        window.itemconfig(f4_feels_like, text = str(int(info[4]['main']['feels_like']) - kelvin) + '°', font = ('Segoe Bold', 11))
        window.itemconfig(f4_description, text = info[4]['weather'][0]['description'].capitalize(), font = ('Segoe Bold', 11))

        window.imgref = [bg,photo0,photo1,photo2,photo3,photo4]
    else :
        messagebox.showwarning("Notification","No citys match your search")
        
   
#Interface
def handle_focus_in(_):
    input_entry.delete(0, END)
    input_entry.config(fg='black')

def handle_focus_out(_):
    input_entry.delete(0, END)
    input_entry.config(fg='grey')
    input_entry.insert(0, "Enter city name")

def handle_enter(txt):
    showWeather()
    handle_focus_out('')
input_entry = Entry(GUI, width=30, fg='grey', textvariable = city_value)
def show(event):
    showWeather()  
input_entry.bind('<Return>', show)
input_entry.bind("<FocusOut>", handle_focus_out)
input_entry.bind("<FocusIn>", handle_focus_in)
input_entry.pack(side = TOP,pady=10)
input_entry.insert(0, "Enter city name")


# ###########################################################
# ###########################################################
#window
image = Image.open('background/background.png')
image = image.resize((650,500), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(image)
today_background = window.create_image(325,250., image = bg)
today_temp = window.create_text(370, 100)
today_icon = window.create_image(220, 100 )
today_description = window.create_text(310, 165)
today_day = window.create_text(300, 220)
today_feels_like = window.create_text(220, 250)
today_humidity = window.create_text(370, 250)
today_wind = window.create_text(220, 280)
today_clouds = window.create_text(370, 280)

#window
f1_day = window.create_text(40,360, anchor = 'w')
f1_icon = window.create_image(30, 390, anchor = 'w' )
f1_temp = window.create_text(40,425, anchor = 'w')
f1_feels_like = window.create_text(80,427,anchor = 'w')
f1_description = window.create_text(40,460, anchor = 'w')

# #window
f2_day = window.create_text(190,360, anchor = 'w')
f2_icon = window.create_image(180, 390, anchor = 'w' )
f2_temp = window.create_text(190,425, anchor = 'w')
f2_feels_like = window.create_text(230,427,anchor = 'w')
f2_description = window.create_text(190,460, anchor = 'w')

# #window
f3_day = window.create_text(340,360, anchor = 'w')
f3_icon = window.create_image(330, 390, anchor = 'w' )
f3_temp = window.create_text(340,425, anchor = 'w')
f3_feels_like = window.create_text(380,427,anchor = 'w')
f3_description = window.create_text(340,460, anchor = 'w')

# #window
f4_day = window.create_text(490,360, anchor = 'w')
f4_icon = window.create_image(480, 390, anchor = 'w' )
f4_temp = window.create_text(490,425, anchor = 'w')
f4_feels_like = window.create_text(530,427,anchor = 'w')
f4_description = window.create_text(490,460, anchor = 'w')







window.place(x=0,y=0)
GUI.mainloop()