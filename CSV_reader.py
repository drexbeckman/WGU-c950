import csv
import datetime

from hash_table import Hash_table
import datetime

from package import package

#open csv files
file = open("WGUPSPackageCSV.csv")
reader = csv.reader(file)
remove_header = next(reader)

address_file = open("addresses.csv")
address_reader = csv.reader(address_file)
remove_header_address = next(address_reader)

#create instance of Hash_table class
packages_hash = Hash_table()
#Create a list with address information
address_list = []
#Create lists for the trucks
truck1 = []
truck2 = []
truck1_second = []

#create truck start times
truck1_start_time = datetime.datetime(2021, 1, 1, 8, 0, 0)
truck2_start_time = datetime.datetime(2021, 1, 1, 9, 5, 0)
truck1_second_start_time = datetime.datetime(2021, 1, 1, 10, 40, 0)

#parse through the address CSV to get the address ids
#O(n)
for row in address_reader:
    address_list.append(row[2])

#parse all package data from each row in the csv and put it into a list of values for distances_hash
#O(n * m)
for row in reader:
    package_ID = int(row[0])
    address = row[1]
    city = row[2]
    state = row[3]
    zip = int(row[4])
    deadline = row[5]
    package_weight = int(row[6])
    special_instructions = row[7]
    delivery_status = "not delivered"
    truck = 4
    address_id = 99

    #fix package with incorrect address
    if "Wrong address listed" in special_instructions:
        address = "410 S State St"
        city = "Salt Lake City"
        zip = 84111

    i = 0
    while i < len(address_list):
        if address == address_list[i]:
            address_id = i
        elif address == "3575 W Valley Central Station bus Loop":
            address_id = 16
        i += 1

    #create package list
    #add time status
    package_data = package(package_ID, address, city, state, zip, deadline, package_weight, special_instructions, delivery_status, truck, address_id)
    #packages are sorted manually
    #truck1 will leave before 9 to take care of the one package deadline of 9AM and other time sensitive packages
    #truck2 will leave after 9:05 to take care of delayed-flight and special notes packages
    #truck3 will leave after 10:30 to take care of wrong address/remaining packages
    #O(1)
    #1 new [12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 26, 31, 33, 34, 39]
    #2 new [1, 2, 3, 4, 5, 6, 18, 25, 28, 29, 30, 32, 36, 37, 38, 40]
    #3 new[7, 8, 9, 10, 11, 24, 27, 35]
    if package_ID in [12, 13, 14, 15, 16, 17, 19, 20, 21, 30, 23, 26, 31, 33, 37, 39]:
        package_data.set_truck_id(1)
        truck1.append(package_data)
    elif package_ID in [1, 2, 3, 4, 5, 6, 18, 25, 28, 29, 22, 32, 36, 34, 38, 40]:
        package_data.set_truck_id(2)
        truck2.append(package_data)
    else:
        package_data.set_truck_id(3)
        truck1_second.append(package_data)

    packages_hash.add_item(package_ID, package_data)

#return the hash table containing package information O(1)
def get_hash_table():
    return packages_hash
#return list of truck1's packages O(1)
def get_truck_1():
    return truck1
#return list of truck2's packages O(1)
def get_truck_2():
    return truck2
#return list of truck3's packages O(1)
def get_truck_1_second():
    return truck1_second

#return leave time of truck1 O(1)
def get_truck1_start_time():
    return truck1_start_time
#return leave time of truck2 O(1)
def get_truck2_start_time():
    return truck2_start_time
#return leave time of truck3 O(1)
def get_truck1_second_start_time():
    return truck1_second_start_time

