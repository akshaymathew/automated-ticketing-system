"""
@author : Akshay Mathew
"""
from heapq import heapify, heappush, heappop
from ticket import Ticket
from parking_spot import ParkingSpot

# Define all relevant properties of a parking lot
class ParkingLot(object):
    def __init__(self,capacity):
        self.capacity = capacity
        self.heap = []
        self.ticket_dict = {}
        heapify(self.heap)
        self.occupied = [0 for i in range(capacity)]
        for i in range(capacity):
            heappush(self.heap,ParkingSpot(i,0))
    def find_nearest_slot(self):
        return self.heap[0].slot,self.heap[0].occupied

    def allocate_ticket(self, registration_number,driver_age):
        slot, is_occupied = self.find_nearest_slot()
        if (is_occupied == 1):
            print ("No slot available")
            return (-1,-1,-1)
        self.ticket_dict[registration_number] = (slot, driver_age)
        self.occupied[slot] = 0
        self.heap[0].occupied = 1
        ticket = Ticket()
        obj = ticket.create(registration_number, slot, driver_age)
        #print (obj)
        self.ticket_dict[obj[1]] = (obj[0],obj[2])
        self.occupied[slot] = 1
        heapify(self.heap)
        return obj


    def return_ticket(self,slot):
        # Find slot and mark it as vacant
        for i in range(len(self.heap)):
            if (self.heap[i].slot == slot):
                self.heap[i].occupied = 0
                heapify(self.heap)
        # for i in range(0, len(self.heap)):
        #     print (self.heap[i].print_me())
        #     print()
        #find registration number for that slot
        reg_no = "-1"
        age = -1
        for key in self.ticket_dict:
            if self.ticket_dict[key][0] == slot:
                reg_no = key
                age = self.ticket_dict[key][1]
        self.ticket_dict.pop(reg_no)
        return reg_no,age
    def get_ticket_list(self):
        return self.ticket_dict