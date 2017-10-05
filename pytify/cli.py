#!/usr/bin/python3
from __future__ import absolute_import, unicode_literals
import pytify.pytifylib
from pytify.strategy import get_pytify_class_by_platform
from pytify.song_list import SongList
from pytify.prompt import custom_prompt
from pytify.commander import Commander
from room.room import Room
import argparse
import sys
import pkg_resources

from pytify.room import Room


class App:
    def __init__(self):
        self.pytify = get_pytify_class_by_platform()()
        self.room = None
        self.command = Commander(self.pytify, self.room)

        self.interaction()

    def list_songs(self, list):
        SongList(list, self.room)

    def host_room(self):
        print('hosting')
        # connect
        addr = '123.123.123.123'
        self.room = Room(self.pytify, addr)
        self.command = Commander(self.pytify, self.room)

    def leave_room(self):
        print('leaving')
        # leave
        self.room = None

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

            if self.command.run(search_input):
                continue

            if self.room:
                search = self.pytify.query(search_input)
                if search:
                    self.list_songs(list=self.pytify.list())
            else:
                print('You need a room to add songs to!')


def main():
    try:
        App()
    except EOFError:
        print('\n Closing application...\n')
    except KeyboardInterrupt:
        print('\n Closing application...\n')
