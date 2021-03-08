"""
@author : Akshay Mathew
"""
from ticket import Ticket
from parking_spot import ParkingSpot
from parking_lot import ParkingLot
import os,sys
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
            if dict[key][1] == age:
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
    args = sys.argv
    file = args[1]
    #file = "D:\Task\\automated-ticketing-system\\input.txt"
    #REad from file
    if not os.path.exists(file):
        print("File does not exist")

    file_obj = open(file,"r")
    k =0
    #print (file_obj.readline())
    for x in file_obj:
        k = k+1
        #print (x)
        command = x.split(" ")
        #print (command)
        n = len(command)
        instruction = command[0]
        instruction = instruction.strip()
        if instruction == "Create_parking_lot":
            #print ("Initailise")
            if len(command)>1:
                capacity = int(command[1].strip())
                print (capacity)
                ats = AutomatedTicketingSystem(capacity)
            else:
                print ("Wrong command")
                break
        elif instruction == "Park":
            #print("park")
            if (len(command)>3):
                reg_number = command[1].strip()
                if (command[2].strip() == "driver_age"):
                    age =int(command[3])
                    ats.assign_ticket(reg_number, age)
                else:
                    print("Wrong command")
                    break
            else:
                print("Wrong command")
                break
        elif instruction == "Slot_numbers_for_driver_of_age":
            #print ("Slot by age")
            if (len(command) > 1):
                age = int(command[1].strip())
                ats.get_slot_numbers_by_driver_age(age)
            else:
                print ("wrong command")
                break
        elif instruction == "Slot_number_for_car_with_number":
            #print ("Slot by number")
            if (len(command) > 1):
                reg_no = command[1].strip()
                ats.get_slot_number_by_plate_number(reg_no)
            else:
                print ("Wrong commad")
                break

        elif instruction == "Leave":
            #print ("deallocate ticket")
            if (len(command)>1):
                slot = int(command[1].strip())
                ats.unassign_ticket(slot)
            else:
                print ("wrong command")
                break
        elif instruction == "Vehicle_registration_number_for_driver_of_age":
            #print ("vehicle number by age")
            if (len(command)>1):
                age = int(command[1].strip())
                ats.get_registration_numbers(age)
            else:
                print ("Wrong command")
                break
        else:
            print ("Wrong instruction")
            break
    exit()



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

