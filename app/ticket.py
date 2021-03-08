"""
@author : Akshay Mathew
"""


# Define all the relevant properties of the car, driver and parking lot that is needed for a ticket object in a parking lot
class Ticket(object):
    def __init__(self):
        self.registration_number = None
        self.slot_number = None
        self.driver_age = None

    def __registration_number(self, value):
        self.registration_number = value

    def __slot_number(self, value):
        self.slot_number = value

    def __driver_age(self, value):
        self.driver_age = value

    def create(self, registration_number, slot_number, driver_age):
        #ticket = Ticket()
        self.slot_number = slot_number
        self.registration_number = registration_number
        self.driver_age = driver_age
        #print (self.slot_number)
        return self.slot_number, self.registration_number, self.driver_age
    def get_slot(self):
        return self.slot_number
    def get_age(self):
        return self.driver_age
    def get_registration(self):
        return self.registration_number