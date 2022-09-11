class Guest:
    def __init__(self, cash, fav_genre, fav_song):
        self.cash = cash
        self.fav_genre = fav_genre
        self.fav_song = fav_song

    def join_group(self, guest_group):
        guest_group.total_guests += 1
        return

    def enter_karaoke(self, karaoke_bar):
        if self.cash >= karaoke_bar.entry_fee:
            self.cash -= karaoke_bar.entry_fee
            karaoke_bar.till += karaoke_bar.entry_fee

    def play_fav_song(self, karaoke_song):
        if karaoke_song == self.fav_song:
            print("Woo hoo!")

