class package:
    #package constructor
    def __init__(self, package_id, address, city, state, zip, deadline, weight, notes, delivery_status, truck_id, address_id):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.delivery_status = delivery_status
        self.truck_id = truck_id
        self.address_id = address_id

    #getters
    def get_package_id(self):
        return self.package_id
    def get_address(self):
        return self.address
    def get_city(self):
        return self.city
    def get_state(self):
        return self.state
    def get_zip(self):
        return self.zip
    def get_deadline(self):
        return self.deadline
    def get_weight(self):
        return self.weight
    def get_notes(self):
        return self.notes
    def get_delivery_status(self):
        return self.delivery_status
    def get_truck_id(self):
        return self.truck_id
    def get_address_id(self):
        return self.address_id

    #setters
    def set_package_id(self, package_id):
        self.package_id = package_id
    def set_address(self, address):
        self.address = address
    def set_city(self, city):
        self.city = city
    def set_state(self, state):
        self.state = state
    def set_zip(self, zip):
        self.zip = zip
    def set_deadline(self, deadline):
        self.deadline = deadline
    def set_weight(self, weight):
        self.weight = weight
    def set_notes(self, notes):
        self.notes = notes
    def set_delivery_status(self, delivery_status):
        self.delivery_status = delivery_status
    def set_truck_id(self, truck_id):
        self.truck_id = truck_id
    def set_address_id(self, address_id):
        self.address_id = address_id