import unittest
from src.guest import Guest
from src.guest_group import GuestGroup
from src.karaoke_bar import KaraokeBar
from src.songs import Song
from src.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest(10, "Pop", "I See Fire")
        self.guest2 = Guest(10, "Rock", "Everlong")
        self.guest3 = Guest(50, "Blues and Soul", "House of the Rising Sun")
        self.guest4 = Guest(50, "Rock", "Vicious")
        self.guest5 = Guest(50, "Metal", "The Number of the Beast")
        self.guest6 = Guest(50, "Country", "A Boy Named Sue")
        self.guest7 = Guest(100, "Rock", "Ever Fallen in Love(With Someone You Shouldn't've)")
        self.guest8 = Guest(100, "Pop", "Umbrella")
        self.guest9 = Guest(50, "Metal", "Run to the Hills")
        self.guest10 = Guest(200, "Country", "Bolsarino")

        self.room1 = Room("Joyzone", 6, "Pop", False)
        self.room2 = Room("Code Sheeran", 8, "Pop", True)
        self.room3 = Room("House of the 0 and 1", 5, "Blues and Soul", False)
        self.room4 = Room("Loop Reed", 8, "Rock", True)
        self.room5 = Room("The Integer of the Beast", 4, "Metal", False)
        self.room6 = Room("Johnny Crash", 6, "Country", False)

        self.song1 = Song("Boyzone", "No Matter What", "Pop")
        self.song2 = Song("Ed Sheeran", "I See Fire", "Pop")
        self.song3 = Song("The Animals", "House of the Rising Sun", "Blues and Soul")
        self.song4 = Song("Lou Reed", "Vicious", "Rock")
        self.song5 = Song("Iron Maiden", "The Number of the Beast", "Metal")
        self.song6 = Song("Johnny Cash", "A Boy Named Sue", "Country")

        self.rooms = []
        self.rooms.extend([self.room1, self.room2, self.room3, self.room4, self.room5, self.room6])

        self.songs = []
        self.songs.extend([self.song1, self.song2, self.song3, self.song4, self.song5, self.song6])

        self.karaoke_bar = KaraokeBar("Kode to Joy", 1000, self.songs, self.rooms, 40)
        

    def test_guest_has_cash(self):
        self.assertEqual(200, self.guest10.cash)

    def test_guest_has_fav_genre(self):
        self.assertEqual("Country", self.guest10.fav_genre)

    def test_guest_has_fav_song(self):
        self.assertEqual("Bolsarino", self.guest10.fav_song)

    def test_guest_can_join_group(self):
        self.guest_group = GuestGroup(0)
        self.guest10.join_group(self.guest_group)
        self.assertEqual(1, self.guest_group.total_guests)

    def test_guest_enter_karaoke_has_money(self):
        self.guest10.enter_karaoke(self.karaoke_bar)
        self.assertEqual(160, self.guest10.cash)
        self.assertEqual(1040, self.karaoke_bar.till)

    def test_guest_enter_karaoke_not_money(self):
        self.guest1.enter_karaoke(self.karaoke_bar)
        self.assertEqual(10, self.guest1.cash)
        self.assertEqual(1000, self.karaoke_bar.till)

    # def test_guest_favourite_song_play(self):
    #     self.is_correct = 0
    #     self.guest31.play_fav_song(self.karaoke_bar.songs[3], self.is_correct)
    #     self.assertEqual(1, self.is_correct)
    