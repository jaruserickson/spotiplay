#!/usr/bin/python3
from __future__ import absolute_import, unicode_literals
import socket
import json
import sys
import pkg_resources
import pytify.pytifylib
from pytify.strategy import get_pytify_class_by_platform
from pytify.song_list import SongList
from pytify.prompt import custom_prompt
from pytify.commander import Commander

from pytify.room import Room

HOST = 'ec2-54-89-160-77.compute-1.amazonaws.com'
PORT = 8080

class App:
    def __init__(self):
        self.pytify = get_pytify_class_by_platform()()
        self.room = None
        self.command = Commander(self.pytify, self.room)

        self.interaction()

    def list_songs(self, list):
        SongList(list, self.room)

    def host_room(self):
        print('Sending host request...')
        room_addr = create_room(HOST, PORT)
        self.room = Room(self.pytify, room_addr) # no queue
        self.command = Commander(self.pytify, self.room)

    def leave_room(self):
        print('Sending leave request...')
        ret = leave_room(HOST, PORT)
        if ret[0] != '@':
            self.room = None
        print(ret)

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
                    self.list_songs(list=self.pytify.list())
            else:
                print('You need a room to add songs to!')


def create_room(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
    sock.send(('/CREATE_ROOM' + "\r\n").encode('ascii'))
    room_key = sock.recv(1024).decode('ascii')
    sock.close()

    return room_key

def leave_room(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    sock.send(('/LEAVE_ROOM' + "\r\n").encode('ascii'))
    ret_val = sock.recv(1024).decode('ascii')
    sock.close()

    return ret_val

def join_room(host, port, room_addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    sock.send(('/JOIN_ROOM' + "\r\n").encode('ascii'))
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
    try:
        App()
    except EOFError:
        print('\n Closing application...\n')
    except KeyboardInterrupt:
        print('\n Closing application...\n')
