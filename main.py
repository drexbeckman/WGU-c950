#Drex Beckman 001082313

import distances_and_deliveries
import CSV_reader
import datetime
from package import package

#collect time and mileage data to display to user
truck1_mileage_stat, truck1_time_stat = distances_and_deliveries.deliver(CSV_reader.get_truck_1(), CSV_reader.get_truck1_start_time(), True)
truck2_mileage_stat, truck2_time_stat = distances_and_deliveries.deliver(CSV_reader.get_truck_2(), CSV_reader.get_truck2_start_time(), True)
truck3_mileage_stat, truck3_time_stat = distances_and_deliveries.deliver(CSV_reader.get_truck_1_second(), CSV_reader.get_truck1_second_start_time(), False)

#deliver the packages using greedy algorithm
distances_and_deliveries.deliver_packages()

#create instance of the hash table
hash_table = CSV_reader.get_hash_table()

#Create a dateTime object to use to compare user input times to delivery status of packages
date_string = "2021-1-1 "
format_string = "%Y-%m-%d %H:%M"
hash_format = "%Y-%m-%d %H:%M:%S"

user_in_string = ""

#Allow the user to enter a time, to get status of all packages, or see how far each truck travelled per trip
#O(n * m)
while user_in_string != "q":
    try:
        user_in = input("Enter a time to track packages, 'info' for distance and time information, or 'q' to quit: ")
        user_in_string = date_string + user_in
        user_date_time = datetime.datetime.strptime(user_in_string, format_string)

        i = 1
        while i < 41:
            curr_package = hash_table.search_item(i)
            status_string = curr_package.get_delivery_status()
            delivery_time_str = status_string[14:22]
            delivery_time_str = date_string + delivery_time_str
            delivery_time_date = datetime.datetime.strptime(delivery_time_str, hash_format)
            if curr_package.get_truck_id() == 1 and user_date_time.time() >= CSV_reader.get_truck1_start_time().time():
                if user_date_time.time() >= delivery_time_date.time():
                    print(f"Package ID: {curr_package.get_package_id()} | Address: {curr_package.get_address()} | Deadline: {curr_package.get_deadline()} | City: {curr_package.get_city()} | Zip: {curr_package.get_zip()} | Weight: {curr_package.get_weight()} | Status: {curr_package.get_delivery_status()}")
                else:
                    print(f"Package ID: {curr_package.get_package_id()} | Address: {curr_package.get_address()} | Deadline: {curr_package.get_deadline()} | City: {curr_package.get_city()} | Zip: {curr_package.get_zip()} | Weight: {curr_package.get_weight()} | Status: En-route")
            elif curr_package.get_truck_id() == 1 and user_date_time.time() < CSV_reader.get_truck1_start_time().time():
                print(f"Package ID: {curr_package.get_package_id()} | Address: {curr_package.get_address()} | Deadline: {curr_package.get_deadline()} | City: {curr_package.get_city()} | Zip: {curr_package.get_zip()} | Weight: {curr_package.get_weight()} | Status: At hub")
            elif curr_package.get_truck_id() == 2 and user_date_time.time() >= CSV_reader.get_truck2_start_time().time():
                if user_date_time.time() >= delivery_time_date.time():
                    print(f"Package ID: {curr_package.get_package_id()} | Address: {curr_package.get_address()} | Deadline: {curr_package.get_deadline()} | City: {curr_package.get_city()} | Zip: {curr_package.get_zip()} | Weight: {curr_package.get_weight()} | Status: {curr_package.get_delivery_status()}")
                else:
                    print(f"Package ID: {curr_package.get_package_id()} | Address: {curr_package.get_address()} | Deadline: {curr_package.get_deadline()} | City: {curr_package.get_city()} | Zip: {curr_package.get_zip()} | Weight: {curr_package.get_weight()} | Status: En-route")
            elif curr_package.get_truck_id() == 2 and user_date_time.time() < CSV_reader.get_truck2_start_time().time():
                print(f"Package ID: {curr_package.get_package_id()} | Address: {curr_package.get_address()} | Deadline: {curr_package.get_deadline()} | City: {curr_package.get_city()} | Zip: {curr_package.get_zip()} | Weight: {curr_package.get_weight()} | Status: At hub")
            elif curr_package.get_truck_id() == 3 and user_date_time.time() >= CSV_reader.get_truck1_second_start_time().time():
                if user_date_time.time() >= delivery_time_date.time():
                    print(f"Package ID: {curr_package.get_package_id()} | Address: {curr_package.get_address()} | Deadline: {curr_package.get_deadline()} | City: {curr_package.get_city()} | Zip: {curr_package.get_zip()} | Weight: {curr_package.get_weight()} | Status: {curr_package.get_delivery_status()}")
                else:
                    print(f"Package ID: {curr_package.get_package_id()} | Address: {curr_package.get_address()} | Deadline: {curr_package.get_deadline()} | City: {curr_package.get_city()} | Zip: {curr_package.get_zip()} | Weight: {curr_package.get_weight()} | Status: En-route")
            elif curr_package.get_truck_id() == 3 and user_date_time.time() < CSV_reader.get_truck1_second_start_time().time():
                print(f"Package ID: {curr_package.get_package_id()} | Address: {curr_package.get_address()} | Deadline: {curr_package.get_deadline()} | City: {curr_package.get_city()} | Zip: {curr_package.get_zip()} | Weight: {curr_package.get_weight()} | Status: At hub")

            i += 1

    except ValueError:
        if user_in == "q":
            break
        #Return distance and time data O(1)
        elif user_in == "info":
            print()
            print("########## Delivery Time and Distance Information ##########")
            print()
            print(f"Truck 1 start time: {CSV_reader.get_truck1_start_time().time()}")
            print(f"Truck 1 returned to hub: {truck1_time_stat.time()}")
            print(f"Truck 1 distance travelled: {truck1_mileage_stat:.2f}")
            print()
            print(f"Truck 2 start time: {CSV_reader.get_truck2_start_time().time()}")
            print(f"Truck 2 returned to hub: {truck2_time_stat.time()}")
            print(f"Truck 2 distance travelled: {truck2_mileage_stat - truck1_mileage_stat :.2f}")
            print()
            print(f"Truck 1 second trip start time: {CSV_reader.get_truck1_second_start_time().time()}")
            print(f"Truck 1 second trip end time: {truck3_time_stat.time()}")
            print(f"Truck 1 second trip distance travelled: {truck3_mileage_stat - truck2_mileage_stat:.2f}")
            print()
            print(f"Total distance travelled: {distances_and_deliveries.deliver_packages():.2f}")


        else:
            print("ValueError. Enter a valid 24hr time with colon separating hours and minutes (ex. 15:30)")
            
