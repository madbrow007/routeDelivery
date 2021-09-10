import packages
import csv


class DistanceData:
    # initializes lists for distances and addresses and then calls the loading function for both
    def __init__(self, initial_capacity=0):
        self.distance_table = []
        self.address_list = []
        for i in range(initial_capacity):
            self.distance_table.append([])

        self.load_address_data()
        self.load_distance_data()

    def print_distance_data(self):
        for i in range(len(self.distance_table)):
            print(self.distance_table[0][0])

    def load_distance_data(self):
        with open("Distance_Table.csv") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=",")

            # reading in and cleaning the data from csv
            for row in csv_reader:
                edited_distance_object = ('",'.join(row).replace("\n", "")).split(sep='",')

                if len(edited_distance_object) != 0:
                    self.distance_table.append(edited_distance_object)

    def load_address_data(self):
        with open("address.csv") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=",")

            # reading in the data from csv
            for row in csv_reader:
                # address_list.append(row[2])
                self.address_list.append(row)

    def get_distance(self, address_id_1, address_id_2):

        distance = self.distance_table[address_id_1][address_id_2]

        if distance == '':
            distance = self.distance_table[address_id_2][address_id_1]

        return float(distance)

    def get_shortest_distance_package(self, current_address: str, package_list: list[packages.Packages]) \
            -> packages.Packages:
        current_address_id = self.get_address_id(current_address)
        closest_package_distance = None
        closest_package = None

        for package in package_list:
            current_distance = self.get_distance(current_address_id, self.get_address_id(package.address))

            if closest_package_distance is None or current_distance < closest_package_distance:
                closest_package_distance = current_distance
                closest_package = package

        return closest_package

    def get_address_id(self, package_address):
        address_id = None

        for address in self.address_list:
            if package_address == address[2]:
                address_id = address[0]
                break

        return int(address_id)

