import googlemaps
# import pandas as pd
import openpyxl as excel
import requests 


"""
file_path = "mnt/c/Users/yuwan/Desktop/"
book = excel.load_workbook(file_path)
sheet = bool.active
print( sheet["A1"].value)
"""
BASE_URL = "https://maps.googleapis.com/maps/api/staticmap?"
API_KEY = "AIzaSyCROdomF3aLAbAxkxX9vjvEwOBhdgTvjO4"
CITY = "Tokyo"
ZOOM = 14
URL = BASE_URL + "center=" + CITY + "&zoom" + str(ZOOM) + "&size=500x500&key=" + API_KEY
response = requests.get(URL)
with open("/mnt/c/Users/yuwan/Desktop/tokyo.png", "wb") as file:
    file.write(response.content)
"""
gm = googlemaps.Client(key = API_KEY)
res = gm.geocode("日暮里駅")
print(res[0])
"""
