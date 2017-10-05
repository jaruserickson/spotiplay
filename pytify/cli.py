#!/usr/bin/python3
''' main cli for spotiplay rooms '''
from __future__ import absolute_import, unicode_literals
import socket
import json
import sys
from Crypto.Cipher import AES

from pytify.strategy import get_pytify_class_by_platform
from pytify.song_list import SongList
from pytify.prompt import custom_prompt
from pytify.commander import Commander

from pytify.room import Room

PORT = 8080
HOST = str(AES.new('1n1dklmnAMADKENM', AES.MODE_ECB).decrypt(b'\xd8\x85\x11\xa85P$\x91\xee\x87\x05>\x9e\x89\xba\xb0\xa5\x14\xfa\xbdu\xe5F\xf6\xa7\xa2\x1d\x92\x1e\x91}\x1f\x96e\x91\x8b\x14\xf6O,&\x16\xd1\xdb\x91\xc4\x98"\xd3\xd2\x1b\x19(\x9f\xa4G[\x18\x8d\\\x06\x81!\x83').strip())[2:-1]

class App:
    ''' cli app '''
    def __init__(self):
        self.pytify = get_pytify_class_by_platform()()
        self.room = None
        self.command = Commander(self.pytify, self.room)

        self.interaction()

    def list_songs(self, song_list):
        ''' display the search results '''
        SongList(song_list, self.room)

    def host_room(self):
        ''' host a room '''
        print('Sending host request...')
        room_addr = create_room(HOST, PORT)
        print('Joined room: %s' % room_addr)
        self.room = Room(self.pytify, room_addr) # no queue
        self.command = Commander(self.pytify, self.room)

    def leave_room(self):
        ''' leave a room '''
        if self.room:
            print('Sending leave request...')
            ret = leave_room(HOST, PORT, self.room.get_addr())
            if ret[0] != '@':
                self.room = None
                print(ret)
                sys.exit()          
        else:
            print("You're not in a room!")

    def join_room(self, addr):
        print('Sending join request...')
        room_data = join_room(HOST, PORT, addr)
        if room_data != {}:
            self.room = Room(self.pytify, addr, room_data) # could be a queue
            self.command = Commander(self.pytify, self.room)
        else:
            print('Problem joining room.')

    def interaction(self):
        print('spotiplay [pytify] 0.0.1')

        while 1:
            search_input = custom_prompt()

            if search_input == '/create_room':
                if not self.room:
                    self.host_room()
                continue

            elif search_input == '/leave':
                self.leave_room()
                continue

            elif search_input.split(' ')[0] == '/join':
                self.join_room(search_input.split(' ')[1])
                continue

            if self.command.run(search_input):
                continue

            if self.room:
                search = self.pytify.query(search_input)
                if search:
                    self.list_songs(self.pytify.list())
            else:
                print('You need a room to add songs to!')


def create_room(host, port):
    ''' actually send the create room request to the server '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    sock.send(('/CREATE_ROOM').encode('ascii'))
    room_key = sock.recv(1024).decode('ascii')
    sock.close()

    return room_key

def leave_room(host, port, addr):
    ''' actually send the leave room request to the server '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    sock.send(('/LEAVE_ROOM').encode('ascii'))
    sock.send(addr.encode('ascii'))

    ret_val = sock.recv(1024).decode('ascii')
    sock.close()

    return ret_val

def join_room(host, port, room_addr):
    ''' actually send the join room request to the server '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    sock.send(('/JOIN_ROOM').encode('ascii'))
    sock.send((str(room_addr)))
    ret_val = sock.recv(1024).decode('ascii')
    room_data = {}
    if ret_val[0] != '@':
        room_data = json.loads(ret_val)
    else:
        print(ret_val)

    sock.close()
    return room_data

def main():
    ''' main '''
    try:
        App()
    except EOFError:
        print('\n Closing application...\n')
    except KeyboardInterrupt:
        print('\n Closing application...\n')
