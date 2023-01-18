import csv
import json
from pprint import pprint

json_history_data = []

with open('historicdata.csv') as file:
    reader = csv.DictReader(file)
    for line in reader:
        json_history_data.append(line)
with open('from_csv_json_history_data.json', mode='w', encoding='UTF-8') as file:
    json.dump(json_history_data, file, ensure_ascii=False, indent=4)
for line in json_history_data:
    speed = line['Traffic In (speed)']
    speed2 = speed.split(" ")
    try:
        gig = speed2[0]
        mbit = speed2[1]
        gbitsmall = mbit[:1]
        print(f"Скорость соединения {gig}.{gbitsmall} Gbit/s")
    except IndexError:
        continue

#IndexError: list index out of range