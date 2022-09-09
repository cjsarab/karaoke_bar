import unittest
from src.room import Room
from src.karaoke_bar import KaraokeBar
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Joyzone", 6, "Pop", False)
        self.room2 = Room("Code Sheeran", 8, "Pop", True)
        self.room3 = Room("House of the 0 and 1", 5, "Blues and Soul", False)
        self.room4 = Room("Loop Reed", 8, "Rock", True)
        self.room5 = Room("The Integer of the Beast", 4, "Metal", False)
        self.room6 = Room("Johnny Crash", 6, "Country", False)

        self.song1 = Song("Boyzone", "No Matter What", 1998)
        self.song2 = Song("Ed Sheeran", "I See Fire", 2013)
        self.song3 = Song("The Animals", "The House of the Rising Sun", 1964)
        self.song4 = Song("Lou Reed", "Vicious", 1972)
        self.song5 = Song("Iron Maiden", "The Number of the Beast", 1982)
        self.song6 = Song("Johnny Cash", "A Boy Named Sue", 1969)

        self.rooms = []
        self.rooms.extend([self.room1, self.room2, self.room3, self.room4, self.room5, self.room6])

        self.songs = []
        self.songs.extend([self.song1, self.song2, self.song3, self.song4, self.song5, self.song6])

        self.karaoke_bar = KaraokeBar("Kode to Joy", 1000, self.songs, self.rooms)

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
