import unittest
from src.karaoke_bar import KaraokeBar
from src.song import Song
from src. room import Room

class TestKaraokeBar(unittest.TestCase):

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

    def test_karaoke_bar_has_name(self):
        self.assertEqual("Kode to Joy", self.karaoke_bar.name) 

    def test_karaoke_bar_has_till_value(self):
        self.assertEqual(1000, self.karaoke_bar.till) 

    def test_karaoke_bar_has_songs(self):
        self.assertEqual(self.songs, self.karaoke_bar.songs)

    def test_karaoke_bar_has_rooms(self):
        self.assertEqual(self.rooms, self.karaoke_bar.rooms)

    def test_karaoke_bar_room_one_joyzone(self):
        self.assertEqual("Joyzone", self.karaoke_bar.rooms[0].name)

    def test_karaoke_bar_room_two_code_sheeran(self):
        self.assertEqual("Code Sheeran", self.karaoke_bar.rooms[1].name) 

    def test_karaoke_bar_room_three_house_0_1(self):
        self.assertEqual("House of the 0 and 1", self.karaoke_bar.rooms[2].name) 

    def test_karaoke_bar_room_four_loop_reed(self):
        self.assertEqual("Loop Reed", self.karaoke_bar.rooms[3].name) 

    def test_karaoke_bar_room_five_integer_of_the_beast(self):
        self.assertEqual("The Integer of the Beast", self.karaoke_bar.rooms[4].name) 

    def test_karaoke_bar_room_six_johnny_crash(self):
        self.assertEqual("Johnny Crash", self.karaoke_bar.rooms[5].name) 


