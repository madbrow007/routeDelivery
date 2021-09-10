from datetime import datetime, timedelta
import packages
import distanceData


class Trucks:
    def __init__(self, truck_id):
        self.truckID = truck_id
        self.truckPackageList: list[packages.Packages] = []
        self.fullyLoaded = False
        self.distances = distanceData.DistanceData

    def is_fully_loaded(self):
        if len(self.truckPackageList) == 16:
            self.fullyLoaded = True
        else:
            self.fullyLoaded = False
        return self.fullyLoaded

    def load_a_package(self, package: packages.Packages):
        package.deliveryStatus = "On Truck"
        self.truckPackageList.append(package)

    # pickup packages from hub based on constraints and distances
    def pickup_packages(self, package_list: list[packages.Packages], current_time: timedelta):
        last_loaded: packages.Packages

        hub = "4001 S 700 E"
        special_notes_package_list: list[packages.Packages] = []
        timed_package_list: list[packages.Packages] = []

        # searching for packages that need to be grouped together
        for package in package_list:
            if int(package.packageID) in (13, 14, 15, 16, 19, 20):
                special_notes_package_list.append(package)

        # loading special note 'group together' packages by distance
        while len(special_notes_package_list) != 0:
            self.load_a_package(self.distances().get_shortest_distance_package(hub, special_notes_package_list))
            last_loaded = self.distances().get_shortest_distance_package(hub, special_notes_package_list)
            special_notes_package_list.remove(last_loaded)
            package_list.remove(last_loaded)

        # withholds packages that are delayed and wrong until they arrived or are fixed
        if current_time < timedelta(hours=int(9), minutes=int(5)):
            for package in package_list:
                if package.specialNotes[0] in ("D", "W"):
                    package_list.remove(package)

        # searches for packages based on time priority
        for package in package_list:
            if package.deliveryDeadline != "EOD":
                timed_package_list.append(package)

        # loading time priority packages
        while len(timed_package_list) != 0:
            self.load_a_package(self.distances().get_shortest_distance_package(hub, timed_package_list))
            last_loaded = self.distances().get_shortest_distance_package(hub, timed_package_list)
            timed_package_list.remove(last_loaded)
            package_list.remove(last_loaded)

        # if at the hub, loads the package closest to the hub
        if len(self.truckPackageList) == 0:

            self.load_a_package(self.distances().get_shortest_distance_package(hub, package_list))
            last_loaded = self.distances().get_shortest_distance_package(hub, package_list)
            package_list.remove(last_loaded)

        else:
            last_loaded = self.truckPackageList[len(self.truckPackageList) - 1]

        # while truck is not full, loads packages based on distance
        while package_list and (not self.is_fully_loaded()):
            self.load_a_package(self.distances().get_shortest_distance_package(last_loaded.address, package_list))
            last_loaded = self.distances().get_shortest_distance_package(last_loaded.address, package_list)
            package_list.remove(last_loaded)

        print(f"loaded packages on truck {self.truckID} at {current_time}")
        print()

    # deliver packages based on constraints, distances and time
    def deliver_packages(self, current_time: timedelta):
        last_unloaded: packages.Packages or None = None
        previous_address = packages.Packages
        total_mileage = 0
        current_mileage = 0
        hub = "4001 S 700 E"
        previous_address.address = hub

        package_list_copy = self.truckPackageList[:]

        if timedelta(hours=int(9), minutes=int(50)) < current_time < timedelta(hours=int(10), minutes=int(30)):
            for package in package_list_copy:

                if package.deliveryDeadline != "EOD":
                    last_unloaded = package
                    current_mileage = self.distances().get_distance(
                        self.distances().get_address_id(previous_address.address),
                        self.distances().get_address_id(package.address))

                    current_time = current_time + timedelta(hours=current_mileage / 18)
                    total_mileage += current_mileage
                    print("Current truck delivery mileage: ", round(total_mileage, 2))

                    self.unload_package(last_unloaded, current_time)

                    previous_address = last_unloaded

        else:
            # delivers package closest to hub
            last_unloaded = self.distances().get_shortest_distance_package(hub, self.truckPackageList)
            current_mileage += self.distances().get_distance(self.distances().get_address_id(hub),
                                                             self.distances().get_address_id(last_unloaded.address))

            current_time = current_time + timedelta(hours=current_mileage / 18)
            total_mileage = current_mileage

            print("Current truck delivery mileage: ", current_mileage)
            print("Current truck delivery time: ", current_time)

            self.unload_package(self.distances().get_shortest_distance_package(hub, self.truckPackageList),
                                current_time)
            previous_address = last_unloaded

        while self.truckPackageList:
            last_unloaded = self.distances().get_shortest_distance_package(last_unloaded.address, self.truckPackageList)
            current_mileage = self.distances().get_distance(self.distances().get_address_id(previous_address.address),
                                                            self.distances().get_address_id(last_unloaded.address))

            current_time = current_time + timedelta(hours=current_mileage / 18)
            total_mileage += current_mileage
            print("Current distance for this delivery route:", round(total_mileage, 2), "miles")

            self.unload_package(last_unloaded, current_time)

            previous_address = last_unloaded

        # distance from last address to hub
        current_mileage = self.distances().get_distance(self.distances().get_address_id(previous_address.address),
                                                        self.distances().get_address_id(hub))

        current_time = current_time + timedelta(hours=current_mileage / 18)
        total_mileage += current_mileage

        return total_mileage, current_time

    def unload_package(self, package: packages.Packages, current_time: timedelta):
        d = datetime.strptime(str(current_time), "%H:%M:%S")
        package.deliveryStatus = f"Delivered by truck {self.truckID} at {d.strftime('%I:%M %p')}"

        self.truckPackageList.remove(package)

        print(f"Delivered package {package.packageID} from truck {self.truckID} at {d.strftime('%I:%M %p')}."
              f" Package Delivery Deadline was: {package.deliveryDeadline}")

# # test code, loads 2 packages and prints list then unloads one and prints list again
# p1 = packages.Packages(1, '195 W Oakland Ave', 'Salt Lake City', 'UT', 84115, '10:30 AM', 21)
# p2 = packages.Packages(2, '233 Canyon Rd', 'Salt Lake City', 'UT', '84103', 'EOD', '2', 'Can only be on truck 2')
# p3 = packages.Packages(3, '380 W 2880 S', 'Salt Lake City', 'UT', 84115, 'EOD', 4)
# p4 = packages.Packages(4, '410 S State St', 'Salt Lake City', 'UT', 84115, 'EOD', 4)
# #     print(f"package 2 delivery status: {p2.deliveryStatus}")
# #
# truck1 = Trucks(1)
#
# pl = [p1, p2, p3, p4]
#
# truck1.pickup_packages(pl)
