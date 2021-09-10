# Madison Bryan #001386110
from datetime import datetime, timedelta
import trucks
import packageDataHashTable


def main():
    truck_2 = trucks.Trucks(2)
    package_hash_table = packageDataHashTable.PackageDataHashTable()
    undelivered_packages = package_hash_table.get_undelivered_package_list()
    total_mileage = 0
    initial_time = timedelta(hours=int(8), minutes=int(0))
    current_time = initial_time
    selected_package_id = None

    # while there are still undelivered_packages, the truck will pick up and deliver packages
    while undelivered_packages:

        undelivered_packages = package_hash_table.get_undelivered_package_list()

        truck_2.pickup_packages(undelivered_packages, current_time)

        mileage_and_time = truck_2.deliver_packages(current_time)
        current_time = mileage_and_time[1]
        current_time_format = datetime.strptime(str(current_time), "%H:%M:%S")

        total_mileage += mileage_and_time[0]

        print()
        print("Truck returned to hub at ", current_time_format.strftime('%I:%M %p'))
        print("Total mileage after truck delivery: ", round(total_mileage, 2))

    print("___________________________________________________________________")

    for num in range(5):
        print()

    print("Welcome! To view package delivery status and information, "
          "scroll up to view all or type in a specific command.")

    next_button = None

    while next_button != "x":
        next_button = (input("To quit the program, type 'x'. To search for a package, type 'f'."
                             " To view total mileage, type 'm'. To check packages by time, type 't': "))
        if next_button == "x":
            exit()
        elif next_button == "f":
            try:
                selected_package_id = int(input("Package ID: "))

                print(package_hash_table.find_package(selected_package_id).show_package())
                print()
            except AttributeError:
                print("Package does not exist, try again!")
        elif next_button == "m":
            print("Total mileage after truck deliveries: ", round(total_mileage, 2))
            print()
        elif next_button == "t":
            print("Type a time after 08:00:00 (using 24 hour time)")
            hour = int(input("Type an hour first, i.e., 1, 4, 14, 16, etc.: "))
            minute = int(input("Now type minutes, i.e., 00, 30, etc.: "))
            for package in package_hash_table.get_package_list():
                time_str = package.deliveryStatus.split(' ')[5].split(':')
                delivery_time = timedelta(hours=int(time_str[0]), minutes=int(time_str[1]))
                if delivery_time <= timedelta(hours=int(hour), minutes=int(minute)):
                    print(package.show_package())
        else:
            print("Try typing in a different command!")
            print()


if __name__ == '__main__':
    main()
