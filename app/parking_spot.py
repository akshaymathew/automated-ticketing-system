"""
@author : Akshay Mathew
"""

# class definition
class ParkingSpot:

    # constructor
    def __init__(self, slot, occupied):
        self.slot = slot
        self.occupied = occupied

        # function for customized printing

    def print_me(self):
        print("Slot :", self.slot)
        print("Presence :", self.occupied)

        # override the comparison operator

    def __lt__(self, nxt):

        if (self.occupied == 0 and nxt.occupied == 0):
            return self.slot < nxt.slot
        elif (self.occupied == 0 and nxt.occupied == 1):
            return 1
        elif (self.occupied == 1 and nxt.occupied == 0):
            return 0
        else:
            return -1
    def get_val(self):
        return self.slot,self.occupied
    def set_occupied(self):
        self.occupied = 1
    def set_free(self):
        self.occupied = 0