class Packages:
    packageID: int

    def __init__(self, package_id, address, city, state, zip_code, delivery_deadline, mass_kilo, special_notes="none"):
        self.packageID = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zip_code
        self.deliveryDeadline = delivery_deadline
        self.massKilo = mass_kilo
        if special_notes != "":
            self.specialNotes = special_notes
        else:
            self.specialNotes = "None"
        self.deliveryStatus = "AT HUB"

    def show_package(self):
        return (f"Package ID: {self.packageID}, Address: {self.address}, {self.city}, {self.state} {self.zipCode}"
                f", Delivery Deadline: {self.deliveryDeadline}, Weight: {self.massKilo}, "
                f"Delivery Status: {self.deliveryStatus}")
