import unittest
import sys
import os
sys.path.append(os.getcwd()+"\\..\\app")
#sys.path.insert(0,'D:\DIGSI\src')
from ticket import Ticket
from parking_spot import ParkingSpot
from parking_lot import ParkingLot

class TestClassMethods(unittest.TestCase):

    def test_ticket_creation(self):
        x = Ticket().create("KA-01-HH-1234", 3, 34)
        self.assertEqual(x, (3, "KA-01-HH-1234", 34))
    def test_parkingspot_creation(self):
        pk = ParkingSpot(4,1)
        x = pk.get_val()
        self.assertEqual(x, (4,1))
    def test_parkinglot_creation(self):
        pk = ParkingLot(4)
        res_1 = pk.allocate_ticket("KA-01-HH-1234", 21)
        res_2 = pk.allocate_ticket("PB-01-HH-1234", 21)
        res_3 = pk.allocate_ticket("PB-01-TG-2341", 40)
        self.assertEqual(res_1, (0,"KA-01-HH-1234", 21))
        self.assertEqual(res_2, (1, "PB-01-HH-1234", 21))
        self.assertEqual(res_3, (2, "PB-01-TG-2341", 40))


if __name__ == '__main__':
    unittest.main()