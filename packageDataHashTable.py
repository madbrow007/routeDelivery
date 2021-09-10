
import packages
import csv
import re


class PackageDataHashTable:

    table: list[list[packages.Packages]]

    # initializes hashtable list and loads package data from csv
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])
        self.load_package_data()

    # inserts package into hashtable
    def insert_package(self, package: packages.Packages):
        bucket = hash(package.packageID) % len(self.table)
        bucket_list = self.table[bucket]
        bucket_list.append(package)

    # finds package by id
    def find_package(self, package_id):
        bucket = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket]
        found_package = "Package not found"

        for package in bucket_list:

            if package_id == package.packageID:
                found_package = package
                break

        return found_package

    # returns a list of all packages
    def get_package_list(self):
        package_list: list[packages.Packages] = []
        curr_package = None
        i = 1
        try:
            while curr_package != "Package not found":
                curr_package = self.find_package(i)
                package_list.append(curr_package)
                i += 1
            package_list.remove(curr_package)
        except AttributeError:
            print("package list retrieved ")
        return package_list

    # returns a list of all undelivered packages
    def get_undelivered_package_list(self):
        all_packages: list[packages.Packages] = self.get_package_list()
        undelivered_packages: list[packages.Packages] = []

        for package in all_packages:
            if package.deliveryStatus == "AT HUB":
                undelivered_packages.append(package)
        return undelivered_packages

    # reads package data in from csv file
    def load_package_data(self):
        with open("PackageList.csv") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=",")

            for skip in range(8):
                next(csv_reader)

            for row in csv_reader:
                edited_package_object = (",".join(row).replace(",,,,,", ""))
                edited_package_object = re.split(",(?!\\s)", edited_package_object)

                a_package = packages.Packages(int(edited_package_object[0]), edited_package_object[1],
                                              edited_package_object[2], edited_package_object[3],
                                              edited_package_object[4],
                                              edited_package_object[5], edited_package_object[6],
                                              edited_package_object[7])
                self.insert_package(a_package)
