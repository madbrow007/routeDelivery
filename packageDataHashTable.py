import packages
import csv

class PackageDataHashTable:
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def get_package_list(self):
        return self.table

    # todo change key to packageid
    def insert_package(self, package):
        bucket = hash(package) % len(self.table)
        bucket_list = self.table[bucket]
        bucket_list.append(package)

    # todo change key to packageid
    def find_package(self, package) -> packages.Packages:
        bucket = hash(package) % len(self.table)
        bucket_list = self.table[bucket]

        if package in bucket_list:
            return bucket_list[bucket_list.index(package)]
        else:
            return None

    def load_package_data(self):
        with open("PackageList.csv") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=",")

            for skip in range(11):
                next(csv_reader)

            for row in csv_reader:
                edited_package_object = (",".join(row).replace(",,,,,", "")).split(sep=",")

                p1 = packages.Packages(edited_package_object[0], edited_package_object[1], edited_package_object[2],
                                       edited_package_object[3], edited_package_object[4], edited_package_object[5],
                                       edited_package_object[6], edited_package_object[7])
                self.insert_package(p1)


# # test code / creating sample packages and hash table
# p1 = packages.Packages(1, '195 W Oakland Ave', 'Salt Lake City', 'UT', 84115, '10:30 AM', 21)
# p2 = packages.Packages(3, '233 Canyon Rd', 'Salt Lake City', 'UT', '84103', 'EOD', '2', 'Can only be on truck 2')
# ht1 = PackageDataHashTable(3)
#
# ht1.insert_package(p1)
#
# # searching for package and error handling
# try:
#     print(ht1.find_package(p2).show_package())
# except AttributeError:
#     print("package does not exist, please try searching another")

