''' room.py '''
from pytify.pytifylib import Pytifylib

class Room(Pytifylib):
    ''' room '''
    def __init__(self, pytify, addr):
        self.pytify = pytify
        self.addr = addr
        self.queue = []

    def get_next_song(self):
        ''' get next song '''
        return self.queue[1]

    def get_current_song(self):
        ''' get current playing song '''
        return self.queue[0]

    def get_queue(self):
        ''' return current queue '''
        return self.queue

    def add_song(self, key):
        ''' add song, assuming were in the search '''
        self.queue.append({
            "uri": self._get_song_uri_at_index(key),
            "name": self._get_song_name_at_index(key)
        })

    def remove_song(self, key):
        ''' remove song, assuming were in the search '''
        try:
            self.queue.remove({
                "uri": self._get_song_uri_at_index(key),
                "name": self._get_song_name_at_index(key)
            })
            return 1
        except ValueError:
            print("That song isn't in the queue!")
            return 0

    def get_addr(self):
        ''' return room address '''
        return self.addr
