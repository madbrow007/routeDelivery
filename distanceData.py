import packages
import csv


class DistanceData:
    def __init__(self, initial_capacity=0):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def print_distance_data(self):
        for i in range(len(self.table)):
            print(self.table[0][0])

    def load_distance_data(self):
        with open("Distance_Table.csv") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=",")

            for skip in range(4):
                next(csv_reader)

            # reading in and cleaning the data from csv
            for row in csv_reader:
                edited_distance_object = ('",'.join(row).replace("\n", "")).split(sep='",')

                if len(edited_distance_object) != 0:
                    self.table.append(edited_distance_object)
                    print(edited_distance_object)


d1 = DistanceData()
d1.load_distance_data()
print("___________________________________________")

d1.print_distance_data()

