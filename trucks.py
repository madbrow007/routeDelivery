import packages


class Trucks:
    def __init__(self, truck_id):
        self.truckID = truck_id
        self.packageList = []

    def load_package(self, package: packages.Packages):
        package.deliveryStatus = f"On truck {self.truckID}"
        self.packageList.append(package)

        # todo add truck time
        print("loaded package on truck", self.truckID)

    def unload_package(self, package: packages.Packages):
        package.deliveryStatus = f"Delivered by truck {self.truckID}"
        self.packageList.remove(package)

        # todo add truck time
        print("unloaded package on truck", self.truckID)


# test code, loads 2 packages and prints list then unloads one and prints list again
p1 = packages.Packages(1, '195 W Oakland Ave', 'Salt Lake City', 'UT', 84115, '10:30 AM', 21)
p2 = packages.Packages(3, '233 Canyon Rd', 'Salt Lake City', 'UT', '84103', 'EOD', '2', 'Can only be on truck 2')
print(f"package 2 delivery status: {p2.deliveryStatus}")

truck1 = Trucks(1)

truck1.load_package(p1)
truck1.load_package(p2)

print(f"package 2 delivery status: {p2.deliveryStatus}")
print(truck1.packageList)

truck1.unload_package(p2)

print(f"package 2 delivery status: {p2.deliveryStatus}")
print(truck1.packageList)
