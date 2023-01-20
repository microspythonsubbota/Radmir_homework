import csv
import json
from pprint import pprint
import xmltodict
import xml.dom.minidom
from xml.dom.minidom import parse, parseString
import xml.etree.ElementTree as ET


# json_history_data = []
#
# with open('historicdata.csv') as file:
#     reader = csv.DictReader(file)
#     for line in reader:
#         json_history_data.append(line)
# with open('from_csv_json_history_data.json', mode='w', encoding='UTF-8') as file:
#     json.dump(json_history_data, file, ensure_ascii=False, indent=4)
# for line in json_history_data:
#     speed = line['Traffic In (speed)']
#     speed2 = speed.split(" ")
#     try:
#         gig = speed2[0]
#         mbit = speed2[1]
#         gbitsmall = mbit[:1]
#         print(f"Скорость соединения {gig}.{gbitsmall} Gbit/s")
#     except IndexError:
#         continue
###IndexError: list index out of range

# Задание b)
# json_data = []
# with open("historicdata.xml", 'r') as myfile:
#     data_dict = xmltodict.parse(myfile.read())
#     json_data = json.dumps(data_dict)
#     pprint(json_data)

# with open("from_xml_json_history_data", 'w') as json_line:
#     json_line.write(json_data)

# def main():
# # use the parse() function to load and parse an XML file
#     doc = xml.dom.minidom.parse("historicdata.xml");
# # print out the document node and the name of the first child tag
#     print(doc.nodeName)
#     print(doc.firstChild.tagName)
#
# # get a list of XML tags from the document and print each one
#     expertise = doc.getElementsByTagName("value channel")
#     print(expertise)
#     for skill in expertise:
#         print(skill.getAttribute("Traffic Out (volume)"))
# if __name__ == "__main__":
#     main();

tree = ET.parse('historicdata.xml')
root = tree.getroot()
# all items data
dict1 = {}
list1 = []
for elem in root:
    for subelem in elem:
        a = subelem.attrib
        d = subelem.text
        list1.append(a)
        list1.append(d)
        dict1.update(a)
for line in list1:
    print(line)



