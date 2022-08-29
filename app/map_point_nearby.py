import googlemaps
import folium

API_KEY = ""

input_location = input("可能な限り具体的に入力ください（入力例：日暮里駅）　：")
input_radius = input("半径何メートルで検索しますか？（入力例：100）　：")
input_keyword = input("キーワードを入力してください（入力例：とんかつ）　：")

gm = googlemaps.Client(key = API_KEY)
geocode_result = gm.geocode(input_location)
loc = geocode_result[0]["geometry"]["location"]

place_results = gm.places_nearby(location = loc,
                                radius = input_radius,
                                keyword = input_keyword,
                                language = "ja",
                                )

center_location_list = []
center_location_list.append(loc["lat"])
center_location_list.append(loc["lng"])

map = folium.Map(center_location_list,zoom_start=18)

for results_dic in place_results["results"]:
    location_list = []
    location_list.append(results_dic["geometry"]["location"]["lat"])
    location_list.append(results_dic["geometry"]["location"]["lng"])

    if results_dic["rating"] >= 2.5 :
        folium.Marker(location=location_list,
                        popup=results_dic["name"] ).add_to(map)
    else:
        continue

map.save(f"/mnt/c/Users/yuwan/Desktop/map_nearby_{input_location}.html")




    

