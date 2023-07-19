import csv
import json
import urllib.request as request
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)
    # print(data)
#attractio-------------
attraction_list=data["result"]["results"]
# print (attraction_list)
with open("attraction.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    for attraction in attraction_list:
        name = attraction["stitle"]
        address = attraction.get("address")
        regions = ""

        for area in ["中正區", "萬華區", "中山區", "大同區", "大安區", "松山區", "信義區", "士林區", "文山區", "北投區", "內湖區", "南港區"]:
            if area in address:
                regions= area
        
        longitude = attraction["longitude"]
        latitude = attraction["latitude"]
        images = attraction["file"].split("https:")[1:] 
        image_url = "https:" + images[0]

        writer.writerow([name, regions,longitude,latitude,image_url])
        

#MRT------------------

mrt_dict = {}
for attraction in data["result"]["results"]:
    mrt = attraction.get("MRT")
    if mrt not in mrt_dict:
        mrt_dict[mrt] = []
    mrt_dict[mrt].append(attraction["stitle"])


with open("mrt.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)

    for mrt_station, attractions in mrt_dict.items():
        print(attractions)
        if mrt_station :
            writer.writerow([mrt_station] + attractions)
        else:
            writer.writerow(attractions)