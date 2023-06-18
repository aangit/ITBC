# Write a program that takes an input text (string) in the following format:

# REG_OZNAKA  BOJA    TIP_VOZILA
# NI-543-MM   siva    automobil
# LE-345-KM   plava    kamion
# BG-345-TT   bela    automobil
# KG-365-KG   plava    automobil
# SU-475-GM   bela    automobil
# KG-845-YB   crna    autobus
# NI-345-XD   bela    automobil
# UE-134-NF   crna    automobil
# AL-226-DF   bela    kamion

# (The data is listed in separate rows, and each row is separated by a tab. 
#  The first row (REGISTRATION_PLATE COLOR VEHICLE_TYPE) is part of the input text)

# Create an output in the following format:
# {
#     tip_vozila: {
#             "automobil": "66.67%",
#             "kamion": "22.22%",
#             "autobus": "11.11%"
#     },
#     gradovi: ["NI", "LE", "BG", "KG", "UE", "AL", "SU"],
#     boja_po_tipu: {
#         "automobil":{
#             "siva": 1,
#             "bela": 3,
#             "plava": 1,
#             "crna": 1,
#        },
#         "kamion":{
#             "bela": 1,
#             "plava": 1
#     },
#         "autobus":{
#             "crna": 1
#         }
#     },
# }

import pprint

raw_data = """REG_OZNAKA	BOJA	TIP_VOZILA
NI-543-MM	siva	automobil
LE-345-KM	plava	kamion
BG-345-TT	bela	automobil
KG-365-KG	plava	automobil
SU-475-GM	bela	automobil
KG-845-YB	crna	autobus
NI-345-XD	bela	automobil
UE-134-NF	crna	automobil
AL-226-DF	bela	kamion"""


raw_data_rows = raw_data.splitlines()
key_list = raw_data_rows[0].split("\t")



values_list = []
for row in raw_data_rows[1:]:
    values_list.append(row.split("\t"))


def create_vehicle_dict(key_list, value_list):
    vehicle = {}
    for i in range(len(key_list)):
        vehicle[key_list[i]] = value_list[i]
    return vehicle


def create_multiple_vehicles(key_list, values_list):
    multiple_vehicles = []
    for value_list in values_list:
        vehicle = create_vehicle_dict(key_list, value_list)
        multiple_vehicles.append(vehicle)
    return multiple_vehicles


vehicle_list = create_multiple_vehicles(key_list, values_list)


def find_vehicle_type(vehicle_list):
    vehicle_type_dict = {}
    for vehicle in vehicle_list:
        vehicle_type = vehicle["TIP_VOZILA"]  # automobil
        if vehicle_type not in vehicle_type_dict:
            vehicle_type_dict[vehicle_type] = 1
        else:
            vehicle_type_dict[vehicle_type] += 1
    vehicle_count = len(vehicle_list)
    for vehicle_type_key in vehicle_type_dict:
        vehicle_type_dict[vehicle_type_key] = round(
            vehicle_type_dict[vehicle_type_key] * 100 / vehicle_count, 2)
    return vehicle_type_dict




def find_cities(vehicle_list):
    cities = set()
    for vehicle in vehicle_list:
        reg = vehicle["REG_OZNAKA"]
        city = reg[:2]
        cities.add(city)

    return list(cities)


def color_by_type(vehicle_list):
    color_dict = {}
    for vehicle in vehicle_list:
        vehicle_type_key = vehicle["TIP_VOZILA"] 
        color_key = vehicle["BOJA"] 
        if vehicle_type_key not in color_dict:
            color_dict[vehicle_type_key] = {}
            vehicle_type_dict = color_dict[vehicle_type_key]
            vehicle_type_dict[color_key] = 1

        else:
            vehicle_type_dict = color_dict[vehicle_type_key]
            if color_key not in vehicle_type_dict:
                vehicle_type_dict[color_key] = 1
            else:
                vehicle_type_dict[color_key] += 1
    return color_dict



def generate_report(vehicle_list):
    final_report = {
        "tip_vozila": find_vehicle_type(vehicle_list),
        "gradovi": find_cities(vehicle_list),
        "boja_po_tipu": color_by_type(vehicle_list),
    }
    return final_report

pprint.pprint(generate_report(vehicle_list))