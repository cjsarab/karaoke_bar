class GuestGroup:
    def __init__(self, total_guests):
        self.total_guests = total_guests

    def enter_room(self, room_size):
        if self.total_guests <= room_size:
            return True
        else:
            return False
    