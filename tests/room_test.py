import unittest
from src.room import Room
from src.guest_group import GuestGroup

class TestRoom(unittest.TestCase):

    def setUp(self):

        self.room1 = Room("Joyzone", 6, "Pop", False)
        self.room2 = Room("Code Sheeran", 8, "Pop", True)
        self.room3 = Room("House of the 0 and 1", 5, "Blues and Soul", False)
        self.room4 = Room("Loop Reed", 8, "Rock", True)
        self.room5 = Room("The Integer of the Beast", 4, "Metal", False)
        self.room6 = Room("Johnny Crash", 6, "Country", False)

        self.guest_group_too_big = GuestGroup(10)
        self.guest_group_ok = GuestGroup(4)

    def test_room_one_has_name_joyzone(self):
        self.assertEqual("Joyzone", self.room1.name)

    def test_room_two_has_name_code_sheeran(self):
        self.assertEqual("Code Sheeran", self.room2.name)

    def test_room_three_has_name_house_of_0_and_1(self):
        self.assertEqual("House of the 0 and 1", self.room3.name)

    def test_room_four_has_name_loop_reed(self):
        self.assertEqual("Loop Reed", self.room4.name)

    def test_room_five_has_name_integer_of_the_beast(self):
        self.assertEqual("The Integer of the Beast", self.room5.name)

    def test_room_six_has_name_johnny_crash(self):
        self.assertEqual("Johnny Crash", self.room6.name)

    def test_room_accepts_group(self):
        self.guest_group_too_big.enter_room(self.room1.capacity)
        self.assertEqual(False, )
