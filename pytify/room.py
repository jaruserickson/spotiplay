''' room.py '''
import socket
import json
from pytify.pytifylib import Pytifylib

HOST = 'ec2-54-89-160-77.compute-1.amazonaws.com'
PORT = 8080

class Room(Pytifylib):
    ''' room '''
    def __init__(self, pytify, addr, room_data):
        self.pytify = pytify
        self.addr = addr
        if room_data:
            self.queue = room_data["songs"]
        else:
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
        print(update_queue(self.addr, self.queue))

    def remove_song(self, key):
        ''' remove song, assuming were in the search '''
        try:
            self.queue.remove({
                "uri": self._get_song_uri_at_index(key),
                "name": self._get_song_name_at_index(key)
            })
            ret = update_queue(self.addr, self.queue)
            print(ret)
            return ret[0] == '^'
        except ValueError:
            print("That song isn't in the queue!")
            return 0

    def get_addr(self):
        ''' return room address '''
        return self.addr

def update_queue(addr, queue):
    ''' update queue at addr '''
    if addr:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.send(('/UPDATE_Q' + "\r\n").encode('ascii'))
        sock.send(str(addr).encode('ascii'))
        sock.send(json.dumps(queue).encode('ascii'))

        return sock.recv(1024).decode('ascii')
