import unittest
from src.song import Song
from data import songs

class TestSong(unittest.TestCase):

    def setUp(self):

        self.song1 = songs.all_songs["Boyzone"][1]
        self.song2 = songs.all_songs["Ed Sheeran"][5]
        self.song3 = songs.all_songs["The Animals"][1]
        self.song4 = songs.all_songs["Lou Reed"][1]
        self.song5 = songs.all_songs["Iron Maiden"][1]
        self.song6 = songs.all_songs["Johnny Cash"][2]

    def test_song_one_has_name_no_matter_what(self):
        self.assertEqual("No Matter What", self.song1)

    def test_song_two_has_name_i_see_fire(self):
        self.assertEqual("I See Fire", self.song2)

    def test_song_three_has_name_house_of_rising_sun(self):
        self.assertEqual("House of the Rising Sun", self.song3)

    def test_song_four_has_name_vicious(self):
        self.assertEqual("Vicious", self.song4)

    def test_song_five_has_name_number_of_the_beast(self):
        self.assertEqual("The Number of the Beast", self.song5)

    def test_song_six_has_name_a_boy_named_sue(self):
        self.assertEqual("A Boy Named Sue", self.song6)