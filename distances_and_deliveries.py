import csv
import CSV_reader
import datetime
from package import package

#open distance CSV
file = open("address_distances.csv")
reader = csv.reader(file)
distance_data = list(reader)

#open address CSV
address_file = open("addresses.csv")
read_address = csv.reader(address_file)
address_data = []
for data in read_address:
    if data[2] != "address":
        address_data.append(data[2])

#create time variables to import truck's start times from CSV_reader
truck1_time = CSV_reader.get_truck1_start_time()
truck2_time = CSV_reader.get_truck2_start_time()
truck3_time = CSV_reader.get_truck1_second_start_time()

#create total distance variable to add all truck mileages
total_distance_travelled = 0.0

#create hash table object
packages_hash = CSV_reader.get_hash_table()

#Method for getting the distance between two addresses
#O(1)
def distance_between(address_1, address_2):
    if distance_data[address_data.index(address_1)][address_data.index(address_2)] == "":
        return float(distance_data[address_data.index(address_2)][address_data.index(address_1)])
    return float(distance_data[address_data.index(address_1)][address_data.index(address_2)])

#Method for finding the shortest distance between an address and the addresses in a truck's package list
#O(n)
def shortest_distance(from_address, truck_list):
    min_distance = 9999
    curr_package_id = 0
    next_package_id = 0
    next_address = ""

    for package in truck_list:
        curr_package_id = package.get_package_id()
        package_address = package.get_address()
        distance = distance_between(from_address, package_address)

        if distance < min_distance:
            min_distance = distance
            next_package_id = curr_package_id
            next_address = package_address
    return min_distance, next_package_id, next_address

#deliver function using greedy algorithm to determine what package will be delivered next
#updates total_distance_travelled for all trucks, and also calculates the time and distance to return to hub
#Calls function shortest_distance which loops through truck_list inside loop going through len(truck_list)
#O(n * m)
def deliver(truck_list, truck_start_time, returns_to_hub):
    from_address = "4001 South 700 East"
    global total_distance_travelled
    i = 0

    while i != len(truck_list):
        min_dist, package_id, address = shortest_distance(from_address, truck_list)
        total_distance_travelled += min_dist
        truck_seconds = (min_dist / 18) * 60 * 60
        truck_time = datetime.timedelta(seconds=truck_seconds)
        truck_start_time += truck_time
        from_address = address
        curr_package = packages_hash.search_item(package_id)
        curr_package.set_delivery_status(f"delivered at: {truck_start_time.time()}")
        packages_hash.add_item(package_id, curr_package)
        truck_list.remove(curr_package)

    if returns_to_hub == True:
        min_dist = distance_between(from_address, "4001 South 700 East")
        total_distance_travelled += min_dist
        truck_seconds = (min_dist / 18) * 60 * 60
        truck_time = datetime.timedelta(seconds=truck_seconds)
        truck_start_time += truck_time
        #print(f"returned to hub at: {truck_start_time.time()}")
    return total_distance_travelled, truck_start_time

#method for running all of the truck deliver methods for main
#O(1)
def deliver_packages():
    deliver(CSV_reader.get_truck_1(), truck1_time, True)
    deliver(CSV_reader.get_truck_2(), truck2_time, True)
    deliver(CSV_reader.get_truck_1_second(), truck3_time, False)
    return total_distance_travelled

