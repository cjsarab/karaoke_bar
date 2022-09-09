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

        rooms = []
        rooms.extend([self.room1, self.room2, self.room3, self.room4, self.room5, self.room6])

        songs = []
        songs.extend([self.song1, self.song2, self.song3, self.song4, self.song5, self.song6])

        self.karaoke_bar = KaraokeBar("Kode to Joy", 1000, songs, rooms)

    def test_karaoke_bar_has_name(self):
        self.assertEqual("Kode to Joy", self.karaoke_bar.name) 

