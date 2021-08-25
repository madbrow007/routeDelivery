class PackageDataHashTable:
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])


ht1 = PackageDataHashTable(3)
print("ht1:", ht1.table)
