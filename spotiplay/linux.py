from __future__ import absolute_import, unicode_literals
import sys
from spotiplay.pytifylib import Pytifylib
from spotiplay.dbus.metadata import Metadata
from spotiplay.dbus.interface import Interface


class Linux(Pytifylib):
    def __init__(self):
        self.interface = Interface.factory('org.mpris.MediaPlayer2.Player')

        self.metadata = Metadata()

    def listen(self, index):
        self.interface.OpenUri(
            self._get_song_uri_at_index(index)
        )

    def listen_uri(self, uri):
        self.interface.OpenUri(uri)

    def next(self):
        self.interface.Next()

    def prev(self):
        self.interface.Previous()

    def play_pause(self):
        self.interface.PlayPause()

    def pause(self):
        self.interface.Stop()

    def get_current_playing(self):
        return self.metadata.get_current_playing()
