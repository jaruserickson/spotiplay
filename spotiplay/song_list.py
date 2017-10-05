from __future__ import absolute_import, unicode_literals
import curses
import sys
import os
from curses import panel
from spotiplay.strategy import get_pytify_class_by_platform


class SongList():
    def __init__(self, items, room):
        self.pytify = get_pytify_class_by_platform()()
        self.room = room
        self.items = items

        self.position = 2
        self.song_length = len(items) - 1

        # Init curses screen
        self.window = curses.initscr()

        self.window.keypad(1)

        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        # Show shortcuts
        self.shortcuts()

        # Disable echoing of keys to the screen
        curses.noecho()

        # Disable blinking cursor
        curses.curs_set(False)

        # Use user terminal settings
        curses.endwin()

        # Display window
        curses.wrapper(self.display)

    def shortcuts(self):
        self.items.append(' ')
        self.items.append('Keyboard shortcuts')
        self.items.append('==================')
        self.items.append('Navigation:')
        self.items.append('  <k> <up> ')
        self.items.append('  <j> <down> ')
        self.items.append('Prev: <h> <left>')
        self.items.append('Next: <l> <right>')
        self.items.append('Add Song To Queue: <p> <enter>')
        self.items.append('Remove Song From Queue: <r>')
        self.items.append('Search: <s>')
        self.items.append('Play/Pause: <spacebar>')
        self.items.append('Quit: <q>')
        self.items.append('Queue:')
        self.items.append(self.room.get_queue())

    def navigate(self, n):
        self.position += n

        if self.position < 2:
            self.position = 2
        elif self.position > self.song_length:
            self.position = self.song_length

    def exit_if_terminal_size_is_to_small(self):
        # get_terminal_size is introduced in python 3.3
        try:
            (columns, lines) = os.get_terminal_size()
        except AttributeError:
            return

        if columns < 99 and lines < 30:
            msg = '\n Terminal window screen must be at least 99x30\n'
            msg += ' Your size: %sx%s \n'

            sys.exit(msg % (columns, lines))

    def display(self, stdscr):
        self.panel.top()
        self.panel.show()
        stdscr.clear()

        # Temporary solution to warn the user
        self.exit_if_terminal_size_is_to_small()

        # Play keys.
        play = lambda c: c == ord('p') or c == curses.KEY_ENTER or c == 10 or c == 13

        while True:
            stdscr.refresh()
            curses.doupdate()

            for index, item in enumerate(self.items):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                stdscr.addstr(index, 1, str(item), mode)

            key = stdscr.getch()

            # Start song
            if play(key):
                self.room.add_song(int(self.position - 1))

            elif key == ord('r'):
                self.room.remove_song(int(self.position -1))

            # Up
            elif key == ord('k') or key == curses.KEY_UP:
                self.navigate(-1)

            # Down
            elif key == ord('j') or key == curses.KEY_DOWN:
                self.navigate(1)

            # Left
            elif key == ord('h') or key == curses.KEY_LEFT:
                self.pytify.prev()

            # Rights
            elif key == ord('l') or key == curses.KEY_RIGHT:
                self.pytify.listen(self.room.get_next_song())

            # Play/Pause
            elif key == ord(' '):
                self.pytify.play_pause()

            # Search
            elif key == ord('s'):
                break

            # Quit
            elif key == ord('q'):
                break


        stdscr.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()
