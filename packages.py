class Packages:
    def __init__(self, package_id, address, city, state, zip_code, delivery_deadline, mass_kilo, special_notes="none"):
        self.packageID = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zip_code
        self.deliveryDeadline = delivery_deadline
        self.massKilo = mass_kilo
        self.specialNotes = special_notes
        self.deliveryStatus = "AT HUB"

    def show_package(self):
        return self.packageID, self.address, self.city, self.state, self.zipCode, \
               self.deliveryDeadline, self.massKilo, self.specialNotes, self.deliveryStatus




