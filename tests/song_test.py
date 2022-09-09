import unittest
from src.songs import Song

class TestSong(unittest.TestCase):

    def setUp(self):

        self.song1 = Song("Boyzone", "No Matter What", "Pop")
        self.song2 = Song("Ed Sheeran", "I See Fire", "Pop")
        self.song3 = Song("The Animals", "House of the Rising Sun", "Blues and Soul")
        self.song4 = Song("Lou Reed", "Vicious", "Rock")
        self.song5 = Song("Iron Maiden", "The Number of the Beast", "Metal")
        self.song6 = Song("Johnny Cash", "A Boy Named Sue", "Country")

    def test_song_one_has_name_no_matter_what(self):
        self.assertEqual("No Matter What", self.song1.title)

    def test_song_two_has_name_i_see_fire(self):
        self.assertEqual("I See Fire", self.song2.title)

    def test_song_three_has_name_house_of_rising_sun(self):
        self.assertEqual("House of the Rising Sun", self.song3.title)

    def test_song_four_has_name_vicious(self):
        self.assertEqual("Vicious", self.song4.title)

    def test_song_five_has_name_number_of_the_beast(self):
        self.assertEqual("The Number of the Beast", self.song5.title)

    def test_song_six_has_name_a_boy_named_sue(self):
        self.assertEqual("A Boy Named Sue", self.song6.title)