import googlemaps
import folium

API_KEY = ""

input_location = input("可能な限り具体的に入力ください（入力例：日暮里駅）　：")
input_radius = input("半径何メートルで検索しますか？（入力例：100）　：")
input_keyword = input("キーワードを入力してください（入力例：とんかつ）　：")

"""
中心とする地点をgoogle map上から取得する。
"""
gm = googlemaps.Client(key = API_KEY)
geocode_result = gm.geocode(input_location)
loc = geocode_result[0]["geometry"]["location"]


center_location_list = []
center_location_list.append(loc["lat"])
center_location_list.append(loc["lng"])

"""
中心地点を基に地図を作成
"""

map = folium.Map(center_location_list,zoom_start=18)

"""
入力されたキーワード,半径から店の情報を取り出す。
place_resultsは辞書型
"""

place_results = gm.places_nearby(location = loc,
                                radius = input_radius,
                                keyword = input_keyword,
                                language = "ja",
                                )

"""
place_resultsから経度、緯度を取り出し、地図上にマッピングする。
"""

for results_dic in place_results["results"]:
    location_list = []
    location_list.append(results_dic["geometry"]["location"]["lat"])
    location_list.append(results_dic["geometry"]["location"]["lng"])

    if results_dic["rating"] >= 2.5 :
        folium.Marker(location=location_list,
                        popup=results_dic["name"] ).add_to(map)
    else:
        continue
"""
マップをwindowsのデスクトップにセーブ
"""
map.save(f"/mnt/c/Users/yuwan/Desktop/map_nearby_{input_location}.html")
