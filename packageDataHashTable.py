import packages


class PackageDataHashTable:
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def get_package_list(self):
        return self.table

    def insert_package(self, package):
        bucket = hash(package) % len(self.table)
        bucket_list = self.table[bucket]
        bucket_list.append(package)

    def find_package(self, package) -> packages.Packages:
        bucket = hash(package) % len(self.table)
        bucket_list = self.table[bucket]

        if package in bucket_list:
            return bucket_list[bucket_list.index(package)]
        else:
            return None


# test code / creating sample packages and hash table
p1 = packages.Packages(1, '195 W Oakland Ave', 'Salt Lake City', 'UT', 84115, '10:30 AM', 21)
p2 = packages.Packages(3, '233 Canyon Rd', 'Salt Lake City', 'UT', '84103', 'EOD', '2', 'Can only be on truck 2')
ht1 = PackageDataHashTable(3)

ht1.insert_package(p1)

# searching for package and error handling
try:
    print(ht1.find_package(p2).show_package())
except AttributeError:
    print("package does not exist, please try searching another")

