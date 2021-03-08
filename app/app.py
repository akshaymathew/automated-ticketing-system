"""
@author : Akshay Mathew
"""
from ticket import Ticket
from parking_spot import ParkingSpot
from parking_lot import ParkingLot
class AutomatedTicketingSystem(object):
    def __init__(self,capacity):
        self.pk = ParkingLot(capacity)
        print ("Created parking of",str(capacity),"slots")
    def assign_ticket(self,registration_number,driver_age):
        response = self.pk.allocate_ticket(str(registration_number),driver_age)
        if response == (-1,-1,-1):
            print ("Cant assign")
        else:
            print ("Car with vehicle registration number ",response[1]," has been parked at slot number ",str(response[0]+1))
    def unassign_ticket(self,slot):
        dict = self.pk.get_ticket_list()
        #print (dict)
        #print (str(registration_number))
        #print (dict[registration_number])
        #age = dict[registration_number][1]
        slot_index = slot - 1
        reg_no, age = self.pk.return_ticket(slot_index)
        #print (response)

        if age == -1:
            print ("can't deallocate ticket as it doesnot exist")
        else:
            print ("Slot number",slot,"vacated, the car with vehicle registration number",reg_no,"left the space, the driver of the car was of age",str(age))
    def get_registration_numbers(self,age):
        dict = self.pk.get_ticket_list()
        result = []
        for key in dict:
            #print (key)
            if dict[key][1] == age:
                #print ("Yes")
                result.append(key)
        if len(result) == 0:
            print ("No slot numbers available")
            return []
        for i in range(len(result)-1):
            print (str(result[i]+1), end =",")
        print (str(result[len(result)-1]+1))
        return result
    def get_slot_number_by_plate_number(self,registration_number):
        dict = self.pk.get_ticket_list()
        if registration_number in dict:
            print (str(dict[registration_number][0]+1))
            return dict[registration_number][0]
        else:
            print ("No slot with such registration plate")
            return -1
    def get_slot_numbers_by_driver_age(self, age):
        result = []
        dict = self.pk.get_ticket_list()
        for key in dict:
            if dict[key][1] == age:
                result.append(dict[key][0])
        if len(result) == 0:
            print ("No slot numbers available")
            return []
        for i in range(len(result)-1):
            print (str(result[i]+1), end =",")
        print (str(result[len(result)-1]+1))
        return result

if __name__ == '__main__':
    ats = AutomatedTicketingSystem(6)
    ats.assign_ticket("KA-01-HH-1234", 21)
    ats.assign_ticket("PB-01-HH-1234", 21)
    ats.get_slot_numbers_by_driver_age(21)
    ats.assign_ticket("PB-01-TG-2341", 40)
    ats.get_slot_number_by_plate_number("PB-01-HH-1234")
    ats.unassign_ticket(2)
    #ats.leave(2)
    ats.assign_ticket("HR-29-TG-3098", 39)
    ats.get_registration_numbers(18)
    exit()
    # y_list = ats.get_ticket_list()
    # print(y_list)
    # for obj in y_list:
    #     print (obj.get_slot())
    #     print (obj.get_age())
    # print (pk.return_ticket("KA"))
    print("Final")
    print(ats.assign_ticket("KP", 22))
    #ats = AutomatedTicketingSystem(3)
    print (ats.get_registration_numbers(21))
    print(ats.get_slot_number_by_plate_number("IN"))
    print(ats.get_slot_numbers_by_driver_age(21))
    #app.run(host="0.0.0.0", port="5123")

